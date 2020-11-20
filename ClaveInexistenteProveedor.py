#Librería utilizada para crear la aplicación/ventana.
from PyQt5 import QtCore, QtGui, QtWidgets

#Donde se crea la aplicación (Ventana que avisa que la clave de proveedor a utilizar no existe, por lo tanto se tiene que elegir otra)
#Se utiliza al agregar o actualizar algun producto.
class Ui_ClaveInexistenteProveedor(object):
    def setupUi(self, ClaveInexistenteProveedor):
        ClaveInexistenteProveedor.setObjectName("ClaveInexistenteProveedor")
        ClaveInexistenteProveedor.resize(284, 107)
        ClaveInexistenteProveedor.setStyleSheet("background-color: rgb(226, 230, 255);")
        self.centralwidget = QtWidgets.QWidget(ClaveInexistenteProveedor)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 251, 71))
        self.label.setObjectName("label")
        ClaveInexistenteProveedor.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ClaveInexistenteProveedor)
        self.statusbar.setObjectName("statusbar")
        ClaveInexistenteProveedor.setStatusBar(self.statusbar)

        self.retranslateUi(ClaveInexistenteProveedor)
        QtCore.QMetaObject.connectSlotsByName(ClaveInexistenteProveedor)

    #MENSAJE ASIGNADO EN EL LABEL.
    def retranslateUi(self, ClaveInexistenteProveedor):
        _translate = QtCore.QCoreApplication.translate
        ClaveInexistenteProveedor.setWindowTitle(_translate("ClaveInexistenteProveedor", "MainWindow"))
        self.label.setText(_translate("ClaveInexistenteProveedor", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">CLAVE DE PROVEEDOR</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">INEXISTENTE</span></p></body></html>"))

#PERMITE QUE LA APLICACIÓN SE CIERRE.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClaveInexistenteProveedor = QtWidgets.QMainWindow()
    ui = Ui_ClaveInexistenteProveedor()
    ui.setupUi(ClaveInexistenteProveedor)
    ClaveInexistenteProveedor.show()
    sys.exit(app.exec_())
