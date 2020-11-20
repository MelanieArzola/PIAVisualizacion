#Librería utilizada para crear la aplicación/ventana.
from PyQt5 import QtCore, QtGui, QtWidgets

#Donde se crea la aplicación (Ventana que avisa que los datos se agregaron exitosamente.)
class Ui_DatosAgregados(object):
    def setupUi(self, DatosAgregados):
        DatosAgregados.setObjectName("DatosAgregados")
        DatosAgregados.resize(284, 107)
        DatosAgregados.setStyleSheet("background-color: rgb(226, 230, 255);")
        self.centralwidget = QtWidgets.QWidget(DatosAgregados)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 251, 71))
        self.label.setObjectName("label")
        DatosAgregados.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DatosAgregados)
        self.statusbar.setObjectName("statusbar")
        DatosAgregados.setStatusBar(self.statusbar)

        self.retranslateUi(DatosAgregados)
        QtCore.QMetaObject.connectSlotsByName(DatosAgregados)
    
    #MENSAJE ASIGNADO EN EL LABEL.
    def retranslateUi(self, DatosAgregados):
        _translate = QtCore.QCoreApplication.translate
        DatosAgregados.setWindowTitle(_translate("DatosAgregados", "MainWindow"))
        self.label.setText(_translate("DatosAgregados", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">DATOS AGREGADOS</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">EXITOSAMENTE</span></p></body></html>"))

#PERMITE QUE LA APLICACIÓN SE CIERRE.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DatosAgregados = QtWidgets.QMainWindow()
    ui = Ui_DatosAgregados()
    ui.setupUi(DatosAgregados)
    DatosAgregados.show()
    sys.exit(app.exec_())
