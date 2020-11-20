#Importación de ventanas para conectar en las funciones.
from NuevoCliente import Ui_NuevoCliente
from EliminarCliente import Ui_EliminarClientes
from ActualizarCliente import Ui_ActualizarCliente
#Importación de sql para establecer la conexión y excepciones.
import sqlite3
from sqlite3 import Error
#Librería para crear nuestra aplicación.
from PyQt5 import QtCore, QtGui, QtWidgets

#Creación de la aplicación. (Menú de clientes donde se permite consultar, agregar, eliminar y actualizar información.)
class Ui_Clientes(object):
    def setupUi(self, Clientes):
        Clientes.setObjectName("Clientes")
        Clientes.resize(502, 329)
        Clientes.setStyleSheet("background-color: rgb(226, 230, 255);")
        self.centralwidget = QtWidgets.QWidget(Clientes)
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
        Clientes.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Clientes)
        self.statusbar.setObjectName("statusbar")
        Clientes.setStatusBar(self.statusbar)

        self.retranslateUi(Clientes)
        QtCore.QMetaObject.connectSlotsByName(Clientes)
        #PROGRAMACIÓN DE BOTONES PARA CONECTAR A LAS FUNCIONES
        
        #Permite limpiar la tabla para agregar datos actualizados.
        self.BConsultaP.clicked.connect(self.tableWidget.clearContents)
        #Conecta a la función de consultar toda la información guardada en clientes.
        self.BConsultaP.clicked.connect(self.ConsultaClientes)
        #Conecta a la función para agregar nuevo cliente.
        self.BAgregarP.clicked.connect(self.AgregarClientes)
        #Conecta a la función para eliminar un cliente.
        self.BEliminarP.clicked.connect(self.EliminarClientes)
        #Conecta a la función que permite actualizar un cliente.
        self.BActualizarP.clicked.connect(self.ActualizarClientes)

    #Función que permite consultar lo que esta dentro de la tabla cliente.
    def ConsultaClientes(self):
        #Try para excepciones.
        try:
            #Establecer conexión con la base de datos.
            with sqlite3.connect("PIA_1845788.db") as conn:
                #Establecer el cursor.
                micursor = conn.cursor()
                #Seleccionar todo de la tabla Cliente.
                micursor.execute("SELECT * FROM Cliente")
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
    
    #Conexión a la ventana de agregar cliente(codigo en .py)
    def AgregarClientes(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_NuevoCliente()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
    
    #Conexión a la ventana de eliminar cliente(codigo en .py)
    def EliminarClientes(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_EliminarClientes()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
    
    #Conexión a la ventana de actualizar cliente (codigo en .py)
    def ActualizarClientes(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_ActualizarCliente()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    #Asignación de texto a los botones.
    def retranslateUi(self, Clientes):
        _translate = QtCore.QCoreApplication.translate
        Clientes.setWindowTitle(_translate("Clientes", "MainWindow"))
        self.label_2.setText(_translate("Clientes", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">CLIENTES</span></p></body></html>"))
        self.BConsultaP.setText(_translate("Clientes", "CONSULTAR"))
        self.BAgregarP.setText(_translate("Clientes", "AGREGAR"))
        self.BEliminarP.setText(_translate("Clientes", "ELIMINAR"))
        self.BActualizarP.setText(_translate("Clientes", "ACTUALIZAR"))

#Cerrar aplicación.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Clientes = QtWidgets.QMainWindow()
    ui = Ui_Clientes()
    ui.setupUi(Clientes)
    Clientes.show()
    sys.exit(app.exec_())
