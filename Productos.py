#Importar librerías para utilizarlas en la gráfica.
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
#Librería para crear nuestra aplicación.
from PyQt5 import QtCore, QtGui, QtWidgets
#Importación de ventanas para conectar en las funciones.
from NuevoProducto import Ui_AgregarProducto
from EliminarProducto import Ui_EliminarProducto
from ActualizarProducto import Ui_ActualizarProducto
#Importación de sql para establecer la conexión y excepciones.
import sqlite3
from sqlite3 import Error


#Creación de la aplicación. (Menú de productos donde se permite consultar, agregar, eliminar y actualizar información.)
class Ui_Productos(object):
    def setupUi(self, Productos):
        Productos.setObjectName("Productos")
        Productos.resize(534, 329)
        Productos.setStyleSheet("background-color: rgb(226, 230, 255);")
        self.centralwidget = QtWidgets.QWidget(Productos)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 531, 31))
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 520, 192))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setObjectName("tableWidget")
        self.BConsultaP = QtWidgets.QPushButton(self.centralwidget)
        self.BConsultaP.setGeometry(QtCore.QRect(10, 270, 75, 23))
        self.BConsultaP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BConsultaP.setObjectName("BConsultaP")
        self.BAgregarP = QtWidgets.QPushButton(self.centralwidget)
        self.BAgregarP.setGeometry(QtCore.QRect(230, 270, 75, 23))
        self.BAgregarP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BAgregarP.setObjectName("BAgregarP")
        self.BEliminarP = QtWidgets.QPushButton(self.centralwidget)
        self.BEliminarP.setGeometry(QtCore.QRect(340, 270, 75, 23))
        self.BEliminarP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BEliminarP.setObjectName("BEliminarP")
        self.BActualizarP = QtWidgets.QPushButton(self.centralwidget)
        self.BActualizarP.setGeometry(QtCore.QRect(120, 270, 75, 23))
        self.BActualizarP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BActualizarP.setObjectName("BActualizarP")
        self.BGraficaP = QtWidgets.QPushButton(self.centralwidget)
        self.BGraficaP.setGeometry(QtCore.QRect(450, 270, 75, 23))
        self.BGraficaP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BGraficaP.setObjectName("BGraficaP")
        Productos.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Productos)
        self.statusbar.setObjectName("statusbar")
        Productos.setStatusBar(self.statusbar)

        self.retranslateUi(Productos)
        QtCore.QMetaObject.connectSlotsByName(Productos)
        #PROGRAMACIÓN DE BOTONES PARA CONECTAR A LAS FUNCIONES
        
        #Permite limpiar la tabla para agregar datos actualizados.
        self.BConsultaP.clicked.connect(self.tableWidget.clearContents)
        #Conecta a la función de consultar toda la información guardada.
        self.BConsultaP.clicked.connect(self.ConsultaProducto)
        #Conecta a la función donde se gráfica los productos y con su inventario.
        self.BGraficaP.clicked.connect(self.Grafica)
        #Conecta a la función para agregar nuevo producto.
        self.BAgregarP.clicked.connect(self.AgregarProducto)
        #Conecta a la función para eliminar un producto.
        self.BEliminarP.clicked.connect(self.EliminarProducto)
        #Conecta a la función que permite actualizar un producto.
        self.BActualizarP.clicked.connect(self.ActualizarProducto)
    
    #Función para gráficar.
    def Grafica(self):
        #Try para excepciones. 
        try:
            #Conexión a la base de datos
            with sqlite3.connect("PIA_1845788.db") as conn:
                #Definición del cursor para obtener la información.
                micursor = conn.cursor()
                #Buscar los nombres de productos guardados.
                micursor.execute("SELECT Nombre FROM Producto")
                listaProductos = []
                nombreP = micursor.fetchall()
                #Ciclo para obtener solo el dato y agregarlo a una nueva lista que se utilizara paara la gráfica.
                for dato in nombreP:
                    for n in dato:
                        nombre= str(n)
                        listaProductos.append(nombre)
                #Obtener la cantidad de cada producto anteriormente obtenido de la base de datos.
                micursor.execute("SELECT Inventario FROM Producto")
                listaInventario = []
                inventarioP = micursor.fetchall()
                #Sacarlo de la tupla que esta dentro de lista, y agregarlos a una lista final la cual utilizaremos para el gráfico.
                for dato in inventarioP:
                    for n in dato:
                        inventario= int(n)
                        listaInventario.append(inventario)
                #Añadir etiquetas a la gráfica
                fid, ax = plt.subplots()
                #Etiqueta eje Y
                ax.set_ylabel("Inventario")
                #Etiqueta eje X
                ax.set_xlabel("Productos")
                #Titulo gráfica
                ax.set_title("Cantidad de productos en inventario")
                #Creación de la gráfica (x,y) = (productos,inventario)
                plt.bar(listaProductos,listaInventario)
                plt.savefig('barras_simples.png')
                #Mostramos la gráfica
                plt.show()
        #Excepción que muestra si hay un error con la base de datos.
        except Error as e:
            print(e)
   
    #Función que permite consultar lo que esta dentro de la tabla producto.
    def ConsultaProducto(self):
        #Try para excepciones. 
         try:
             #Establecer conexión con la base de datos.
             with sqlite3.connect("PIA_1845788.db") as conn:
                #Establecer el cursor.
                micursor = conn.cursor()
                #Seleccionar la clave, nombre, precio, cantidad en inventario del producto, la clave de proveedor y el nombre del proveedor del cual depende.
                micursor.execute("SELECT p.Clave_Producto,p.Nombre, p.Precio, p.Inventario, pro.Clave_Proveedor, pro.Nombre FROM Producto p INNER JOIN Proveedor pro ON p.Clave_Proveedor = pro.Clave_Proveedor")
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
    
    #Conexión a la ventana de agregar producto (codigo en .py)
    def AgregarProducto(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_AgregarProducto()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
    
    #Conexión a la ventana de eliminar producto (codigo en .py)
    def EliminarProducto(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_EliminarProducto()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
    
    #Conexión a la ventana de actualizar producto (codigo en .py)
    def ActualizarProducto(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_ActualizarProducto()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    #Asignación de texto a los botones.
    def retranslateUi(self, Productos):
        _translate = QtCore.QCoreApplication.translate
        Productos.setWindowTitle(_translate("Productos", "MainWindow"))
        self.label_2.setText(_translate("Productos", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">PRODUCTOS</span></p></body></html>"))
        self.BConsultaP.setText(_translate("Productos", "CONSULTAR"))
        self.BAgregarP.setText(_translate("Productos", "AGREGAR"))
        self.BEliminarP.setText(_translate("Productos", "ELIMINAR"))
        self.BActualizarP.setText(_translate("Productos", "ACTUALIZAR"))
        self.BGraficaP.setText(_translate("Productos", "GRAFICA"))

#Cerrar aplicación.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Productos = QtWidgets.QMainWindow()
    ui = Ui_Productos()
    ui.setupUi(Productos)
    Productos.show()
    sys.exit(app.exec_())
