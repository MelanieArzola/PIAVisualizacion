#Librería utilizada para crear la aplicación/ventana.
from PyQt5 import QtCore, QtGui, QtWidgets

#Donde se crea la aplicación (Ventana que avisa que los datos se eliminaron exitosamente.)
class Ui_DatosEliminados(object):
    def setupUi(self, DatosEliminados):
        DatosEliminados.setObjectName("DatosEliminados")
        DatosEliminados.resize(284, 105)
        DatosEliminados.setStyleSheet("background-color: rgb(226, 230, 255);")
        self.centralwidget = QtWidgets.QWidget(DatosEliminados)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 251, 71))
        self.label.setObjectName("label")
        DatosEliminados.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DatosEliminados)
        self.statusbar.setObjectName("statusbar")
        DatosEliminados.setStatusBar(self.statusbar)

        self.retranslateUi(DatosEliminados)
        QtCore.QMetaObject.connectSlotsByName(DatosEliminados)

    #MENSAJE ASIGNADO EN EL LABEL.
    def retranslateUi(self, DatosEliminados):
        _translate = QtCore.QCoreApplication.translate
        DatosEliminados.setWindowTitle(_translate("DatosEliminados", "MainWindow"))
        self.label.setText(_translate("DatosEliminados", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">DATOS ELIMINADOS</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">EXITOSAMENTE</span></p></body></html>"))

#PERMITE QUE LA APLICACIÓN SE CIERRE.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DatosEliminados = QtWidgets.QMainWindow()
    ui = Ui_DatosEliminados()
    ui.setupUi(DatosEliminados)
    DatosEliminados.show()
    sys.exit(app.exec_())
