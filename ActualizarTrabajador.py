#Importación de sql para establecer la conexión y excepciones.
import sqlite3
from sqlite3 import Error
#Importación de ventanas para conectar en las funciones.
from DatosActualizados import Ui_DatosActualizados
from ClaveExistenteUP import Ui_ClaveExistente
from ClaveInexistenteUP import Ui_ClaveInexistenteUP
from ClavePuestoInexistente import Ui_ClaveInexistentePuesto
from Alerta import Ui_Alerta
#Librería para crear nuestra aplicación.
from PyQt5 import QtCore, QtGui, QtWidgets


#Creación de la aplicación. (Menú de trabajador donde se introducen los datos del trabajador a actualizar.)
class Ui_ActualizarTrabajador(object):
    def setupUi(self, ActualizarTrabajador):
        ActualizarTrabajador.setObjectName("ActualizarTrabajador")
        ActualizarTrabajador.resize(293, 515)
        ActualizarTrabajador.setStyleSheet("background-color: rgb(226, 230, 255);")
        self.centralwidget = QtWidgets.QWidget(ActualizarTrabajador)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 291, 51))
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 69, 91, 21))
        self.label.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 150, 101, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 190, 101, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 230, 101, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 270, 101, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 350, 101, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 390, 101, 20))
        self.label_11.setObjectName("label_11")
        self.claveT = QtWidgets.QLineEdit(self.centralwidget)
        self.claveT.setGeometry(QtCore.QRect(120, 60, 161, 31))
        self.claveT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.claveT.setObjectName("claveT")
        self.Nombre = QtWidgets.QLineEdit(self.centralwidget)
        self.Nombre.setGeometry(QtCore.QRect(120, 100, 161, 31))
        self.Nombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Nombre.setObjectName("Nombre")
        self.ApellidoP = QtWidgets.QLineEdit(self.centralwidget)
        self.ApellidoP.setGeometry(QtCore.QRect(120, 140, 161, 31))
        self.ApellidoP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ApellidoP.setObjectName("ApellidoP")
        self.ApellidoM = QtWidgets.QLineEdit(self.centralwidget)
        self.ApellidoM.setGeometry(QtCore.QRect(120, 180, 161, 31))
        self.ApellidoM.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ApellidoM.setObjectName("ApellidoM")
        self.Fecha = QtWidgets.QLineEdit(self.centralwidget)
        self.Fecha.setGeometry(QtCore.QRect(120, 220, 161, 31))
        self.Fecha.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Fecha.setText("")
        self.Fecha.setObjectName("Fecha")
        self.Telefono = QtWidgets.QLineEdit(self.centralwidget)
        self.Telefono.setGeometry(QtCore.QRect(120, 260, 161, 31))
        self.Telefono.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Telefono.setObjectName("Telefono")
        self.Usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.Usuario.setGeometry(QtCore.QRect(120, 300, 161, 31))
        self.Usuario.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Usuario.setObjectName("Usuario")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 310, 101, 20))
        self.label_12.setObjectName("label_12")
        self.Contra = QtWidgets.QLineEdit(self.centralwidget)
        self.Contra.setGeometry(QtCore.QRect(120, 340, 161, 31))
        self.Contra.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Contra.setObjectName("Contra")
        self.Actualizar = QtWidgets.QPushButton(self.centralwidget)
        self.Actualizar.setGeometry(QtCore.QRect(200, 430, 75, 23))
        self.Actualizar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Actualizar.setObjectName("Actualizar")
        self.Verificar = QtWidgets.QPushButton(self.centralwidget)
        self.Verificar.setGeometry(QtCore.QRect(110, 431, 75, 23))
        self.Verificar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Verificar.setObjectName("Verificar")
        self.Limpiar = QtWidgets.QPushButton(self.centralwidget)
        self.Limpiar.setGeometry(QtCore.QRect(20, 431, 75, 23))
        self.Limpiar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Limpiar.setObjectName("Limpiar")
        self.CPuesto = QtWidgets.QLineEdit(self.centralwidget)
        self.CPuesto.setGeometry(QtCore.QRect(120, 380, 161, 31))
        self.CPuesto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CPuesto.setObjectName("CPuesto")
        ActualizarTrabajador.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ActualizarTrabajador)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 293, 21))
        self.menubar.setObjectName("menubar")
        ActualizarTrabajador.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ActualizarTrabajador)
        self.statusbar.setObjectName("statusbar")
        ActualizarTrabajador.setStatusBar(self.statusbar)

        self.retranslateUi(ActualizarTrabajador)
        #Boton Limpiar para limpiar todos los campos.
        self.Limpiar.clicked.connect(self.claveT.clear)
        self.Limpiar.clicked.connect(self.Nombre.clear)
        self.Limpiar.clicked.connect(self.ApellidoP.clear)
        self.Limpiar.clicked.connect(self.ApellidoM.clear)
        self.Limpiar.clicked.connect(self.Fecha.clear)
        self.Limpiar.clicked.connect(self.Telefono.clear)
        self.Limpiar.clicked.connect(self.Usuario.clear)
        self.Limpiar.clicked.connect(self.Contra.clear)
        self.Limpiar.clicked.connect(self.CPuesto.clear)
        QtCore.QMetaObject.connectSlotsByName(ActualizarTrabajador)
        #Botones programados
        #Boton que permite actualizar la información a la base de datos.
        self.Actualizar.clicked.connect(self.UpdateData)
        #Boton que permite verificar que la información cargada en la aplicación sea válida.
        self.Verificar.clicked.connect(self.VerificarDatos)

    #Función que permite verificar que la información dada por el usuario sea válida para cargar.
    def VerificarDatos(self):
        #Try para excepciones. 
        try:
            #Conexión a la base de datos
            with sqlite3.connect("PIA_1845788.db") as conn:
                #Definir nuestro cursor.
                micursor = conn.cursor()
                #Leer clave de trabajador que se introduce en nuestra ventana de Actualizar Trabajador.
                Clave = self.claveT.text()
                #Convertir la clave a entero.Ya que en la base se tiene como Entero.
                clave = int(Clave)
                #Ejecutar una línea que nos permite obtener todas las claves guardadas en Trabajador.
                micursor.execute("SELECT Clave_Trabajador FROM Trabajador")
                #Guardar los resultados en la variable claveT
                claveT = micursor.fetchall()
                #Declarar una lista donde se guardaran las claves de trabajador.
                listaClaves = []
                #Ciclo para el unpack del resultado de claveT.
                for dato in claveT:
                    for n in dato:
                        ClaveT= int(n)
                        #Agregar cada clave a la lista de listaClaves.
                        listaClaves.append(ClaveT)
                #Leer clave de puesto que se introduce en nuestra ventana de Agregar Trabajador.
                ClaveP = self.CPuesto.text()
                #Convertir la clave a entero. Ya que en la base se tiene como Entero.
                clavePuesto = int(ClaveP)
                #Ejecutar una línea que nos permite obtener todas las claves guardadas en Puesto.
                micursor.execute("SELECT Clave FROM Puesto")
                #Guardar los resultados en la variable claveP.
                claveP = micursor.fetchall()
                #Declarar una lista donde se guardaran las claves de puesto.
                listaClavesP = []
                #Ciclo para el unpack del resultado de claveP.
                for dato in claveP:
                    for n in dato:
                        ClaveP= int(n)
                        #Agregar cada clave a la lista de listaClavesP.
                        listaClavesP.append(ClaveP)
                #ESTO ES UNA DOBLE VERIFICACIÓN YA QUE TAMBIÉN SE HACE EN LA FUNCIÓN DE AGREGAR.
                #Si la clave de trabajador que introdujo el usuario esta dentro de listaClaves y la clave de puesto que introdujo es parte de listaClavesP:
                if clave in listaClaves and clavePuesto in listaClavesP:
                    #Se muestra una ventana donde se avisa que la clave es existente. (Hablando de ambas claves
                    self.ventana = QtWidgets.QMainWindow()
                    self.ui = Ui_ClaveExistente()
                    self.ui.setupUi(self.ventana)
                    self.ventana.show()
                #Si la clave del trabajador que introdujo el usuario NO se encuentra dentro de listaClaves.
                elif clave not in listaClaves:
                    #Se muestra una ventana donde se avisa que la clave de trabajador no existe, por lo tanto no se puede actualizar.
                    self.ventana = QtWidgets.QMainWindow()
                    self.ui = Ui_ClaveInexistenteUP()
                    self.ui.setupUi(self.ventana)
                    self.ventana.show()
                #Si la clave del puesto que introdujo el usuario NO se encuentra dentro de listaClavesP:
                elif clavePuesto not in listaClavesP:
                    #Se muestra una ventana donde se avisa que la clave de puesto no existe, por lo tanto no se puede actualizar.
                    self.ventana = QtWidgets.QMainWindow()
                    self.ui = Ui_ClaveInexistentePuesto()
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
                #Leer clave de trabajador que se introduce en nuestra ventana de Actualizar Trabajador.
                Clave = self.claveT.text()
                #Convertir la clave a entero.Ya que en la base se tiene como Entero.
                clave = int(Clave)
                #Ejecutar una línea que nos permite obtener todas las claves guardadas en Trabajador.
                micursor.execute("SELECT Clave_Trabajador FROM Trabajador")
                #Guardar los resultados en la variable claveT
                claveT = micursor.fetchall()
                #Declarar una lista donde se guardaran las claves de trabajador.
                listaClaves = []
                #Ciclo para el unpack del resultado de claveT.
                for dato in claveT:
                    for n in dato:
                        ClaveT= int(n)
                        #Agregar cada clave a la lista de listaClaves.
                        listaClaves.append(ClaveT)
                #Leer clave de puesto que se introduce en nuestra ventana de Agregar Trabajador.
                ClaveP = self.CPuesto.text()
                #Convertir la clave a entero. Ya que en la base se tiene como Entero.
                clavePuesto = int(ClaveP)
                #Ejecutar una línea que nos permite obtener todas las claves guardadas en Puesto.
                micursor.execute("SELECT Clave FROM Puesto")
                #Guardar los resultados en la variable claveP.
                claveP = micursor.fetchall()
                #Declarar una lista donde se guardaran las claves de puesto.
                listaClavesP = []
                #Ciclo para el unpack del resultado de claveP.
                for dato in claveP:
                    for n in dato:
                        ClaveP= int(n)
                        #Agregar cada clave a la lista de listaClavesP.
                        listaClavesP.append(ClaveP)
                #ESTO ES UNA DOBLE VERIFICACIÓN YA QUE TAMBIÉN SE HACE EN LA FUNCIÓN DE AGREGAR.
                #Si la clave de trabajador que introdujo el usuario esta dentro de listaClaves y la clave de puesto que introdujo es parte de listaClavesP:
                if clave in listaClaves and clavePuesto in listaClavesP:
                    #Se lee el nombre que se introduce en la aplicación y se agrega a la variable nombre.
                    nombre = self.Nombre.text()
                    #Se lee el apellido paterno que se introduce en la aplicación y se agrega a la variable apellidoP.
                    apellidoP = self.ApellidoP.text()
                    #Se lee el apellido materno que se introduce en la aplicación y se agrega a la variable apellidoM.
                    apellidoM = self.ApellidoM.text()
                    #Se lee la fecha de ingreso que se introduce en la aplicación y se agrega a la variable fechaIngreso.
                    fechaIngreso = self.Fecha.text()
                    #Se lee el telefono que se introduce en la aplicación y se agrega a la variable Telefono.
                    Telefono = self.Telefono.text()
                    #Se cambia el valor a entero y se guarda en la variable telefono. Ya que en la base se tiene como Entero.
                    telefono = int(Telefono)
                    #Se lee el valor de usuario que se introduce en la aplicación y se agrega a la variable usuario.
                    usuario = self.Usuario.text()
                    #Se lee el valor de contraseña que se introduce en la aplicación y se agrega a la variable contraseña.
                    contraseña = self.Contra.text()
                    #Se lee el valor de clavePuesto que se introduce en la aplicación y se agrega a la variable cpuesto.
                    cpuesto = self.CPuesto.text()
                    #VARIABLE DONDE SE GUARDA LA LINEA PARA ACTUALIZAR LA INFORMACIÓN DE TRABAJADOR.
                    query = """UPDATE Trabajador SET Nombre = ?, ApellidoPaterno = ?, ApellidoMaterno = ?, Fecha_Ingreso = ?, Telefono = ?, Usuario = ?, Contraseña = ?,Puesto = ? WHERE Clave_Trabajador= ?"""
                    #VARIABLE DONDE SE GUARDAN LAS VARIABLES QUE CONTIENEN LA INFORMACION QUE SE GUARDARA.
                    inputData = (nombre, apellidoP, apellidoM, fechaIngreso,telefono,usuario, contraseña,cpuesto,clave)
                    #Se ejecuta las variables en conjunto, permitiendo actualizar la información.
                    micursor.execute(query,inputData)
                    #Ventana donde aparece que los datos fueron actualizados correctamente.
                    self.ventana = QtWidgets.QMainWindow()
                    self.ui = Ui_DatosActualizados()
                    self.ui.setupUi(self.ventana)
                    self.ventana.show()
                #Si la clave del trabajador que introdujo el usuario NO se encuentra dentro de listaClaves.
                elif clave not in listaClaves:
                    #Se muestra una ventana donde se avisa que la clave de trabajador no existe, por lo tanto no se puede actualizar.
                    self.ventana = QtWidgets.QMainWindow()
                    self.ui = Ui_ClaveInexistenteUP()
                    self.ui.setupUi(self.ventana)
                    self.ventana.show()
                #Si la clave del puesto que introdujo el usuario NO se encuentra dentro de listaClavesP:
                elif clavePuesto not in listaClavesP:
                    #Se muestra una ventana donde se avisa que la clave de puesto no existe, por lo tanto no se puede actualizar.
                    self.ventana = QtWidgets.QMainWindow()
                    self.ui = Ui_ClaveInexistentePuesto()
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
    def retranslateUi(self, ActualizarTrabajador):
        _translate = QtCore.QCoreApplication.translate
        ActualizarTrabajador.setWindowTitle(_translate("ActualizarTrabajador", "MainWindow"))
        self.label_5.setText(_translate("ActualizarTrabajador", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">ACTUALIZAR TRABAJADOR</span></p></body></html>"))
        self.label.setText(_translate("ActualizarTrabajador", "<html><head/><body><p align=\"center\">CLAVE</p></body></html>"))
        self.label_2.setText(_translate("ActualizarTrabajador", "<html><head/><body><p align=\"center\">NOMBRE</p></body></html>"))
        self.label_6.setText(_translate("ActualizarTrabajador", "<html><head/><body><p align=\"center\">APELLIDO PATERNO</p></body></html>"))
        self.label_7.setText(_translate("ActualizarTrabajador", "<html><head/><body><p align=\"center\">APELLIDO MATERNO</p></body></html>"))
        self.label_8.setText(_translate("ActualizarTrabajador", "<html><head/><body><p align=\"center\">FECHA INGRESO</p></body></html>"))
        self.label_9.setText(_translate("ActualizarTrabajador", "<html><head/><body><p align=\"center\">TELÉFONO</p></body></html>"))
        self.label_10.setText(_translate("ActualizarTrabajador", "<html><head/><body><p align=\"center\">CONTRASEÑA</p></body></html>"))
        self.label_11.setText(_translate("ActualizarTrabajador", "<html><head/><body><p align=\"center\">CLAVE PUESTO</p></body></html>"))
        self.label_12.setText(_translate("ActualizarTrabajador", "<html><head/><body><p align=\"center\">USUARIO</p></body></html>"))
        self.Actualizar.setText(_translate("ActualizarTrabajador", "ACTUALIZAR"))
        self.Verificar.setText(_translate("ActualizarTrabajador", "VERIFICAR"))
        self.Limpiar.setText(_translate("ActualizarTrabajador", "LIMPIAR"))

#Cerrar aplicación.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ActualizarTrabajador = QtWidgets.QMainWindow()
    ui = Ui_ActualizarTrabajador()
    ui.setupUi(ActualizarTrabajador)
    ActualizarTrabajador.show()
    sys.exit(app.exec_())
