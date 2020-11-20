#Librería para crear nuestra aplicación.
from PyQt5 import QtCore, QtGui, QtWidgets
#Importación de sql para establecer la conexión y excepciones.
import sqlite3
from sqlite3 import Error
#Importación de ventanas para conectar en las funciones.
from DatosEliminados import Ui_DatosEliminados
from ClaveInexistenteEP import Ui_ClaveInexistenteEP
from Alerta import Ui_Alerta

#Creación de la aplicación. (Menú de productos donde se introduce la clave a eliminar.)
class Ui_EliminarProducto(object):
    def setupUi(self, EliminarProducto):
        EliminarProducto.setObjectName("EliminarProducto")
        EliminarProducto.resize(311, 344)
        EliminarProducto.setStyleSheet("background-color: rgb(226, 230, 255);")
        self.centralwidget = QtWidgets.QWidget(EliminarProducto)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 301, 51))
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 69, 91, 21))
        self.label.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 230, 81, 16))
        self.label_4.setObjectName("label_4")
        self.Nombre = QtWidgets.QTextBrowser(self.centralwidget)
        self.Nombre.setGeometry(QtCore.QRect(120, 100, 161, 31))
        self.Nombre.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.Nombre.setObjectName("Nombre")
        self.Proveedor = QtWidgets.QTextBrowser(self.centralwidget)
        self.Proveedor.setGeometry(QtCore.QRect(120, 220, 161, 31))
        self.Proveedor.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.Proveedor.setObjectName("Proveedor")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 190, 81, 16))
        self.label_8.setObjectName("label_8")
        self.Inventario = QtWidgets.QTextBrowser(self.centralwidget)
        self.Inventario.setGeometry(QtCore.QRect(120, 180, 161, 31))
        self.Inventario.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.Inventario.setObjectName("Inventario")
        self.Precio = QtWidgets.QTextBrowser(self.centralwidget)
        self.Precio.setGeometry(QtCore.QRect(120, 140, 161, 31))
        self.Precio.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.Precio.setObjectName("Precio")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 61, 16))
        self.label_3.setObjectName("label_3")
        self.ClaveP = QtWidgets.QLineEdit(self.centralwidget)
        self.ClaveP.setGeometry(QtCore.QRect(120, 60, 161, 31))
        self.ClaveP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ClaveP.setObjectName("ClaveP")
        self.Eliminar = QtWidgets.QPushButton(self.centralwidget)
        self.Eliminar.setGeometry(QtCore.QRect(220, 270, 75, 23))
        self.Eliminar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Eliminar.setObjectName("Eliminar")
        self.Limpiar = QtWidgets.QPushButton(self.centralwidget)
        self.Limpiar.setGeometry(QtCore.QRect(20, 270, 75, 23))
        self.Limpiar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Limpiar.setObjectName("Limpiar")
        self.Cargar = QtWidgets.QPushButton(self.centralwidget)
        self.Cargar.setGeometry(QtCore.QRect(120, 270, 75, 23))
        self.Cargar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Cargar.setObjectName("Cargar")
        EliminarProducto.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EliminarProducto)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 311, 21))
        self.menubar.setObjectName("menubar")
        EliminarProducto.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EliminarProducto)
        self.statusbar.setObjectName("statusbar")
        EliminarProducto.setStatusBar(self.statusbar)

        self.retranslateUi(EliminarProducto)
        #Boton Limpiar para limpiar todos los campos.
        self.Limpiar.clicked.connect(self.ClaveP.clear)
        self.Limpiar.clicked.connect(self.Nombre.clear)
        self.Limpiar.clicked.connect(self.Precio.clear)
        self.Limpiar.clicked.connect(self.Inventario.clear)
        self.Limpiar.clicked.connect(self.Proveedor.clear)
        QtCore.QMetaObject.connectSlotsByName(EliminarProducto)
        #Programación de botones
        #Boton que permite cargar la información en la aplicación.
        self.Cargar.clicked.connect(self.ShowData)
        #Boton que permite eliminar la información obtenida de la base de datos.
        self.Eliminar.clicked.connect(self.DeleteData)

    #Función que permite eliminar la información de la base de datos según la clave dada.
    def DeleteData(self):
        #Try para excepciones. 
        try:
            #Conexión a la base de datos
            with sqlite3.connect("PIA_1845788.db") as conn:
                #Leer clave de producto que se introduce en nuestra ventana de Eliminar Producto.
                Clave = self.ClaveP.text()
                #Convertir la clave a entero.
                clave = int(Clave)
                #Definir nuestro cursor.
                mi_cursor = conn.cursor()
                #Ejecutar una línea que nos permite obtener todas las claves guardadas en producto.
                c= mi_cursor.execute("SELECT Clave_Producto FROM Producto")
                #Guardar los resultados en la variable claves.
                claves = mi_cursor.fetchall()
                #Declarar una lista donde se guardaran las claves de productos.
                ClaveP = []
                #Ciclo para el unpack del resultado de claves.
                for dato in claves:
                    for n in dato:
                        CLAVEP = int(n)
                        #Agregar cada clave en la lista ClaveP.
                        ClaveP.append(CLAVEP)        
                #ESTO ES UNA DOBLE VERIFICACIÓN YA QUE TAMBIÉN SE HACE EN LA FUNCIÓN DE VERIFICAR.
                #Si la clave que introdujo el usuario esta dentro de la lista de claves.
                if clave in ClaveP:
                    #Guardar la clave en el diccionario valor, para posteriormente utilizarlo.
                    valor = {"clave":clave}
                    #Ejecutar la linea donde se elimina toda la información guardada con la clave que el usuario otorgo.
                    mi_cursor.execute("DELETE FROM Producto WHERE Clave_Producto= (:clave)",valor)
                    #Ventana que muestra un aviso donde los datos fueron eliminados exitosamente (codigo .py)
                    self.ventana = QtWidgets.QMainWindow()
                    self.ui = Ui_DatosEliminados()
                    self.ui.setupUi(self.ventana)
                    self.ventana.show()
                #Si la clave no se encuentra dentro de la lista:
                else:
                    #Se muestra una ventana que muestra un aviso que la clave que se quiere eliminar no existe (codigo .py)
                    self.ventana = QtWidgets.QMainWindow()
                    self.ui = Ui_ClaveInexistenteEP()
                    self.ui.setupUi(self.ventana)
                    self.ventana.show()
        #Excepcion por si ocurre un error con sqlite3.
        except Error as e:
            print(e)
        #Excepción por si no se llenan los campos necesarios.
        except:
            #Ventana que muestra el mensaje donde se piden llenar todos los campos.
            self.ventana = QtWidgets.QMainWindow()
            self.ui = Ui_Alerta()
            self.ui.setupUi(self.ventana)
            self.ventana.show()
            
    #Función que se utiliza para cargar y mostrar los datos en la aplicación.
    def ShowData(self):
        #Try para excepciones. 
        try:
            #Conexión a la base de datos
            with sqlite3.connect("PIA_1845788.db") as conn:
                #Leer clave de producto que se introduce en nuestra ventana de Eliminar Producto.
                Clave = self.ClaveP.text()
                #Convertir la clave a entero.
                clave = int(Clave)
                #Definir nuestro cursor.
                mi_cursor = conn.cursor()
                #Guardar la clave en el diccionario valor, para posteriormente utilizarlo.
                valor = {"clave":clave}
                #Ejecutar una línea que nos permite obtener todas las claves guardadas en producto.
                c= mi_cursor.execute("SELECT Clave_Producto FROM Producto")
                #Guardar los resultados en la variable claves.
                claves = mi_cursor.fetchall()
                #Declarar una lista donde se guardaran las claves de productos.
                ClaveP = []
                #Ciclo para el unpack del resultado de claves.
                for dato in claves:
                    for n in dato:
                        CLAVEP = int(n)
                        #Agregar cada clave a la lista de Claves.
                        ClaveP.append(CLAVEP)        
                #ESTO ES UNA DOBLE VERIFICACIÓN YA QUE TAMBIÉN SE HACE EN LA FUNCIÓN DE ELIMINAR.
                #Si la clave que introdujo el usuario esta dentro de la lista de claves.
                if clave in ClaveP:      
                    #Buscar nombre del producto en la base de datos según la clave dada por el usuario y mostrarlo.
                    c = mi_cursor.execute("SELECT Nombre FROM Producto WHERE Clave_Producto = (:clave)",valor)
                    #Guardar el resultado en la variable de nombre.
                    nombre = mi_cursor.fetchall()
                    #Ciclo para el unpack del resultado de nombre.
                    for dato in nombre:
                        for n in dato:
                            Nombre = str(n)
                    #Asignar al campo de Nombre el valor de Nombre que se obtuvo anteriormente.
                    self.Nombre.setText(Nombre)
                    
                    #Buscar el precio del producto en la base de datos según la clave dada por el usuario y mostrarlo.
                    c = mi_cursor.execute("SELECT Precio FROM Producto WHERE Clave_Producto = (:clave)",valor)
                    #Guardar el resultado en la variable de Precio.
                    Precio = mi_cursor.fetchall()
                    #Ciclo para el unpack del resultado de Precio.
                    for dato in Precio:
                        for n in dato:
                            precio = str(n)
                    #Asignar al campo de Precio el valor de precio que se obtuvo anteriormente.
                    self.Precio.setText(precio)
                    
                    #Buscar cantidad de productos en inventario en la base de datos según la clave dada por el usuario y mostrarlo.
                    c = mi_cursor.execute("SELECT Inventario FROM Producto WHERE Clave_Producto = (:clave)",valor)
                    #Guardar el resultado en la variable de Inventario.
                    Inventario = mi_cursor.fetchall()
                    #Ciclo para el unpack del resultado de Inventario.
                    for dato in Inventario:
                        for n in dato:
                            inventario = str(n)
                    #Asignar al campo de Inventario el valor de inventario que se obtuvo anteriormente.
                    self.Inventario.setText(inventario)
                    
                    #Buscar nombre del proveedor en la base de datos según la clave de producto dada por el usuario  y mostrarlo
                    c = mi_cursor.execute("SELECT p.Nombre FROM Producto pro INNER JOIN Proveedor p ON pro.Clave_Proveedor = p.Clave_Proveedor WHERE Clave_Producto = (:clave)",valor)
                    #Guardar el resultado en la variable de Proveedor.
                    Proveedor= mi_cursor.fetchall()
                    #Ciclo para el unpack del resultado de Proveedor.
                    for dato in Proveedor:
                        for n in dato:
                            proveedor = str(n)
                    #Asignar al campo de Proveedor el valor de proveedor que se obtuvo anteriormente.
                    self.Proveedor.setText(proveedor)
                #Si la clave no se encuentra dentro de la lista:
                else:
                    #Se muestra una ventana que muestra un aviso que la clave que se quiere eliminar no existe (codigo .py)
                    self.ventana = QtWidgets.QMainWindow()
                    self.ui = Ui_ClaveInexistenteEP()
                    self.ui.setupUi(self.ventana)
                    self.ventana.show()
        #Excepcion por si ocurre un error con sqlite3.
        except Error as e:
            print(e)
        #Excepción por si no se llenan los campos necesarios.
        except:
            #Ventana que muestra el mensaje donde se piden llenar todos los campos.
            self.ventana = QtWidgets.QMainWindow()
            self.ui = Ui_Alerta()
            self.ui.setupUi(self.ventana)
            self.ventana.show()
            
    #Asignación de texto a los botones y labels.       
    def retranslateUi(self, EliminarProducto):
        _translate = QtCore.QCoreApplication.translate
        EliminarProducto.setWindowTitle(_translate("EliminarProducto", "MainWindow"))
        self.label_5.setText(_translate("EliminarProducto", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">ELIMINAR PRODUCTO</span></p></body></html>"))
        self.label.setText(_translate("EliminarProducto", "<html><head/><body><p align=\"center\">CLAVE</p></body></html>"))
        self.label_2.setText(_translate("EliminarProducto", "<html><head/><body><p align=\"center\">NOMBRE</p></body></html>"))
        self.label_4.setText(_translate("EliminarProducto", "<html><head/><body><p align=\"center\">PROVEEDOR</p></body></html>"))
        self.label_8.setText(_translate("EliminarProducto", "<html><head/><body><p align=\"center\">INVENTARIO</p></body></html>"))
        self.label_3.setText(_translate("EliminarProducto", "<html><head/><body><p align=\"center\">PRECIO</p></body></html>"))
        self.Eliminar.setText(_translate("EliminarProducto", "ELIMINAR"))
        self.Limpiar.setText(_translate("EliminarProducto", "LIMPIAR"))
        self.Cargar.setText(_translate("EliminarProducto", "CARGAR"))

#Cerrar aplicación.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EliminarProducto = QtWidgets.QMainWindow()
    ui = Ui_EliminarProducto()
    ui.setupUi(EliminarProducto)
    EliminarProducto.show()
    sys.exit(app.exec_())
