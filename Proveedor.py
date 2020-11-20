#Librería para crear nuestra aplicación.
from PyQt5 import QtCore, QtGui, QtWidgets
#Importación de ventanas para conectar en las funciones.
from NuevoProveedor import Ui_MenuNP
from EliminarProveedor import Ui_MenuEP
from ActualizarProveedor import Ui_ActualizarProveedor
#Importación de sql para establecer la conexión y excepciones.
import sqlite3
from sqlite3 import Error

#Creación de la aplicación. (Menú de proveedores donde se permite consultar, agregar, eliminar y actualizar información.)
class Ui_Proveedores(object):
    def setupUi(self, Proveedores):
        Proveedores.setObjectName("Proveedores")
        Proveedores.resize(502, 329)
        Proveedores.setStyleSheet("background-color: rgb(226, 230, 255);")
        self.centralwidget = QtWidgets.QWidget(Proveedores)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 501, 31))
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 481, 192))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setRowCount(15)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.BConsultaP = QtWidgets.QPushButton(self.centralwidget)
        self.BConsultaP.setGeometry(QtCore.QRect(50, 270, 75, 23))
        self.BConsultaP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BConsultaP.setObjectName("BConsultaP")
        self.BAgregarP = QtWidgets.QPushButton(self.centralwidget)
        self.BAgregarP.setGeometry(QtCore.QRect(270, 270, 75, 23))
        self.BAgregarP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BAgregarP.setObjectName("BAgregarP")
        self.BEliminarP = QtWidgets.QPushButton(self.centralwidget)
        self.BEliminarP.setGeometry(QtCore.QRect(380, 270, 75, 23))
        self.BEliminarP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BEliminarP.setObjectName("BEliminarP")
        self.BActualizarP = QtWidgets.QPushButton(self.centralwidget)
        self.BActualizarP.setGeometry(QtCore.QRect(160, 270, 75, 23))
        self.BActualizarP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BActualizarP.setObjectName("BActualizarP")
        Proveedores.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Proveedores)
        self.statusbar.setObjectName("statusbar")
        Proveedores.setStatusBar(self.statusbar)

        self.retranslateUi(Proveedores)
        QtCore.QMetaObject.connectSlotsByName(Proveedores)
        #PROGRAMACIÓN DE BOTONES PARA CONECTAR A LAS FUNCIONES
        
        #Permite limpiar la tabla para agregar datos actualizados.
        self.BConsultaP.clicked.connect(self.tableWidget.clearContents)
        #Conecta a la función de consultar toda la información guardada en proveedores.
        self.BConsultaP.clicked.connect(self.ConsultaP)
        #Conecta a la función para agregar nuevo proveedor.
        self.BAgregarP.clicked.connect(self.AgregarP)
        #Conecta a la función para eliminar un proveedor.
        self.BEliminarP.clicked.connect(self.EliminarP)
        #Conecta a la función que permite actualizar un proveedor.
        self.BActualizarP.clicked.connect(self.ActualizarP)

    #Función que permite consultar lo que esta dentro de la tabla proveedor.
    def ConsultaP(self):
        #Try para excepciones. 
        try:
            #Establecer conexión con la base de datos.
            with sqlite3.connect("PIA_1845788.db") as conn:
                #Establecer el cursor.
                micursor = conn.cursor()
                #Seleccionar todo de la tabla Proveedor.
                micursor.execute("SELECT * FROM Proveedor")
                #Guardar lo que se busco en la variable.
                PB1 = micursor.fetchall()
                #Pasar la información de la variable a la tabla.
                for row_number, row_data in enumerate(PB1):
                    self.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        #Excepción con error de sqlite3.
        except Error as e:
            print(e)
    
    #Conexión a la ventana de agregar proveedor(codigo en .py)
    def AgregarP(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_MenuNP()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
    
    #Conexión a la ventana de eliminar proveedor (codigo en .py)
    def EliminarP(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_MenuEP()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
    
    #Conexión a la ventana de actualizar proveedor (codigo en .py)
    def ActualizarP(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_ActualizarProveedor()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    #Asignación de texto a los botones.
    def retranslateUi(self, Proveedores):
        _translate = QtCore.QCoreApplication.translate
        Proveedores.setWindowTitle(_translate("Proveedores", "MainWindow"))
        self.label_2.setText(_translate("Proveedores", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">PROVEEDORES</span></p></body></html>"))
        self.BConsultaP.setText(_translate("Proveedores", "CONSULTAR"))
        self.BAgregarP.setText(_translate("Proveedores", "AGREGAR"))
        self.BEliminarP.setText(_translate("Proveedores", "ELIMINAR"))
        self.BActualizarP.setText(_translate("Proveedores", "ACTUALIZAR"))

#Cerrar aplicación.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Proveedores = QtWidgets.QMainWindow()
    ui = Ui_Proveedores()
    ui.setupUi(Proveedores)
    Proveedores.show()
    sys.exit(app.exec_())
