#Librería utilizada para crear la aplicación/ventana.
from PyQt5 import QtCore, QtGui, QtWidgets

#Donde se crea la aplicación (Ventana que avisa que los datos se actualizaron exitosamente.)
class Ui_DatosActualizados(object):
    def setupUi(self, DatosActualizados):
        DatosActualizados.setObjectName("DatosActualizados")
        DatosActualizados.resize(284, 107)
        DatosActualizados.setStyleSheet("background-color: rgb(226, 230, 255);")
        self.centralwidget = QtWidgets.QWidget(DatosActualizados)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 251, 71))
        self.label.setObjectName("label")
        DatosActualizados.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DatosActualizados)
        self.statusbar.setObjectName("statusbar")
        DatosActualizados.setStatusBar(self.statusbar)

        self.retranslateUi(DatosActualizados)
        QtCore.QMetaObject.connectSlotsByName(DatosActualizados)

    #MENSAJE ASIGNADO EN EL LABEL.
    def retranslateUi(self, DatosActualizados):
        _translate = QtCore.QCoreApplication.translate
        DatosActualizados.setWindowTitle(_translate("DatosActualizados", "MainWindow"))
        self.label.setText(_translate("DatosActualizados", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">DATOS ACTUALIZADOS</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">EXITOSAMENTE</span></p></body></html>"))

#PERMITE QUE LA APLICACIÓN SE CIERRE.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DatosActualizados = QtWidgets.QMainWindow()
    ui = Ui_DatosActualizados()
    ui.setupUi(DatosActualizados)
    DatosActualizados.show()
    sys.exit(app.exec_())
