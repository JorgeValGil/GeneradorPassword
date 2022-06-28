# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 320)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icono/icono.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.spinBox_password_size = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_password_size.setGeometry(QtCore.QRect(225, 55, 42, 22))
        self.spinBox_password_size.setMinimum(1)
        self.spinBox_password_size.setMaximum(256)
        self.spinBox_password_size.setObjectName("spinBox_password_size")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 100, 301, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox_numbers = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_numbers.setFont(font)
        self.checkBox_numbers.setChecked(True)
        self.checkBox_numbers.setObjectName("checkBox_numbers")
        self.verticalLayout_3.addWidget(self.checkBox_numbers)
        self.checkBox_symbols = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_symbols.setFont(font)
        self.checkBox_symbols.setChecked(True)
        self.checkBox_symbols.setObjectName("checkBox_symbols")
        self.verticalLayout_3.addWidget(self.checkBox_symbols)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_uppercase_letters = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_uppercase_letters.setFont(font)
        self.checkBox_uppercase_letters.setChecked(True)
        self.checkBox_uppercase_letters.setObjectName("checkBox_uppercase_letters")
        self.verticalLayout_2.addWidget(self.checkBox_uppercase_letters)
        self.checkBox_lowercase_letters = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_lowercase_letters.setFont(font)
        self.checkBox_lowercase_letters.setCheckable(True)
        self.checkBox_lowercase_letters.setChecked(True)
        self.checkBox_lowercase_letters.setObjectName("checkBox_lowercase_letters")
        self.verticalLayout_2.addWidget(self.checkBox_lowercase_letters)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.labe_size = QtWidgets.QLabel(self.centralwidget)
        self.labe_size.setGeometry(QtCore.QRect(20, 60, 150, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labe_size.setFont(font)
        self.labe_size.setObjectName("labe_size")
        self.label_titulo = QtWidgets.QLabel(self.centralwidget)
        self.label_titulo.setGeometry(QtCore.QRect(10, 10, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_titulo.setFont(font)
        self.label_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titulo.setObjectName("label_titulo")
        self.pushButton_generar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_generar.setGeometry(QtCore.QRect(10, 240, 75, 23))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/aceptar/aceptar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_generar.setIcon(icon1)
        self.pushButton_generar.setObjectName("pushButton_generar")
        self.pushButton_salir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_salir.setGeometry(QtCore.QRect(235, 240, 75, 23))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/salir/salir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_salir.setIcon(icon2)
        self.pushButton_salir.setObjectName("pushButton_salir")
        self.pushButton_copiar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_copiar.setGeometry(QtCore.QRect(235, 199, 75, 23))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/copiar/copiar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_copiar.setIcon(icon3)
        self.pushButton_copiar.setObjectName("pushButton_copiar")
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(10, 200, 200, 20))
        self.lineEdit_password.setReadOnly(True)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.labelstatusbar = QtWidgets.QLabel(self.centralwidget)
        self.labelstatusbar.setGeometry(QtCore.QRect(110, 260, 47, 13))
        self.labelstatusbar.setText("")
        self.labelstatusbar.setObjectName("labelstatusbar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Generador Contraseñas"))
        self.spinBox_password_size.setToolTip(_translate("MainWindow", "Tamaño de la contraseña"))
        self.checkBox_numbers.setText(_translate("MainWindow", "Números"))
        self.checkBox_symbols.setText(_translate("MainWindow", "Símbolos"))
        self.checkBox_uppercase_letters.setText(_translate("MainWindow", "Letras mayúsuculas"))
        self.checkBox_lowercase_letters.setText(_translate("MainWindow", "Letras minúsculas"))
        self.labe_size.setText(_translate("MainWindow", "Tamaño de la contraseña:"))
        self.label_titulo.setText(_translate("MainWindow", "GENERADOR DE CONTRASEÑAS"))
        self.pushButton_generar.setToolTip(_translate("MainWindow", "Generar contraseña"))
        self.pushButton_generar.setText(_translate("MainWindow", "Generar"))
        self.pushButton_salir.setToolTip(_translate("MainWindow", "Salir"))
        self.pushButton_salir.setText(_translate("MainWindow", "Salir"))
        self.pushButton_copiar.setToolTip(_translate("MainWindow", "Copiar contraseña"))
        self.pushButton_copiar.setText(_translate("MainWindow", "Copiar"))
        self.lineEdit_password.setPlaceholderText(_translate("MainWindow", "Contraseña generada..."))
import aceptar_rc
import copiar_rc
import icono_rc
import salir_rc
