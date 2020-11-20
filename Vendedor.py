#Librería para crear nuestra aplicación.
from PyQt5 import QtCore, QtGui, QtWidgets

#Creación de la aplicación. (Menú del vendedor)
class Ui_Vendedor(object):
    def setupUi(self, Vendedor):
        Vendedor.setObjectName("Vendedor")
        Vendedor.resize(233, 136)
        Vendedor.setStyleSheet("background-color: rgb(226, 230, 255);")
        self.centralwidget = QtWidgets.QWidget(Vendedor)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 231, 41))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 60, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 60, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        Vendedor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Vendedor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 233, 21))
        self.menubar.setObjectName("menubar")
        Vendedor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Vendedor)
        self.statusbar.setObjectName("statusbar")
        Vendedor.setStatusBar(self.statusbar)

        self.retranslateUi(Vendedor)
        QtCore.QMetaObject.connectSlotsByName(Vendedor)

    #Asignación de texto a los botones.
    def retranslateUi(self, Vendedor):
        _translate = QtCore.QCoreApplication.translate
        Vendedor.setWindowTitle(_translate("Vendedor", "MainWindow"))
        self.label.setText(_translate("Vendedor", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Menu Principal</span></p></body></html>"))
        self.pushButton.setText(_translate("Vendedor", "Venta Nueva"))
        self.pushButton_2.setText(_translate("Vendedor", "Cierre del día"))

#Cerrar aplicación.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Vendedor = QtWidgets.QMainWindow()
    ui = Ui_Vendedor()
    ui.setupUi(Vendedor)
    Vendedor.show()
    sys.exit(app.exec_())
