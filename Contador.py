#Librería para crear nuestra aplicación.
from PyQt5 import QtCore, QtGui, QtWidgets

#Creación de la aplicación. (Menu del Contador)
class Ui_Contador(object):
    def setupUi(self, Contador):
        Contador.setObjectName("Contador")
        Contador.resize(531, 123)
        Contador.setStyleSheet("background-color: rgb(226, 230, 255);")
        self.centralwidget = QtWidgets.QWidget(Contador)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 531, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 60, 75, 23))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(130, 60, 75, 23))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(230, 60, 75, 23))
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(330, 60, 75, 23))
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(430, 60, 75, 23))
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        Contador.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Contador)
        self.statusbar.setObjectName("statusbar")
        Contador.setStatusBar(self.statusbar)

        self.retranslateUi(Contador)
        QtCore.QMetaObject.connectSlotsByName(Contador)

    #Asignación de texto a los botones.
    def retranslateUi(self, Contador):
        _translate = QtCore.QCoreApplication.translate
        Contador.setWindowTitle(_translate("Contador", "MainWindow"))
        self.label_2.setText(_translate("Contador", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Menú Principal</span></p></body></html>"))
        self.pushButton_4.setText(_translate("Contador", "Compras"))
        self.pushButton_5.setText(_translate("Contador", "Ventas"))
        self.pushButton_6.setText(_translate("Contador", "Inventario"))
        self.pushButton_7.setText(_translate("Contador", "Facturación"))
        self.pushButton_8.setText(_translate("Contador", "Estadísticas"))

#Cerrar aplicación.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Contador = QtWidgets.QMainWindow()
    ui = Ui_Contador()
    ui.setupUi(Contador)
    Contador.show()
    sys.exit(app.exec_())
