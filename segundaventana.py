# Form implementation generated from reading ui file 'segunda_ventana.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt6.uic import loadUi


class Ui_SegundaVentana(object):

    def setupUi(self, SegundaVentana):
        SegundaVentana.setObjectName("SegundaVentana")
        SegundaVentana.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SegundaVentana)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 130, 75, 23))
        self.pushButton.setObjectName("pushButton")


        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 170, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 210, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 250, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        SegundaVentana.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SegundaVentana)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        SegundaVentana.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SegundaVentana)
        self.statusbar.setObjectName("statusbar")
        SegundaVentana.setStatusBar(self.statusbar)

        self.retranslateUi(SegundaVentana)
        QtCore.QMetaObject.connectSlotsByName(SegundaVentana)

        self.pushButton.clicked.connect(self.browsefiles)
        self.pushButton_4.clicked.connect(self.savefiles)

    def browsefiles(self):
        QFileDialog.getOpenFileName(parent=None, caption='Open File',
                                    directory='C:\\Users\\Sergi\\Documents\\GitHub\\MiCloudPrivada', filter='',
                                    initialFilter='')
    def savefiles(self):
        QFileDialog.getSaveFileName(parent=None, caption='Open File',
                                    directory='C:\\Users\\Sergi\\Documents\\GitHub\\MiCloudPrivada', filter='',
                                    initialFilter='')



    def retranslateUi(self, SegundaVentana):
        _translate = QtCore.QCoreApplication.translate
        SegundaVentana.setWindowTitle(_translate("SegundaVentana", "MainWindow"))
        self.pushButton.setText(_translate("SegundaVentana", "Descargar"))
        self.pushButton_2.setText(_translate("SegundaVentana", "Actualizar"))
        self.pushButton_3.setText(_translate("SegundaVentana", "Eliminar"))
        self.pushButton_4.setText(_translate("SegundaVentana", "Subir"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    SegundaVentana = QtWidgets.QMainWindow()
    ui = Ui_SegundaVentana()
    ui.setupUi(SegundaVentana)
    SegundaVentana.show()
    sys.exit(app.exec())
