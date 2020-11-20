#Librería utilizada para crear la aplicación/ventana.
from PyQt5 import QtCore, QtGui, QtWidgets

#Donde se crea la aplicación (Ventana que avisa que la clave a utilizar no existe, por lo tanto se tiene que elegir otra)
#Se utiliza al actualizar algun dato.
class Ui_ClaveInexistenteUP(object):
    def setupUi(self, ClaveInexistenteUP):
        ClaveInexistenteUP.setObjectName("ClaveInexistenteUP")
        ClaveInexistenteUP.resize(284, 107)
        ClaveInexistenteUP.setStyleSheet("background-color: rgb(226, 230, 255);")
        self.centralwidget = QtWidgets.QWidget(ClaveInexistenteUP)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 271, 71))
        self.label.setObjectName("label")
        ClaveInexistenteUP.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ClaveInexistenteUP)
        self.statusbar.setObjectName("statusbar")
        ClaveInexistenteUP.setStatusBar(self.statusbar)

        self.retranslateUi(ClaveInexistenteUP)
        QtCore.QMetaObject.connectSlotsByName(ClaveInexistenteUP)

    #MENSAJE ASIGNADO EN EL LABEL.
    def retranslateUi(self, ClaveInexistenteUP):
        _translate = QtCore.QCoreApplication.translate
        ClaveInexistenteUP.setWindowTitle(_translate("ClaveInexistenteUP", "MainWindow"))
        self.label.setText(_translate("ClaveInexistenteUP", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">CLAVE INEXISTENTE</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">NO SE PUEDE ACTUALIZAR</span></p></body></html>"))

#PERMITE QUE LA APLICACIÓN SE CIERRE.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClaveInexistenteUP = QtWidgets.QMainWindow()
    ui = Ui_ClaveInexistenteUP()
    ui.setupUi(ClaveInexistenteUP)
    ClaveInexistenteUP.show()
    sys.exit(app.exec_())
