#Importación de sql para establecer la conexión y excepciones.
import sqlite3
from sqlite3 import Error
#Librería para crear nuestra aplicación.
from PyQt5 import QtCore, QtGui, QtWidgets
#Importación de ventanas para conectar en las funciones.
from DatosEliminados import Ui_DatosEliminados
from ClaveInexistenteEP import Ui_ClaveInexistenteEP
from Alerta import Ui_Alerta

#Creación de la aplicación. (Menú de clientes donde se introduce la clave a eliminar.)
class Ui_EliminarClientes(object):
    def setupUi(self, EliminarClientes):
        EliminarClientes.setObjectName("EliminarClientes")
        EliminarClientes.resize(311, 408)
        EliminarClientes.setStyleSheet("background-color: rgb(226, 230, 255);")
        self.centralwidget = QtWidgets.QWidget(EliminarClientes)
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
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 280, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 230, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 150, 101, 20))
        self.label_6.setObjectName("label_6")
        self.claveC = QtWidgets.QLineEdit(self.centralwidget)
        self.claveC.setGeometry(QtCore.QRect(120, 60, 161, 31))
        self.claveC.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.claveC.setObjectName("claveC")
        self.Eliminar = QtWidgets.QPushButton(self.centralwidget)
        self.Eliminar.setGeometry(QtCore.QRect(220, 340, 75, 23))
        self.Eliminar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Eliminar.setObjectName("Eliminar")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 190, 101, 20))
        self.label_7.setObjectName("label_7")
        self.Nombre = QtWidgets.QTextBrowser(self.centralwidget)
        self.Nombre.setGeometry(QtCore.QRect(120, 100, 161, 31))
        self.Nombre.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.Nombre.setObjectName("Nombre")
        self.Direccion = QtWidgets.QTextBrowser(self.centralwidget)
        self.Direccion.setGeometry(QtCore.QRect(120, 260, 161, 61))
        self.Direccion.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.Direccion.setObjectName("Direccion")
        self.Telefono = QtWidgets.QTextBrowser(self.centralwidget)
        self.Telefono.setGeometry(QtCore.QRect(120, 220, 161, 31))
        self.Telefono.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.Telefono.setObjectName("Telefono")
        self.ApellidoP = QtWidgets.QTextBrowser(self.centralwidget)
        self.ApellidoP.setGeometry(QtCore.QRect(120, 140, 161, 31))
        self.ApellidoP.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.ApellidoP.setObjectName("ApellidoP")
        self.ApellidoM = QtWidgets.QTextBrowser(self.centralwidget)
        self.ApellidoM.setGeometry(QtCore.QRect(120, 180, 161, 31))
        self.ApellidoM.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.ApellidoM.setObjectName("ApellidoM")
        self.Limpiar = QtWidgets.QPushButton(self.centralwidget)
        self.Limpiar.setGeometry(QtCore.QRect(20, 340, 75, 23))
        self.Limpiar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Limpiar.setObjectName("Limpiar")
        self.Cargar = QtWidgets.QPushButton(self.centralwidget)
        self.Cargar.setGeometry(QtCore.QRect(120, 340, 75, 23))
        self.Cargar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Cargar.setObjectName("Cargar")
        EliminarClientes.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EliminarClientes)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 311, 21))
        self.menubar.setObjectName("menubar")
        EliminarClientes.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EliminarClientes)
        self.statusbar.setObjectName("statusbar")
        EliminarClientes.setStatusBar(self.statusbar)

        self.retranslateUi(EliminarClientes)
        #Boton Limpiar para limpiar todos los campos.
        self.Limpiar.clicked.connect(self.claveC.clear)
        self.Limpiar.clicked.connect(self.Nombre.clear)
        self.Limpiar.clicked.connect(self.ApellidoP.clear)
        self.Limpiar.clicked.connect(self.ApellidoM.clear)
        self.Limpiar.clicked.connect(self.Telefono.clear)
        self.Limpiar.clicked.connect(self.Direccion.clear)
        QtCore.QMetaObject.connectSlotsByName(EliminarClientes)
        #Programación de botones
        #Boton que permite cargar la información en la aplicación.
        self.Cargar.clicked.connect(self.ShowData)
        #Boton que permite eliminar la información obtenida de la base de datos.
        self.Eliminar.clicked.connect(self.DeleteData)
    
    #Función que permite eliminar la información de la base de datos según la clave dada.
    def DeleteData(self):
        #Try para excepciones.
        try:
            #Conexión a la base de datos.
            with sqlite3.connect("PIA_1845788.db") as conn:
                #Leer clave de producto que se introduce en nuestra ventana de Eliminar Cliente.
                Clave = self.claveC.text()
                #Convertir la clave a entero.
                clave = int(Clave)
                #Definir nuestro cursor.
                mi_cursor = conn.cursor()
                #Ejecutar una línea que nos permite obtener todas las claves guardadas en cliente.
                c= mi_cursor.execute("SELECT Clave_Cliente FROM Cliente")
                #Guardar los resultados en la variable claves.
                claves = mi_cursor.fetchall()
                #Declarar una lista donde se guardaran las claves de clientes.
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
                    mi_cursor.execute("DELETE FROM Cliente WHERE Clave_Cliente= (:clave)",valor)
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
                #Leer clave de producto que se introduce en nuestra ventana de Eliminar Cliente.
                Clave = self.claveC.text()
                #Convertir la clave a entero.
                clave = int(Clave)
                #Definir nuestro cursor.
                mi_cursor = conn.cursor()
                #Ejecutar una línea que nos permite obtener todas las claves guardadas en cliente.
                c= mi_cursor.execute("SELECT Clave_Cliente FROM Cliente")
                #Guardar los resultados en la variable claves.
                claves = mi_cursor.fetchall()
                #Declarar una lista donde se guardaran las claves de clientes.
                ClaveP = []
                #Ciclo para el unpack del resultado de claves.
                for dato in claves:
                    for n in dato:
                        CLAVEP = int(n)
                        #Agregar cada clave en la lista ClaveP.
                        ClaveP.append(CLAVEP)
                
                #ESTO ES UNA DOBLE VERIFICACIÓN YA QUE TAMBIÉN SE HACE EN LA FUNCIÓN DE ELIMINAR.
                #Si la clave que introdujo el usuario esta dentro de la lista de claves.
                if clave in ClaveP:
                    #Guardar la clave en el diccionario valor, para posteriormente utilizarlo.
                    valor = {"clave":clave}
                    #Buscar nombre del cliente en la base de datos según la clave dada por el usuario y mostrarlo.
                    c = mi_cursor.execute("SELECT Nombre FROM Cliente WHERE Clave_Cliente = (:clave)",valor)
                    #Guardar el resultado en la variable nombre.
                    nombre = mi_cursor.fetchall()
                    #Ciclo para el unpack del resultado de nombre.
                    for dato in nombre:
                        for n in dato:
                            Nombre = str(n)
                    #Asignar al campo de Nombre el valor de Nombre que se obtuvo anteriormente.
                    self.Nombre.setText(Nombre)
                    
                    #Buscar el apellido paterno del cliente en la base de datos según la clave dada por el usuario y mostrarlo.
                    c = mi_cursor.execute("SELECT Apellido_Paterno FROM Cliente WHERE Clave_Cliente = (:clave)",valor)
                    #Guardar el resultado en la variable apP.
                    apP = mi_cursor.fetchall()
                    #Ciclo para el unpack del resultado de apP.
                    for dato in apP:
                        for n in dato:
                            paterno = str(n)
                    #Asignar al campo de ApellidoP el valor de paterno que se obtuvo anteriormente.
                    self.ApellidoP.setText(paterno)
                    
                    #Buscar el apellido materno del cliente en la base de datos según la clave dada por el usuario y mostrarlo.
                    c = mi_cursor.execute("SELECT Apellido_Materno FROM Cliente WHERE Clave_Cliente = (:clave)",valor)
                    #Guardar el resultado en la variable apM.
                    apM = mi_cursor.fetchall()
                    #Ciclo para el unpack del resultado de apM.
                    for dato in apM:
                        for n in dato:
                            materno = str(n)
                    #Asignar al campo de ApellidoM el valor de materno que se obtuvo anteriormente.
                    self.ApellidoM.setText(materno)
                    
                    #Buscar el telefono del cliente en la base de datos según la clave dada por el usuario y mostrarlo.
                    c = mi_cursor.execute("SELECT Telefono FROM Cliente WHERE Clave_Cliente = (:clave)",valor)
                    #Guardar el resultado en la variable tel.
                    tel = mi_cursor.fetchall()
                    #Ciclo para el unpack del resultado de tel.
                    for dato in tel:
                        for n in dato:
                            Telefono = str(n)
                    #Asignar al campo de Telefono el valor de Telefono que se obtuvo anteriormente.
                    self.Telefono.setText(Telefono)
                    
                    #Buscar la direccion del cliente en la base de datos según la clave dada por el usuario y mostrarlo.
                    c = mi_cursor.execute("SELECT Dirección FROM Cliente WHERE Clave_Cliente = (:clave)",valor)
                    #Guardar el resultado en la variable direccion.
                    direccion= mi_cursor.fetchall()
                    #Ciclo para el unpack del resultado de direccion.
                    for dato in direccion:
                        for n in dato:
                            Direccion = str(n)
                    #Asignar al campo de Direccion el valor de Direccion que se obtuvo anteriormente.
                    self.Direccion.setText(Direccion)
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
    def retranslateUi(self, EliminarClientes):
        _translate = QtCore.QCoreApplication.translate
        EliminarClientes.setWindowTitle(_translate("EliminarClientes", "MainWindow"))
        self.label_5.setText(_translate("EliminarClientes", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">ELIMINAR CLIENTES</span></p></body></html>"))
        self.label.setText(_translate("EliminarClientes", "<html><head/><body><p align=\"center\">CLAVE</p></body></html>"))
        self.label_2.setText(_translate("EliminarClientes", "<html><head/><body><p align=\"center\">NOMBRE</p></body></html>"))
        self.label_3.setText(_translate("EliminarClientes", "<html><head/><body><p align=\"center\">DIRECCIÓN</p></body></html>"))
        self.label_4.setText(_translate("EliminarClientes", "<html><head/><body><p align=\"center\">TELÉFONO</p></body></html>"))
        self.label_6.setText(_translate("EliminarClientes", "<html><head/><body><p align=\"center\">APELLIDO PATERNO</p></body></html>"))
        self.Eliminar.setText(_translate("EliminarClientes", "ELIMINAR"))
        self.label_7.setText(_translate("EliminarClientes", "<html><head/><body><p align=\"center\">APELLIDO MATERNO</p></body></html>"))
        self.Limpiar.setText(_translate("EliminarClientes", "LIMPIAR"))
        self.Cargar.setText(_translate("EliminarClientes", "CARGAR"))

#Cerrar aplicación.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EliminarClientes = QtWidgets.QMainWindow()
    ui = Ui_EliminarClientes()
    ui.setupUi(EliminarClientes)
    EliminarClientes.show()
    sys.exit(app.exec_())
