#Librería para crear nuestra aplicación.
from PyQt5 import QtCore, QtGui, QtWidgets

#Creación de ventana que se utiliza para recordar todos los campos correctamente.
class Ui_Alerta(object):
    def setupUi(self, Alerta):
        Alerta.setObjectName("Alerta")
        Alerta.resize(284, 145)
        Alerta.setStyleSheet("background-color: rgb(226, 230, 255);")
        self.centralwidget = QtWidgets.QWidget(Alerta)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 20, 281, 101))
        self.label.setObjectName("label")
        Alerta.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Alerta)
        self.statusbar.setObjectName("statusbar")
        Alerta.setStatusBar(self.statusbar)

        self.retranslateUi(Alerta)
        QtCore.QMetaObject.connectSlotsByName(Alerta)

    def retranslateUi(self, Alerta):
        _translate = QtCore.QCoreApplication.translate
        Alerta.setWindowTitle(_translate("Alerta", "MainWindow"))
        self.label.setText(_translate("Alerta", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">FAVOR DE LLENAR</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">TODOS LOS CAMPOS</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">CORRECTAMENTE</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Alerta = QtWidgets.QMainWindow()
    ui = Ui_Alerta()
    ui.setupUi(Alerta)
    Alerta.show()
    sys.exit(app.exec_())
