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

#Creación de la aplicación. (Menú de proveedor donde se introducen los datos del proveedor a agregar.)
class Ui_MenuNP(object):
    def setupUi(self, MenuNP):
        MenuNP.setObjectName("MenuNP")
        MenuNP.resize(304, 392)
        MenuNP.setStyleSheet("background-color: rgb(226, 230, 255);")
        self.centralwidget = QtWidgets.QWidget(MenuNP)
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
        self.label_3.setGeometry(QtCore.QRect(20, 160, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 250, 81, 16))
        self.label_6.setObjectName("label_6")
        self.Agregar = QtWidgets.QPushButton(self.centralwidget)
        self.Agregar.setGeometry(QtCore.QRect(215, 319, 75, 23))
        self.Agregar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Agregar.setObjectName("Agregar")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 290, 81, 16))
        self.label_7.setObjectName("label_7")
        self.claveP = QtWidgets.QLineEdit(self.centralwidget)
        self.claveP.setGeometry(QtCore.QRect(120, 60, 161, 31))
        self.claveP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.claveP.setObjectName("claveP")
        self.nombreP = QtWidgets.QLineEdit(self.centralwidget)
        self.nombreP.setGeometry(QtCore.QRect(120, 100, 161, 31))
        self.nombreP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nombreP.setObjectName("nombreP")
        self.direccionP = QtWidgets.QLineEdit(self.centralwidget)
        self.direccionP.setGeometry(QtCore.QRect(120, 140, 161, 51))
        self.direccionP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.direccionP.setObjectName("direccionP")
        self.telefonoP = QtWidgets.QLineEdit(self.centralwidget)
        self.telefonoP.setGeometry(QtCore.QRect(120, 200, 161, 31))
        self.telefonoP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.telefonoP.setObjectName("telefonoP")
        self.correoP = QtWidgets.QLineEdit(self.centralwidget)
        self.correoP.setGeometry(QtCore.QRect(120, 240, 161, 31))
        self.correoP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.correoP.setObjectName("correoP")
        self.representanteP = QtWidgets.QLineEdit(self.centralwidget)
        self.representanteP.setGeometry(QtCore.QRect(120, 280, 161, 31))
        self.representanteP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.representanteP.setObjectName("representanteP")
        self.Limpiar = QtWidgets.QPushButton(self.centralwidget)
        self.Limpiar.setGeometry(QtCore.QRect(15, 320, 75, 23))
        self.Limpiar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Limpiar.setObjectName("Limpiar")
        self.Verificar = QtWidgets.QPushButton(self.centralwidget)
        self.Verificar.setGeometry(QtCore.QRect(115, 320, 75, 23))
        self.Verificar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Verificar.setObjectName("Verificar")
        MenuNP.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MenuNP)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 304, 21))
        self.menubar.setObjectName("menubar")
        MenuNP.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MenuNP)
        self.statusbar.setObjectName("statusbar")
        MenuNP.setStatusBar(self.statusbar)

        self.retranslateUi(MenuNP)
        #Boton Limpiar para limpiar todos los campos.
        self.Limpiar.clicked.connect(self.claveP.clear)
        self.Limpiar.clicked.connect(self.nombreP.clear)
        self.Limpiar.clicked.connect(self.direccionP.clear)
        self.Limpiar.clicked.connect(self.telefonoP.clear)
        self.Limpiar.clicked.connect(self.correoP.clear)
        self.Limpiar.clicked.connect(self.representanteP.clear)
        QtCore.QMetaObject.connectSlotsByName(MenuNP)
        #Botones programados
        #Boton que permite agregar la información a la base de datos
        self.Agregar.clicked.connect(self.LoadData)
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
                #Leer clave de proveedor que se introduce en nuestra ventana de Agregar Proveedor.
                Clave = self.claveP.text()
                #Convertir la clave a entero.Ya que en la base se tiene como Entero.
                clave = int(Clave)
                #Ejecutar una línea que nos permite obtener todas las claves guardadas en Proveedor.
                micursor.execute("SELECT Clave_Proveedor FROM Proveedor")
                #Guardar los resultados en la variable claveP
                claveP = micursor.fetchall()
                #Declarar una lista donde se guardaran las claves de proveedor.
                listaClaves = []
                #Ciclo para el unpack del resultado de claveP.
                for dato in claveP:
                    for n in dato:
                        ClaveP= int(n)
                        #Agregar cada clave a la lista de listaClaves
                        listaClaves.append(ClaveP)
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
                #Leer clave de proveedor que se introduce en nuestra ventana de Agregar Proveedor.
                Clave = self.claveP.text()
                #Convertir la clave a entero.Ya que en la base se tiene como Entero.
                clave = int(Clave)
                #Ejecutar una línea que nos permite obtener todas las claves guardadas en Proveedor.
                micursor.execute("SELECT Clave_Proveedor FROM Proveedor")
                #Guardar los resultados en la variable claveP
                claveP = micursor.fetchall()
                #Declarar una lista donde se guardaran las claves de proveedor.
                listaClaves = []
                #Ciclo para el unpack del resultado de claveP.
                for dato in claveP:
                    for n in dato:
                        ClaveP= int(n)
                        #Agregar cada clave a la lista de listaClaves
                        listaClaves.append(ClaveP)
                #ESTO ES UNA DOBLE VERIFICACIÓN YA QUE TAMBIÉN SE HACE EN LA FUNCIÓN DE AGREGAR.
                #Si la clave que introdujo el usuario esta dentro de la lista de claves.
                if clave in listaClaves:
                    #Se muestra una ventana donde avisa que la clave ya esta ocupada y que intente con otra.
                    self.ventana = QtWidgets.QMainWindow()
                    self.ui = Ui_ClaveExistente()
                    self.ui.setupUi(self.ventana)
                    self.ventana.show()
                #Si la clave del proveedor no esta dentro de la lista de claves de Proveedor,se prosigue a agregar todo. 
                else:
                    #Se lee el nombre que se introduce en la aplicación y se agrega a la variable nombre.
                    nombre = self.nombreP.text()
                    #Se lee la direccion que se introduce en la aplicación y se agrega a la variable Direccion.
                    direccion = self.direccionP.text()
                    #Se lee el telefono que se introduce en la aplicación y se agrega a la variable Telefono.
                    Telefono = self.telefonoP.text()
                    #Se cambia el valor a entero y se guarda en la variable telefono. Ya que en la base se tiene como Entero.
                    telefono = int(Telefono)
                    #Se lee el correo que se introduce en la aplicación y se agrega a la variable Correo.
                    correo = self.correoP.text()
                    #Se lee el nombre del representante que se introduce en la aplicación y se agrega a la variable Representante.
                    representante = self.representanteP.text()
                    #Guardar valores en un diccionario, con una clave que distinga cada uno.
                    valores = {"clave": clave, "nombre": nombre, "direccion": direccion, "telefono": telefono, "correo": correo,"representante":representante}
                    #Ejecutar la linea de INSERT con las llaves del diccionario valores.
                    micursor.execute("INSERT INTO Proveedor VALUES(:clave,:nombre,:direccion,:telefono,:correo,:representante)", valores)
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
    def retranslateUi(self, MenuNP):
        _translate = QtCore.QCoreApplication.translate
        MenuNP.setWindowTitle(_translate("MenuNP", "MainWindow"))
        self.label_5.setText(_translate("MenuNP", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">NUEVO PROVEEDOR</span></p></body></html>"))
        self.label.setText(_translate("MenuNP", "<html><head/><body><p align=\"center\">CLAVE</p></body></html>"))
        self.label_2.setText(_translate("MenuNP", "<html><head/><body><p align=\"center\">NOMBRE</p></body></html>"))
        self.label_3.setText(_translate("MenuNP", "<html><head/><body><p align=\"center\">DIRECCIÓN</p></body></html>"))
        self.label_4.setText(_translate("MenuNP", "<html><head/><body><p align=\"center\">TELÉFONO</p></body></html>"))
        self.label_6.setText(_translate("MenuNP", "<html><head/><body><p align=\"center\">CORREO</p></body></html>"))
        self.Agregar.setText(_translate("MenuNP", "AGREGAR"))
        self.label_7.setText(_translate("MenuNP", "<html><head/><body><p align=\"center\">REPRESENTANTE</p></body></html>"))
        self.Limpiar.setText(_translate("MenuNP", "LIMPIAR"))
        self.Verificar.setText(_translate("MenuNP", "VERIFICAR"))

#Cerrar aplicación.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MenuNP = QtWidgets.QMainWindow()
    ui = Ui_MenuNP()
    ui.setupUi(MenuNP)
    MenuNP.show()
    sys.exit(app.exec_())
