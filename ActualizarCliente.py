#Importación de sql para establecer la conexión y excepciones.
import sqlite3
from sqlite3 import Error
#Librería para crear nuestra aplicación.
from PyQt5 import QtCore, QtGui, QtWidgets
#Importación de ventanas para conectar en las funciones.
from ClaveExistenteUP import Ui_ClaveExistente
from ClaveInexistenteUP import Ui_ClaveInexistenteUP
from DatosActualizados import Ui_DatosActualizados
from Alerta import Ui_Alerta

#Creación de la aplicación. (Menú de cliente donde se introducen los datos del cliente a actualizar.)
class Ui_ActualizarCliente(object):
    def setupUi(self, ActualizarCliente):
        ActualizarCliente.setObjectName("ActualizarCliente")
        ActualizarCliente.resize(314, 398)
        ActualizarCliente.setStyleSheet("background-color: rgb(226, 230, 255);")
        self.centralwidget = QtWidgets.QWidget(ActualizarCliente)
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
        self.Verificar = QtWidgets.QPushButton(self.centralwidget)
        self.Verificar.setGeometry(QtCore.QRect(120, 330, 75, 23))
        self.Verificar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Verificar.setObjectName("Verificar")
        self.Limpiar = QtWidgets.QPushButton(self.centralwidget)
        self.Limpiar.setGeometry(QtCore.QRect(20, 330, 75, 23))
        self.Limpiar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Limpiar.setObjectName("Limpiar")
        self.Actualizar = QtWidgets.QPushButton(self.centralwidget)
        self.Actualizar.setGeometry(QtCore.QRect(220, 330, 75, 23))
        self.Actualizar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Actualizar.setObjectName("Actualizar")
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
        ActualizarCliente.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ActualizarCliente)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 314, 21))
        self.menubar.setObjectName("menubar")
        ActualizarCliente.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ActualizarCliente)
        self.statusbar.setObjectName("statusbar")
        ActualizarCliente.setStatusBar(self.statusbar)

        self.retranslateUi(ActualizarCliente)
        #Boton Limpiar para limpiar todos los campos.
        self.Limpiar.clicked.connect(self.claveC.clear)
        self.Limpiar.clicked.connect(self.Nombre.clear)
        self.Limpiar.clicked.connect(self.ApellidoP.clear)
        self.Limpiar.clicked.connect(self.ApellidoM.clear)
        self.Limpiar.clicked.connect(self.Telefono.clear)
        self.Limpiar.clicked.connect(self.Direccion.clear)
        QtCore.QMetaObject.connectSlotsByName(ActualizarCliente)
        #Botones programados
        #Boton que permite actualizar la información a la base de datos.
        self.Actualizar.clicked.connect(self.UpdateData)
        #Boton que permite verificar que la información cargada en la aplicación sea válida.
        self.Verificar.clicked.connect(self.VerificarDatos)

    def VerificarDatos(self):
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
                    #Se muestra una ventana donde se avisa que la clave es existente, por lo tanto se puede actualizar
                    self.ventana = QtWidgets.QMainWindow()
                    self.ui = Ui_ClaveExistente()
                    self.ui.setupUi(self.ventana)
                    self.ventana.show()
                #Si la clave no esta dentro de la lista:
                else:
                    #Se muestra una ventana donde se avisa que la clave no existe, por lo tanto no se puede actualizar.
                    self.ventana = QtWidgets.QMainWindow()
                    self.ui = Ui_ClaveInexistenteUP()
                    self.ui.setupUi(self.ventana)
                    self.ventana.show()
        #Excepcion por si ocurre un error con sqlite3.
        except Error as e:
            print(e)
        #Excepción por si no se llenan los campos necesarios
        except:
            #Ventana que muestra el mensaje donde se piden llenar todos los campos.
            self.ventana = QtWidgets.QMainWindow()
            self.ui = Ui_Alerta()
            self.ui.setupUi(self.ventana)
            self.ventana.show()
            
    def UpdateData(self):
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
                    #VARIABLE DONDE SE GUARDA LA LINEA PARA ACTUALIZAR LA INFORMACIÓN DE CLIENTE.
                    query = """UPDATE Cliente SET Nombre = ?, Apellido_Paterno = ?, Apellido_Materno = ?, Telefono = ?, Dirección = ? WHERE Clave_Cliente = ?"""
                    #VARIABLE DONDE SE GUARDAN LAS VARIABLES QUE CONTIENEN LA INFORMACION QUE SE GUARDARA.
                    inputData = (nombre, apellidoP, apellidoM, telefono,direccion,clave)
                    #Se ejecuta las variables en conjunto, permitiendo actualizar la información.
                    micursor.execute(query,inputData)
                    #Ventana donde aparece que los datos fueron actualizados correctamente.
                    self.ventana = QtWidgets.QMainWindow()
                    self.ui = Ui_DatosActualizados()
                    self.ui.setupUi(self.ventana)
                    self.ventana.show()
                #Si la clave del proveedor que introdujo el usuario NO se encuentra dentro de listaClaves.
                else:
                    #Se muestra una ventana donde se avisa que la clave de proveedor no existe, por lo tanto no se puede actualizar.
                    self.ventana = QtWidgets.QMainWindow()
                    self.ui = Ui_ClaveInexistenteUP()
                    self.ui.setupUi(self.ventana)
                    self.ventana.show()
        #Excepcion por si ocurre un error con sqlite3.
        except Error as e:
            print(e)
        #Excepción por si no se llenan los campos necesarios
        except:
            #Ventana que muestra el mensaje donde se piden llenar todos los campos.
            self.ventana = QtWidgets.QMainWindow()
            self.ui = Ui_Alerta()
            self.ui.setupUi(self.ventana)
            self.ventana.show()
            
    #Asignación de texto a los botones y labels. 
    def retranslateUi(self, ActualizarCliente):
        _translate = QtCore.QCoreApplication.translate
        ActualizarCliente.setWindowTitle(_translate("ActualizarCliente", "MainWindow"))
        self.label_5.setText(_translate("ActualizarCliente", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">ACTUALIZAR CLIENTE</span></p></body></html>"))
        self.label.setText(_translate("ActualizarCliente", "<html><head/><body><p align=\"center\">CLAVE</p></body></html>"))
        self.label_2.setText(_translate("ActualizarCliente", "<html><head/><body><p align=\"center\">NOMBRE</p></body></html>"))
        self.label_3.setText(_translate("ActualizarCliente", "<html><head/><body><p align=\"center\">DIRECCIÓN</p></body></html>"))
        self.label_4.setText(_translate("ActualizarCliente", "<html><head/><body><p align=\"center\">TELÉFONO</p></body></html>"))
        self.label_6.setText(_translate("ActualizarCliente", "<html><head/><body><p align=\"center\">APELLIDO PATERNO</p></body></html>"))
        self.label_7.setText(_translate("ActualizarCliente", "<html><head/><body><p align=\"center\">APELLIDO MATERNO</p></body></html>"))
        self.Verificar.setText(_translate("ActualizarCliente", "VERIFICAR"))
        self.Limpiar.setText(_translate("ActualizarCliente", "LIMPIAR"))
        self.Actualizar.setText(_translate("ActualizarCliente", "ACTUALIZAR"))

#Cerrar aplicación.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ActualizarCliente = QtWidgets.QMainWindow()
    ui = Ui_ActualizarCliente()
    ui.setupUi(ActualizarCliente)
    ActualizarCliente.show()
    sys.exit(app.exec_())
