import var, sys
from PyQt5 import QtGui
import string
import random

class Eventos():

    def Salir(self):
        try:
            sys.exit()
        except Exception as error:
            print("Error %s: " % str(error))

    def CopiarPassword(self):
        if var.ui.lineEdit_password.text() != '':
            cb = QtGui.QGuiApplication.clipboard()
            cb.clear(mode=cb.Clipboard)
            cb.setText(var.ui.lineEdit_password.text(), mode=cb.Clipboard)
            var.ui.labelstatusbar.setText('CONTRASEÑA COPIADA')
        else:
            var.ui.labelstatusbar.setText('GENERA UNA CONTRASEÑA PARA PODER COPIARLA')


    def GenerarPassword(self):

        password_size = var.ui.spinBox_password_size.value()
        numbers = var.ui.checkBox_numbers.isChecked()
        lowercase_letters = var.ui.checkBox_lowercase_letters.isChecked()
        uppercase_letters = var.ui.checkBox_uppercase_letters.isChecked()
        symbols = var.ui.checkBox_symbols.isChecked()

        password = ''
        password_printable = ''

        if not numbers and not lowercase_letters and not uppercase_letters and not symbols:
            var.ui.labelstatusbar.setText('MARCA LOS CAMPOS PARA GENERAR UNA CONTRASEÑA')
        else:
            if numbers:
                password_printable += string.digits
            if lowercase_letters:
                password_printable += string.ascii_lowercase
            if uppercase_letters:
                password_printable += string.ascii_uppercase
            if symbols:
                password_printable += string.punctuation
            max_random = len(password_printable) - 1
            for n in range(password_size):
                x = random.randint(0, max_random)
                password += password_printable[x]
            var.ui.lineEdit_password.setText(password)
            var.ui.labelstatusbar.setText('CONTRASEÑA GENERADA')


