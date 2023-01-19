# FTP server gui with PyQt
# https://pythonbasics.org/pyqt/

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMessageBox, QDialog, QFileDialog
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer
from segundaventana import Ui_SegundaVentana
from PyQt5 import QtCore, QtGui
import sys
import os
import threading
import sqlite3


conn = sqlite3.connect('MiCLoudPrivada')
c = conn.cursor()

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

class Example(QtWidgets.QMainWindow):
    def openWindow(self):
        user = self.lineEditUser.text()
        passw = self.lineEditPassword.text()
        if user == 'adminServer'and passw == 'adminServer':
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_SegundaVentana()
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            QMessageBox.information(self, 'ADVERTENCIA', 'ATENCIÓN, el usuario ingresado o contraseña son erroneos')

    def __init__(self):
        super(Example, self).__init__()
        uic.loadUi('gui.ui', self)
        self.pushButtonStart.clicked.connect(self.onClick)
        self.pushButtonStop.clicked.connect(self.onStop)
        self.pushButton.clicked.connect(self.openWindow)

        self.authorizer = DummyAuthorizer()
        self.authorizer.add_anonymous(os.getcwd())
    
        self.handler = FTPHandler
        self.handler.authorizer = self.authorizer
        self.handler.banner = "pyftpdlib based ftpd ready."

        # set a limit for connections
        self.max_cons = 256
        self.max_cons_per_ip = 5

        self.label_4.setGeometry(QtCore.QRect(0, 0, 414, 228))
        self.label_4.setStyleSheet("background-image: url(.//FONDO//ita.jpg);\n""background-repeat: no-repeat;\n"
                                 ""
                                 "")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(".//FONDO//ita.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(False)



    def onClick(self):
        print('iniciar')

        try:
            os.mkdir('./Almacenamiento')
        except:
            print('ya existe carpeta')

        c.execute("SELECT usuario FROM usuariosFTP")
        i = c.fetchall()
        f = i
        cont = 0
        contC = 0

        for x in f:
            c.execute("SELECT carpeta FROM usuariosFTP")
            carpetaAUX = c.fetchall()
            carpeta = listToString(carpetaAUX[contC])
            print(carpeta)
            try:
                os.mkdir('./Almacenamiento/'+carpeta)
                print(x)
                contC = contC + 1
            except:
                print(x)
                contC = contC + 1

        for n in i:
            c.execute("SELECT usuario FROM usuariosFTP")
            usuarioAUX = c.fetchall()
            usuario = listToString(usuarioAUX[cont])
            print(usuario)

            c.execute("SELECT contraseña FROM usuariosFTP")
            passwordAUX = c.fetchall()
            password = listToString(passwordAUX[cont])
            print(password)

            c.execute("SELECT carpeta FROM usuariosFTP")
            carpetaAUX = c.fetchall()
            carpeta = listToString(carpetaAUX[cont])
            print(carpeta)

            c.execute("SELECT permisos FROM usuariosFTP")
            permisosAUX = c.fetchall()
            permisos = listToString(permisosAUX[cont])
            print(permisos)

            self.authorizer.add_user(usuario, password, carpeta, perm=permisos)
            print(n)
            cont = cont + 1

        self.authorizer.add_user('adminCliente', 'adminCliente', './Almacenamiento', perm='elradfmwMT')
        self.address = ('0.0.0.0', 5000)
        self.server = ThreadedFTPServer(self.address, self.handler)

        QMessageBox.information(self, "ADVERTENCIA", "FTP Server iniciado")
        self.start()


    def _run_server(self):
        self.server.serve_forever()
    
    def start(self):
        srv = threading.Thread(target=self._run_server)
        srv.deamon = True
        srv.start()
        
    def onStop(self):
        try:
            print('stop')
            self.server.close_all()
            QMessageBox.information(self, "ADVERTENCIA", "FTP Server detenido")
        except:
            QMessageBox.information(self, "ADVERTENCIA", "No hay un server iniciado")

app = QtWidgets.QApplication([])
win = Example()
win.show()
sys.exit(app.exec())
