# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QCursor, QFont, QIcon)
from PySide6.QtWidgets import (QCheckBox, QHBoxLayout, QLabel, QLayout, QPushButton, QSizePolicy,
                               QSpacerItem, QSpinBox, QTextEdit, QVBoxLayout,
                               QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(687, 230)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(687, 230))
        MainWindow.setMaximumSize(QSize(687, 230))
        icon = QIcon()
        icon.addFile(u"./assert/file-conversion.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 688, 231))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 0, 2, 4)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.label_orig = QLabel(self.layoutWidget)
        self.label_orig.setObjectName(u"label_orig")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_orig.sizePolicy().hasHeightForWidth())
        self.label_orig.setSizePolicy(sizePolicy1)
        self.label_orig.setMinimumSize(QSize(285, 168))
        self.label_orig.setMaximumSize(QSize(285, 168))
        self.label_orig.setCursor(QCursor(Qt.CursorShape.CrossCursor))
        self.label_orig.setStyleSheet(u"border: 1px solid black;\n"
                                      "background-color: white;")
        self.label_orig.setMargin(0)

        self.horizontalLayout_2.addWidget(self.label_orig)

        self.label_new = QLabel(self.layoutWidget)
        self.label_new.setObjectName(u"label_new")
        sizePolicy1.setHeightForWidth(self.label_new.sizePolicy().hasHeightForWidth())
        self.label_new.setSizePolicy(sizePolicy1)
        self.label_new.setMinimumSize(QSize(285, 168))
        self.label_new.setMaximumSize(QSize(285, 168))
        self.label_new.setCursor(QCursor(Qt.CursorShape.CrossCursor))
        self.label_new.setMouseTracking(False)
        self.label_new.setStyleSheet(u"border: 1px solid black;\n"
                                     "background-color: white;")
        self.label_new.setMargin(0)

        self.horizontalLayout_2.addWidget(self.label_new)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.textEdit = QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy2)
        self.textEdit.setMaximumSize(QSize(16777215, 50))
        self.textEdit.setReadOnly(True)
        self.textEdit.setOverwriteMode(False)
        self.textEdit.setCursorWidth(1)

        self.horizontalLayout_4.addWidget(self.textEdit)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalLayout_4.setStretch(0, 9)
        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalLayout.setStretch(0, 9)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout_2.setContentsMargins(8, 0, 0, -1)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.quick_mode = QCheckBox(self.layoutWidget)
        self.quick_mode.setObjectName(u"quick_mode")
        sizePolicy.setHeightForWidth(self.quick_mode.sizePolicy().hasHeightForWidth())
        self.quick_mode.setSizePolicy(sizePolicy)
        self.quick_mode.setCheckable(True)
        self.quick_mode.setChecked(False)

        self.verticalLayout_2.addWidget(self.quick_mode)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.spinBox = QSpinBox(self.layoutWidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(10)
        self.spinBox.setValue(1)

        self.horizontalLayout_5.addWidget(self.spinBox)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.pB_init = QPushButton(self.layoutWidget)
        self.pB_init.setObjectName(u"pB_init")
        sizePolicy.setHeightForWidth(self.pB_init.sizePolicy().hasHeightForWidth())
        self.pB_init.setSizePolicy(sizePolicy)
        self.pB_init.setCheckable(False)
        self.pB_init.setAutoDefault(False)

        self.verticalLayout_2.addWidget(self.pB_init)

        self.pB_dir = QPushButton(self.layoutWidget)
        self.pB_dir.setObjectName(u"pB_dir")
        sizePolicy.setHeightForWidth(self.pB_dir.sizePolicy().hasHeightForWidth())
        self.pB_dir.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.pB_dir)

        self.pB_file = QPushButton(self.layoutWidget)
        self.pB_file.setObjectName(u"pB_file")
        sizePolicy.setHeightForWidth(self.pB_file.sizePolicy().hasHeightForWidth())
        self.pB_file.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.pB_file)

        self.pB_convert = QPushButton(self.layoutWidget)
        self.pB_convert.setObjectName(u"pB_convert")
        sizePolicy.setHeightForWidth(self.pB_convert.sizePolicy().hasHeightForWidth())
        self.pB_convert.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.pB_convert)

        self.pB_save = QPushButton(self.layoutWidget)
        self.pB_save.setObjectName(u"pB_save")
        sizePolicy.setHeightForWidth(self.pB_save.sizePolicy().hasHeightForWidth())
        self.pB_save.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.pB_save)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(0, 9)
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.pB_dir, self.pB_file)
        QWidget.setTabOrder(self.pB_file, self.pB_convert)
        QWidget.setTabOrder(self.pB_convert, self.pB_save)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"dxf\u8f6c\u6362\u5668", None))
        self.label_orig.setText("")
        self.label_new.setText("")
        self.textEdit.setMarkdown("")
        self.textEdit.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"0/0", None))
        self.quick_mode.setText(QCoreApplication.translate("MainWindow", u"Quick Mode", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.pB_init.setText(QCoreApplication.translate("MainWindow", u"Init", None))
        self.pB_dir.setText(QCoreApplication.translate("MainWindow", u"Select Dir", None))
        self.pB_file.setText(QCoreApplication.translate("MainWindow", u"Select File", None))
        self.pB_convert.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.pB_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi
