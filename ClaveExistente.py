#Librería utilizada para crear la aplicación/ventana.
from PyQt5 import QtCore, QtGui, QtWidgets

#Donde se crea la aplicación (Ventana que avisa que la clave a utilizar esta ocupada, por lo tanto se tiene que elegir otra)
class Ui_ClaveExistente(object):
    def setupUi(self, ClaveExistente):
        ClaveExistente.setObjectName("ClaveExistente")
        ClaveExistente.resize(284, 107)
        ClaveExistente.setStyleSheet("background-color: rgb(226, 230, 255);")
        self.centralwidget = QtWidgets.QWidget(ClaveExistente)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 251, 71))
        self.label.setObjectName("label")
        ClaveExistente.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ClaveExistente)
        self.statusbar.setObjectName("statusbar")
        ClaveExistente.setStatusBar(self.statusbar)

        self.retranslateUi(ClaveExistente)
        QtCore.QMetaObject.connectSlotsByName(ClaveExistente)

    #MENSAJE ASIGNADO EN EL LABEL.
    def retranslateUi(self, ClaveExistente):
        _translate = QtCore.QCoreApplication.translate
        ClaveExistente.setWindowTitle(_translate("ClaveExistente", "MainWindow"))
        self.label.setText(_translate("ClaveExistente", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">CLAVE OCUPADA</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">INTENTE CON OTRA</span></p></body></html>"))

#PERMITE QUE LA APLICACIÓN SE CIERRE.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClaveExistente = QtWidgets.QMainWindow()
    ui = Ui_ClaveExistente()
    ui.setupUi(ClaveExistente)
    ClaveExistente.show()
    sys.exit(app.exec_())
