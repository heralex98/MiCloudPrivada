# FTP server gui with PyQt
# https://pythonbasics.org/pyqt/

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMessageBox, QDialog, QFileDialog
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer
from segundaventana import Ui_SegundaVentana
import sys
import os
import threading
 
class Example(QtWidgets.QMainWindow):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SegundaVentana()
        self.ui.setupUi(self.window)
        self.window.show()

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



    def onClick(self):
        print('start')

        user = self.lineEditUser.text()
        passw = self.lineEditPassword.text()
        
        self.authorizer.add_user(user, passw, '.', perm='elrw')
        self.address = ('0.0.0.0', 5000)
        self.server = ThreadedFTPServer(self.address, self.handler)

        QMessageBox.information(self, "FTP Server started", "FTP Server started")
        self.start()


    def _run_server(self):
        self.server.serve_forever()
    
    def start(self):
        srv = threading.Thread(target=self._run_server)
        srv.deamon = True
        srv.start()
        
    def onStop(self):
        print('stop')
        self.server.close_all()        
        QMessageBox.information(self, "FTP Server stopped", "FTP Server stopped")

app = QtWidgets.QApplication([])
win = Example()
win.show()
sys.exit(app.exec())
