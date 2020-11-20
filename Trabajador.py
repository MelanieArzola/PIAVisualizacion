#Librería para crear nuestra aplicación.
from PyQt5 import QtCore, QtGui, QtWidgets
#Importación de ventanas para conectar en las funciones.
from NuevoTrabajador import Ui_NuevoTrabajador
from EliminarTrabajador import Ui_EliminarTrabajador
from ActualizarTrabajador import Ui_ActualizarTrabajador
#Importación de sql para establecer la conexión y excepciones.
import sqlite3
from sqlite3 import Error

#Creación de la aplicación. (Menú de trabjadores donde se permite consultar, agregar, eliminar y actualizar información.)
class Ui_Trabajadores(object):
    def setupUi(self, Trabajadores):
        Trabajadores.setObjectName("Trabajadores")
        Trabajadores.resize(502, 329)
        Trabajadores.setStyleSheet("background-color: rgb(226, 230, 255);")
        self.centralwidget = QtWidgets.QWidget(Trabajadores)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 501, 31))
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 481, 192))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(10)
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
        Trabajadores.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Trabajadores)
        self.statusbar.setObjectName("statusbar")
        Trabajadores.setStatusBar(self.statusbar)

        self.retranslateUi(Trabajadores)
        QtCore.QMetaObject.connectSlotsByName(Trabajadores)
        #PROGRAMACIÓN DE BOTONES PARA CONECTAR A LAS FUNCIONES
        
        #Permite limpiar la tabla para agregar datos actualizados.
        self.BConsultaP.clicked.connect(self.tableWidget.clearContents)
        #Conecta a la función que permite consultar toda la información guardada en la tabla trabajador.
        self.BConsultaP.clicked.connect(self.ConsultaTrabajador)
        #Conecta a la función que permite agregar un trabajador.
        self.BAgregarP.clicked.connect(self.AgregarTrabajador)
        #Conecta a la función que permite eliminar un trabajador.
        self.BEliminarP.clicked.connect(self.EliminarTrabajador)
        #Conecta a la función que permite actualizar un trabajador.
        self.BActualizarP.clicked.connect(self.ActualizarTrabajador)

    #Función que permite consultar lo que esta dentro de la tabla trabajador
    def ConsultaTrabajador(self):
        #Try para excepciones.
        try:
            #Establecer conexión con la base de datos.
            with sqlite3.connect("PIA_1845788.db") as conn:
                #Establecer el cursor.
                micursor = conn.cursor()
                #Seleccionar toda la información de la tabla trabajador junto con el nombre de puesto que le pertenece.
                micursor.execute("SELECT t.Clave_Trabajador,t.Nombre, t.ApellidoPaterno, t.ApellidoMaterno, t.Fecha_Ingreso, t.Telefono, t.Usuario, t.Contraseña, p.Clave,p.Nombre FROM Trabajador t INNER JOIN Puesto p ON t.Puesto = p.Clave")
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
    
    #Conexión a la ventana de agregarr trabajador (codigo en .py)
    def AgregarTrabajador(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_NuevoTrabajador()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
    
    #Conexión a la ventana de eliminar trabajador (codigo en .py)
    def EliminarTrabajador(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_EliminarTrabajador()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
    
    #Conexión a la ventana de actualizar trabajador (codigo en .py)
    def ActualizarTrabajador(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_ActualizarTrabajador()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    #Asignación de texto a los botones.
    def retranslateUi(self, Trabajadores):
        _translate = QtCore.QCoreApplication.translate
        Trabajadores.setWindowTitle(_translate("Trabajadores", "MainWindow"))
        self.label_2.setText(_translate("Trabajadores", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">TRABAJADORES</span></p></body></html>"))
        self.BConsultaP.setText(_translate("Trabajadores", "CONSULTAR"))
        self.BAgregarP.setText(_translate("Trabajadores", "AGREGAR"))
        self.BEliminarP.setText(_translate("Trabajadores", "ELIMINAR"))
        self.BActualizarP.setText(_translate("Trabajadores", "ACTUALIZAR"))

#Cerrar aplicación.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Trabajadores = QtWidgets.QMainWindow()
    ui = Ui_Trabajadores()
    ui.setupUi(Trabajadores)
    Trabajadores.show()
    sys.exit(app.exec_())
