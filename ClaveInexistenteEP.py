#Librería utilizada para crear la aplicación/ventana.
from PyQt5 import QtCore, QtGui, QtWidgets

#Donde se crea la aplicación (Ventana que avisa que la clave a utilizar no existe, por lo tanto se tiene que elegir otra)
#Se utiliza al eliminar algun dato.
class Ui_ClaveInexistenteEP(object):
    def setupUi(self, ClaveInexistenteEP):
        ClaveInexistenteEP.setObjectName("ClaveInexistenteEP")
        ClaveInexistenteEP.resize(284, 107)
        ClaveInexistenteEP.setStyleSheet("background-color: rgb(226, 230, 255);")
        self.centralwidget = QtWidgets.QWidget(ClaveInexistenteEP)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 251, 71))
        self.label.setObjectName("label")
        ClaveInexistenteEP.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ClaveInexistenteEP)
        self.statusbar.setObjectName("statusbar")
        ClaveInexistenteEP.setStatusBar(self.statusbar)

        self.retranslateUi(ClaveInexistenteEP)
        QtCore.QMetaObject.connectSlotsByName(ClaveInexistenteEP)

    #MENSAJE ASIGNADO EN EL LABEL.
    def retranslateUi(self, ClaveInexistenteEP):
        _translate = QtCore.QCoreApplication.translate
        ClaveInexistenteEP.setWindowTitle(_translate("ClaveInexistenteEP", "MainWindow"))
        self.label.setText(_translate("ClaveInexistenteEP", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">CLAVE INEXISTENTE,</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">INTENTE CON OTRA</span></p></body></html>"))

#PERMITE QUE LA APLICACIÓN SE CIERRE.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClaveInexistenteEP = QtWidgets.QMainWindow()
    ui = Ui_ClaveInexistenteEP()
    ui.setupUi(ClaveInexistenteEP)
    ClaveInexistenteEP.show()
    sys.exit(app.exec_())
