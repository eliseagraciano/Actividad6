# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(301, 407)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Mostrar_pushButton = QPushButton(self.centralwidget)
        self.Mostrar_pushButton.setObjectName(u"Mostrar_pushButton")

        self.gridLayout_2.addWidget(self.Mostrar_pushButton, 3, 0, 1, 1)

        self.Agregar_inicio_pushButton = QPushButton(self.centralwidget)
        self.Agregar_inicio_pushButton.setObjectName(u"Agregar_inicio_pushButton")

        self.gridLayout_2.addWidget(self.Agregar_inicio_pushButton, 1, 0, 1, 1)

        self.Agregar_final_pushButton = QPushButton(self.centralwidget)
        self.Agregar_final_pushButton.setObjectName(u"Agregar_final_pushButton")

        self.gridLayout_2.addWidget(self.Agregar_final_pushButton, 2, 0, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)

        self.Destino_y_spinBox = QSpinBox(self.groupBox)
        self.Destino_y_spinBox.setObjectName(u"Destino_y_spinBox")

        self.gridLayout.addWidget(self.Destino_y_spinBox, 5, 1, 1, 1)

        self.Blue_spinBox = QSpinBox(self.groupBox)
        self.Blue_spinBox.setObjectName(u"Blue_spinBox")

        self.gridLayout.addWidget(self.Blue_spinBox, 9, 1, 1, 1)

        self.Green_spinBox = QSpinBox(self.groupBox)
        self.Green_spinBox.setObjectName(u"Green_spinBox")

        self.gridLayout.addWidget(self.Green_spinBox, 8, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)

        self.Destino_x_spinBox = QSpinBox(self.groupBox)
        self.Destino_x_spinBox.setObjectName(u"Destino_x_spinBox")

        self.gridLayout.addWidget(self.Destino_x_spinBox, 3, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)

        self.Velocidad_spinBox = QSpinBox(self.groupBox)
        self.Velocidad_spinBox.setObjectName(u"Velocidad_spinBox")

        self.gridLayout.addWidget(self.Velocidad_spinBox, 6, 1, 1, 1)

        self.Red_spinBox = QSpinBox(self.groupBox)
        self.Red_spinBox.setObjectName(u"Red_spinBox")

        self.gridLayout.addWidget(self.Red_spinBox, 7, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 9, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)

        self.Id_spinBox = QSpinBox(self.groupBox)
        self.Id_spinBox.setObjectName(u"Id_spinBox")

        self.gridLayout.addWidget(self.Id_spinBox, 0, 1, 1, 1)

        self.Origen_x_spinBox = QSpinBox(self.groupBox)
        self.Origen_x_spinBox.setObjectName(u"Origen_x_spinBox")

        self.gridLayout.addWidget(self.Origen_x_spinBox, 1, 1, 1, 1)

        self.Origen_y_spinBox = QSpinBox(self.groupBox)
        self.Origen_y_spinBox.setObjectName(u"Origen_y_spinBox")

        self.gridLayout.addWidget(self.Origen_y_spinBox, 2, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.salida = QPlainTextEdit(self.centralwidget)
        self.salida.setObjectName(u"salida")

        self.gridLayout_2.addWidget(self.salida, 0, 1, 3, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 301, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.Agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar inicio", None))
        self.Agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar final", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"particulas", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Destino x", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Destino y", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"velocidad", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Origen x", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Origen Y", None))
    # retranslateUi

