from os import walk, path
from sys import argv, exit
import configparser

from cv2 import imread, resize, cvtColor, COLOR_BGR2RGB, IMREAD_GRAYSCALE, threshold, \
                THRESH_BINARY, flip, findContours, RETR_CCOMP, CHAIN_APPROX_NONE

import ezdxf
from PySide6.QtGui import QImage, QPixmap, QTextCursor
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui_mainwindow import Ui_MainWindow

import configparser

configParser = configparser.ConfigParser()
configParser.read("dxf_conf.ini", encoding="utf-8")

# 返回 List
gray_scale = 211
try:
    gray_scale = int(configParser["set_para"]["gray_scale"])
except ValueError:
    pass


class Convertor:
    def __init__(self, _ui: Ui_MainWindow):
        self.textEdit_isNotNone = 0
        self.scale = 5
        self.ui = _ui
        self.doc = None

        self.file_path = ""
        self.file_paths = []
        self.file_num = 0
        self.file_all = 0

        self.flag_file = 0
        self.flag_con = 0

        self.ui.pB_init.clicked.connect(self.init)
        self.ui.pB_file.clicked.connect(self.select_file)
        self.ui.pB_dir.clicked.connect(self.select_dir)
        self.ui.pB_convert.clicked.connect(lambda: self.convert(self.file_path))
        self.ui.pB_save.clicked.connect(self.save_file)
        self.ui.spinBox.valueChanged.connect(self.scale_update)
        self.ui.quick_mode.stateChanged.connect(lambda: self.ui.pB_file.setEnabled(not self.ui.pB_file.isEnabled()))

    def init(self):
        self.clear_img()
        self.doc = None
        self.file_path = ""
        self.file_paths = []
        self.file_num = 0
        self.file_all = 0
        self.flag_file = 0
        self.flag_con = 0
        self.ui.label_2.setText("0/0")
        self.output_text("成功初始化")

    def scale_update(self):
        self.scale = int(self.ui.spinBox.value())

    def progress_upgrade(self):
        self.ui.label_2.setText(f"{self.file_num + 1}/{self.file_all}")

    def show_fig(self, fig, file_path):
        try:
            # 读取图片
            if isinstance(file_path, str):
                img = imread(file_path)
                ih, iw, _ = img.shape
            else:
                img = file_path
                ih, iw = img.shape
            # 获取高和宽

            # 获取标签的长和高
            w = fig.geometry().width()
            h = fig.geometry().height()
            # 下面的目的是为了保持原始的纵横比
            if iw / w > ih / h:
                scal = w / iw
                nw = w
                nh = int(scal * ih)
                im_new = resize(img, (nw, nh))
            else:
                scal = w / iw
                nw = int(scal * iw)
                nh = h
                im_new = resize(img, (nw, nh))
            frame = cvtColor(im_new, COLOR_BGR2RGB)
            im = QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[2] * frame.shape[1],
                        QImage.Format_RGB888)
            fig.setPixmap(QPixmap.fromImage(im))
            if not self.flag_file:
                self.output_text(f"成功显示{self.file_path}原图片")
            else:
                self.output_text(f"成功显示{self.file_path}转换图片")

        except Exception as e:
            self.output_text(repr(e))

    def clear_img(self):
        self.ui.label_orig.clear()
        self.ui.label_new.clear()

    def output_text(self, output):
        cursor = self.ui.textEdit.textCursor()
        cursor.movePosition(QTextCursor.End)
        if self.textEdit_isNotNone:
            cursor.insertText('\n' + output)
        else:
            cursor.insertText(output)
            self.textEdit_isNotNone = 1
        self.ui.textEdit.ensureCursorVisible()

    def get_image_paths(self, folder_name):
        image_paths = []
        for root, dirs, files in walk(folder_name):
            for file in files:
                if file.endswith((".jpg", ".png")):
                    image_paths.append(path.join(root, file))
        return image_paths

    def select_file(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("图像文件 (*.png *.jpg);")
        path = None
        if dialog.exec():
            path = dialog.selectedFiles()[0]

        if path is None:
            return

        self.init()
        self.file_path = path
        self.file_all = 1
        self.progress_upgrade()
        self.output_text(f"已选择{self.file_path}文件")
        self.show_fig(self.ui.label_orig, self.file_path)
        self.flag_file = 1

    def select_dir(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setOption(QFileDialog.ShowDirsOnly)
        dir_path = None
        if dialog.exec():
            dir_path = dialog.selectedFiles()[0]
        if dir_path is None:
            return
        file_paths = self.get_image_paths(dir_path)
        file_all = len(file_paths)
        if file_all:
            self.init()
            self.file_all = file_all
            self.output_text(f"已选择{dir_path}文件夹")
            if self.ui.quick_mode.isChecked():
                for file in file_paths:
                    self.progress_upgrade()
                    self.flag_file = 1
                    self.convert(file)
                    self.flag_con = 1
                    self.save_file(name=file)

            else:
                self.progress_upgrade()
                self.file_paths = file_paths
                self.file_path = self.file_paths[self.file_num]
                self.show_fig(self.ui.label_orig, self.file_path)
                self.flag_file = 1

    def convert(self, path):
        if self.flag_file:
            # 读取图像
            image = imread(path, IMREAD_GRAYSCALE)
            height, width = image.shape[:2]
            scale = self.scale
            re_img = resize(image, (width * scale, height * scale))

            if image is None:
                raise ValueError("无法读取图像文件")

            # 使用阈值处理来二值化图像（如果需要进一步处理）
            _, threshold_pic = threshold(re_img, gray_scale, 255, THRESH_BINARY)

            # 图像反转
            flipped_image = flip(threshold_pic, -1)
            flipped_image2 = flip(flipped_image, 1)

            # 找到轮廓
            # cv2.CHAIN_APPROX_NONE找到所有轮廓点  这个文件相对较大
            contours, hierarchy = findContours(flipped_image2, RETR_CCOMP, CHAIN_APPROX_NONE)

            # 创建新的DXF文档
            self.doc = ezdxf.new()
            msp = self.doc.modelspace()
            hatch = msp.add_hatch()

            # 遍历轮廓并添加到DXF文件中
            for i, contour in enumerate(contours):
                # 将轮廓的ndarray转换为列表的列表（每个子列表是一个(x, y)坐标对）
                points = contour.reshape(-1, 2).tolist()
                if points[0][0] * points[0][1] != 0:
                    polyline = msp.add_lwpolyline(points, close=True)
                    hatch.paths.add_polyline_path(polyline)

            hatch.set_pattern_fill('SOLID', color=7)

            self.output_text(f"{path}图片转换成功")
            if not self.ui.quick_mode.isChecked():
                self.show_fig(self.ui.label_new, threshold_pic)
            self.flag_file = 0
            self.flag_con = 1

        else:
            self.output_text("请先选择图片……")

    def save_file(self, name=None):
        if self.flag_con:
            # 保存DXF文件
            if name:
                self.doc.saveas(name.split('.')[0] + ".dxf")
                self.output_text(f"{name}图片保存成功")
            else:
                self.doc.saveas(self.file_path.split('.')[0] + ".dxf")
                self.output_text(f"{self.file_path}图片保存成功")

            self.flag_con = 0
            self.file_num += 1

            if self.ui.quick_mode.isChecked():
                return

            if self.file_num < self.file_all:
                self.file_path = self.file_paths[self.file_num]
                self.flag_file = 1
                self.show_fig(self.ui.label_orig, self.file_path)
                self.progress_upgrade()
        else:
            self.output_text("请先转换图片……")


if __name__ == '__main__':
    app = QApplication(argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    convertor = Convertor(ui)
    window.show()
    exit(app.exec())
