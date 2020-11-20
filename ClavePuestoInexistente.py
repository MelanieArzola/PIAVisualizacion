#Librería utilizada para crear la aplicación/ventana.
from PyQt5 import QtCore, QtGui, QtWidgets

#Donde se crea la aplicación (Ventana que avisa que la clave de puesto NO existe, por lo tanto se debe de poner otro)
#Se utiliza al actualizar o agregar un trabajador.
class Ui_ClaveInexistentePuesto(object):
    def setupUi(self, ClaveInexistentePuesto):
        ClaveInexistentePuesto.setObjectName("ClaveInexistentePuesto")
        ClaveInexistentePuesto.resize(284, 107)
        ClaveInexistentePuesto.setStyleSheet("background-color: rgb(226, 230, 255);")
        self.centralwidget = QtWidgets.QWidget(ClaveInexistentePuesto)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 251, 71))
        self.label.setObjectName("label")
        ClaveInexistentePuesto.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ClaveInexistentePuesto)
        self.statusbar.setObjectName("statusbar")
        ClaveInexistentePuesto.setStatusBar(self.statusbar)

        self.retranslateUi(ClaveInexistentePuesto)
        QtCore.QMetaObject.connectSlotsByName(ClaveInexistentePuesto)

    #MENSAJE ASIGNADO EN EL LABEL.
    def retranslateUi(self, ClaveInexistentePuesto):
        _translate = QtCore.QCoreApplication.translate
        ClaveInexistentePuesto.setWindowTitle(_translate("ClaveInexistentePuesto", "MainWindow"))
        self.label.setText(_translate("ClaveInexistentePuesto", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">CLAVE DE PUESTO</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">INEXISTENTE</span></p></body></html>"))

#PERMITE QUE LA APLICACIÓN SE CIERRE.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClaveInexistentePuesto = QtWidgets.QMainWindow()
    ui = Ui_ClaveInexistentePuesto()
    ui.setupUi(ClaveInexistentePuesto)
    ClaveInexistentePuesto.show()
    sys.exit(app.exec_())
