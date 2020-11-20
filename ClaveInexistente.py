#Librería utilizada para crear la aplicación/ventana.
from PyQt5 import QtCore, QtGui, QtWidgets

#Donde se crea la aplicación (Ventana que avisa que la clave a utilizar esta disponible, por lo tanto se puede proseguir)
class Ui_ClaveInexistente(object):
    def setupUi(self, ClaveInexistente):
        ClaveInexistente.setObjectName("ClaveInexistente")
        ClaveInexistente.resize(284, 107)
        ClaveInexistente.setStyleSheet("background-color: rgb(226, 230, 255);")
        self.centralwidget = QtWidgets.QWidget(ClaveInexistente)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 251, 71))
        self.label.setObjectName("label")
        ClaveInexistente.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ClaveInexistente)
        self.statusbar.setObjectName("statusbar")
        ClaveInexistente.setStatusBar(self.statusbar)

        self.retranslateUi(ClaveInexistente)
        QtCore.QMetaObject.connectSlotsByName(ClaveInexistente)

    #MENSAJE ASIGNADO EN EL LABEL.
    def retranslateUi(self, ClaveInexistente):
        _translate = QtCore.QCoreApplication.translate
        ClaveInexistente.setWindowTitle(_translate("ClaveInexistente", "MainWindow"))
        self.label.setText(_translate("ClaveInexistente", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">CLAVE DISPONIBLE,</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">PROSIGA</span></p></body></html>"))


#PERMITE QUE LA APLICACIÓN SE CIERRE.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClaveInexistente = QtWidgets.QMainWindow()
    ui = Ui_ClaveInexistente()
    ui.setupUi(ClaveInexistente)
    ClaveInexistente.show()
    sys.exit(app.exec_())
