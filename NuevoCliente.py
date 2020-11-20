#Importación de sql para establecer la conexión y excepciones.
import sqlite3
from sqlite3 import Error
#Importación de ventanas para conectar en las funciones.
from DatosAgregados import Ui_DatosAgregados
from ClaveExistente import Ui_ClaveExistente
from ClaveInexistente import Ui_ClaveInexistente
from Alerta import Ui_Alerta
#Librería para crear nuestra aplicación.
from PyQt5 import QtCore, QtGui, QtWidgets

#Creación de la aplicación. (Menú de cliente donde se introducen los datos del cliente a agregar.)
class Ui_NuevoCliente(object):
    def setupUi(self, NuevoCliente):
        NuevoCliente.setObjectName("NuevoCliente")
        NuevoCliente.resize(314, 398)
        NuevoCliente.setStyleSheet("background-color: rgb(226, 230, 255);")
        self.centralwidget = QtWidgets.QWidget(NuevoCliente)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 311, 51))
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 69, 91, 21))
        self.label.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 280, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 230, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 150, 101, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 190, 101, 20))
        self.label_7.setObjectName("label_7")
        self.Cargar = QtWidgets.QPushButton(self.centralwidget)
        self.Cargar.setGeometry(QtCore.QRect(120, 330, 75, 23))
        self.Cargar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Cargar.setObjectName("Cargar")
        self.Limpiar = QtWidgets.QPushButton(self.centralwidget)
        self.Limpiar.setGeometry(QtCore.QRect(20, 330, 75, 23))
        self.Limpiar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Limpiar.setObjectName("Limpiar")
        self.Agregar = QtWidgets.QPushButton(self.centralwidget)
        self.Agregar.setGeometry(QtCore.QRect(220, 330, 75, 23))
        self.Agregar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Agregar.setObjectName("Agregar")
        self.claveC = QtWidgets.QLineEdit(self.centralwidget)
        self.claveC.setGeometry(QtCore.QRect(130, 60, 161, 31))
        self.claveC.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.claveC.setObjectName("claveC")
        self.Nombre = QtWidgets.QLineEdit(self.centralwidget)
        self.Nombre.setGeometry(QtCore.QRect(130, 100, 161, 31))
        self.Nombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Nombre.setObjectName("Nombre")
        self.ApellidoP = QtWidgets.QLineEdit(self.centralwidget)
        self.ApellidoP.setGeometry(QtCore.QRect(130, 140, 161, 31))
        self.ApellidoP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ApellidoP.setObjectName("ApellidoP")
        self.ApellidoM = QtWidgets.QLineEdit(self.centralwidget)
        self.ApellidoM.setGeometry(QtCore.QRect(130, 180, 161, 31))
        self.ApellidoM.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ApellidoM.setObjectName("ApellidoM")
        self.Telefono = QtWidgets.QLineEdit(self.centralwidget)
        self.Telefono.setGeometry(QtCore.QRect(130, 220, 161, 31))
        self.Telefono.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Telefono.setObjectName("Telefono")
        self.Direccion = QtWidgets.QLineEdit(self.centralwidget)
        self.Direccion.setGeometry(QtCore.QRect(130, 260, 161, 51))
        self.Direccion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Direccion.setObjectName("Direccion")
        NuevoCliente.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NuevoCliente)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 314, 21))
        self.menubar.setObjectName("menubar")
        NuevoCliente.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NuevoCliente)
        self.statusbar.setObjectName("statusbar")
        NuevoCliente.setStatusBar(self.statusbar)

        self.retranslateUi(NuevoCliente)
        #Boton Limpiar para limpiar todos los campos.
        self.Limpiar.clicked.connect(self.claveC.clear)
        self.Limpiar.clicked.connect(self.Nombre.clear)
        self.Limpiar.clicked.connect(self.ApellidoP.clear)
        self.Limpiar.clicked.connect(self.ApellidoM.clear)
        self.Limpiar.clicked.connect(self.Telefono.clear)
        self.Limpiar.clicked.connect(self.Direccion.clear)
        QtCore.QMetaObject.connectSlotsByName(NuevoCliente)
        #Botones programados
        #Boton que permite agregar la información a la base de datos
        self.Agregar.clicked.connect(self.LoadData)
        #Boton que permite verificar que la información cargada en la aplicación sea válida.
        self.Cargar.clicked.connect(self.Verificar)

    #Función que permite verificar que la información dada por el usuario sea válida para cargar.
    def Verificar(self):
        #Try para excepciones.
        try:
            #Conexión a la base de datos
            with sqlite3.connect("PIA_1845788.db") as conn:
                #Definir nuestro cursor.
                micursor = conn.cursor()
                #Leer clave de cliente que se introduce en nuestra ventana de Agregar Cliente.
                Clave = self.claveC.text()
                #Convertir la clave a entero.Ya que en la base se tiene como Entero.
                clave = int(Clave)
                #Ejecutar una línea que nos permite obtener todas las claves guardadas en Cliente.
                micursor.execute("SELECT Clave_Cliente FROM Cliente")
                #Guardar los resultados en la variable claveC
                claveC = micursor.fetchall()
                #Declarar una lista donde se guardaran las claves de cliente.
                listaClaves = []
                #Ciclo para el unpack del resultado de claveC.    
                for dato in claveC:
                    for n in dato:
                        ClaveC= int(n)
                        #Agregar cada clave a la lista de listaClaves
                        listaClaves.append(ClaveC)
                #ESTO ES UNA DOBLE VERIFICACIÓN YA QUE TAMBIÉN SE HACE EN LA FUNCIÓN DE AGREGAR.
                #Si la clave que introdujo el usuario esta dentro de la lista de claves.
                if clave in listaClaves:
                    #Se muestra una ventana donde avisa que la clave ya esta ocupada y que intente con otra.
                    self.ventana = QtWidgets.QMainWindow()
                    self.ui = Ui_ClaveExistente()
                    self.ui.setupUi(self.ventana)
                    self.ventana.show()
                #Si la clave del proveedor no esta dentro de la lista de claves de Proveedor. 
                else:
                    #Se muestra la ventana donde se avisa que la clave esta disponible y por lo tanto puede proseguir.
                    self.ventana = QtWidgets.QMainWindow()
                    self.ui = Ui_ClaveInexistente()
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
            
    def LoadData(self):
        #Try para excepciones.
        try:
            #Conexión a la base de datos
            with sqlite3.connect("PIA_1845788.db") as conn:
                #Definir nuestro cursor.
                micursor = conn.cursor()
                #Leer clave de cliente que se introduce en nuestra ventana de Agregar Cliente.
                Clave = self.claveC.text()
                #Convertir la clave a entero.Ya que en la base se tiene como Entero.
                clave = int(Clave)
                #Ejecutar una línea que nos permite obtener todas las claves guardadas en Cliente.
                micursor.execute("SELECT Clave_Cliente FROM Cliente")
                #Guardar los resultados en la variable claveC
                claveC = micursor.fetchall()
                #Declarar una lista donde se guardaran las claves de cliente.
                listaClaves = []
                #Ciclo para el unpack del resultado de claveC.    
                for dato in claveC:
                    for n in dato:
                        ClaveC= int(n)
                        #Agregar cada clave a la lista de listaClaves
                        listaClaves.append(ClaveC)
                #ESTO ES UNA DOBLE VERIFICACIÓN YA QUE TAMBIÉN SE HACE EN LA FUNCIÓN DE AGREGAR.
                #Si la clave que introdujo el usuario esta dentro de la lista de claves.
                if clave in listaClaves:
                    #Se muestra una ventana donde avisa que la clave ya esta ocupada y que intente con otra.
                    self.ventana = QtWidgets.QMainWindow()
                    self.ui = Ui_ClaveExistente()
                    self.ui.setupUi(self.ventana)
                    self.ventana.show()
                #Si la clave del proveedor no esta dentro de la lista de claves de Proveedor. 
                else:
                    #Se lee el nombre que se introduce en la aplicación y se agrega a la variable nombre.
                    nombre = self.Nombre.text()
                    #Se lee el apellido paterno que se introduce en la aplicación y se agrega a la variable apellidoP.
                    apellidoP = self.ApellidoP.text()
                    #Se lee el apellido materno que se introduce en la aplicación y se agrega a la variable apellidoM.
                    apellidoM = self.ApellidoM.text()
                    #Se lee el telefono que se introduce en la aplicación y se agrega a la variable Telefono.
                    Telefono = self.Telefono.text()
                    #Se cambia el valor a entero y se guarda en la variable telefono. Ya que en la base se tiene como Entero.
                    telefono = int(Telefono)
                    #Se lee la direccion que se introduce en la aplicación y se agrega a la variable direccion.
                    direccion = self.Direccion.text()
                    #Guardar valores en un diccionario, con una clave que distinga cada uno.
                    valores = {"clave": clave, "nombre": nombre, "apellidoP": apellidoP, "apellidoM": apellidoM, "telefono": telefono, "direccion":direccion}
                    #Ejecutar la linea de INSERT con las llaves del diccionario valores.
                    micursor.execute("INSERT INTO Cliente VALUES(:clave,:nombre,:apellidoP,:apellidoM,:telefono,:direccion)", valores)
                    #Se abre la ventana con el aviso que los datos han sido agregados exitosamente.
                    self.ventana = QtWidgets.QMainWindow()
                    self.ui = Ui_DatosAgregados()
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
    def retranslateUi(self, NuevoCliente):
        _translate = QtCore.QCoreApplication.translate
        NuevoCliente.setWindowTitle(_translate("NuevoCliente", "MainWindow"))
        self.label_5.setText(_translate("NuevoCliente", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">NUEVO CLIENTE</span></p></body></html>"))
        self.label.setText(_translate("NuevoCliente", "<html><head/><body><p align=\"center\">CLAVE</p></body></html>"))
        self.label_2.setText(_translate("NuevoCliente", "<html><head/><body><p align=\"center\">NOMBRE</p></body></html>"))
        self.label_3.setText(_translate("NuevoCliente", "<html><head/><body><p align=\"center\">DIRECCIÓN</p></body></html>"))
        self.label_4.setText(_translate("NuevoCliente", "<html><head/><body><p align=\"center\">TELÉFONO</p></body></html>"))
        self.label_6.setText(_translate("NuevoCliente", "<html><head/><body><p align=\"center\">APELLIDO PATERNO</p></body></html>"))
        self.label_7.setText(_translate("NuevoCliente", "<html><head/><body><p align=\"center\">APELLIDO MATERNO</p></body></html>"))
        self.Cargar.setText(_translate("NuevoCliente", "VERIFICAR"))
        self.Limpiar.setText(_translate("NuevoCliente", "LIMPIAR"))
        self.Agregar.setText(_translate("NuevoCliente", "AGREGAR"))

#Cerrar aplicación.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NuevoCliente = QtWidgets.QMainWindow()
    ui = Ui_NuevoCliente()
    ui.setupUi(NuevoCliente)
    NuevoCliente.show()
    sys.exit(app.exec_())
