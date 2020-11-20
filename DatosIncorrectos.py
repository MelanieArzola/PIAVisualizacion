#Librería utilizada para crear la aplicación/ventana.
from PyQt5 import QtCore, QtGui, QtWidgets

#Donde se crea la aplicación (Ventana que avisa que los datos que se intentan ingresar son incorrectos, se utiliza en la ventana LOGIN)
class Ui_DatosIncorrectos(object):
    def setupUi(self, DatosIncorrectos):
        DatosIncorrectos.setObjectName("DatosIncorrectos")
        DatosIncorrectos.resize(285, 100)
        DatosIncorrectos.setStyleSheet("background-color: rgb(226, 230, 255);")
        self.centralwidget = QtWidgets.QWidget(DatosIncorrectos)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 251, 71))
        self.label.setObjectName("label")
        DatosIncorrectos.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DatosIncorrectos)
        self.statusbar.setObjectName("statusbar")
        DatosIncorrectos.setStatusBar(self.statusbar)

        self.retranslateUi(DatosIncorrectos)
        QtCore.QMetaObject.connectSlotsByName(DatosIncorrectos)

    #MENSAJE ASIGNADO EN EL LABEL.
    def retranslateUi(self, DatosIncorrectos):
        _translate = QtCore.QCoreApplication.translate
        DatosIncorrectos.setWindowTitle(_translate("DatosIncorrectos", "MainWindow"))
        self.label.setText(_translate("DatosIncorrectos", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">DATOS INCORRECTOS</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">INTENTELO DE NUEVO</span></p></body></html>"))

#PERMITE QUE LA APLICACIÓN SE CIERRE.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DatosIncorrectos = QtWidgets.QMainWindow()
    ui = Ui_DatosIncorrectos()
    ui.setupUi(DatosIncorrectos)
    DatosIncorrectos.show()
    sys.exit(app.exec_())
