#Importación de sql para establecer la conexión y excepciones.
import sqlite3
from sqlite3 import Error
#Importación de ventanas para conectar en las funciones.
from DatosEliminados import Ui_DatosEliminados
from ClaveInexistenteEP import Ui_ClaveInexistenteEP
from Alerta import Ui_Alerta
#Librería para crear nuestra aplicación.
from PyQt5 import QtCore, QtGui, QtWidgets

#Creación de la aplicación. (Menú de proveedores donde se introduce la clave a eliminar.)
class Ui_MenuEP(object):
    def setupUi(self, MenuEP):
        MenuEP.setObjectName("MenuEP")
        MenuEP.resize(304, 431)
        MenuEP.setStyleSheet("background-color: rgb(226, 230, 255);")
        self.centralwidget = QtWidgets.QWidget(MenuEP)
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
        self.label_4.setGeometry(QtCore.QRect(20, 220, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 270, 81, 16))
        self.label_6.setObjectName("label_6")
        self.Eliminar = QtWidgets.QPushButton(self.centralwidget)
        self.Eliminar.setGeometry(QtCore.QRect(215, 360, 75, 23))
        self.Eliminar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Eliminar.setObjectName("Eliminar")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 320, 81, 16))
        self.label_7.setObjectName("label_7")
        self.Nombre = QtWidgets.QTextBrowser(self.centralwidget)
        self.Nombre.setGeometry(QtCore.QRect(120, 100, 161, 31))
        self.Nombre.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.Nombre.setObjectName("Nombre")
        self.Direccion = QtWidgets.QTextBrowser(self.centralwidget)
        self.Direccion.setGeometry(QtCore.QRect(120, 140, 161, 61))
        self.Direccion.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.Direccion.setObjectName("Direccion")
        self.Telefono = QtWidgets.QTextBrowser(self.centralwidget)
        self.Telefono.setGeometry(QtCore.QRect(120, 210, 161, 31))
        self.Telefono.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.Telefono.setObjectName("Telefono")
        self.Correo = QtWidgets.QTextBrowser(self.centralwidget)
        self.Correo.setGeometry(QtCore.QRect(120, 260, 161, 31))
        self.Correo.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.Correo.setObjectName("Correo")
        self.Representante = QtWidgets.QTextBrowser(self.centralwidget)
        self.Representante.setGeometry(QtCore.QRect(120, 310, 161, 31))
        self.Representante.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.Representante.setObjectName("Representante")
        self.claveP = QtWidgets.QLineEdit(self.centralwidget)
        self.claveP.setGeometry(QtCore.QRect(120, 60, 161, 31))
        self.claveP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.claveP.setObjectName("claveP")
        self.Limpiar = QtWidgets.QPushButton(self.centralwidget)
        self.Limpiar.setGeometry(QtCore.QRect(15, 360, 75, 23))
        self.Limpiar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Limpiar.setObjectName("Limpiar")
        self.Cargar = QtWidgets.QPushButton(self.centralwidget)
        self.Cargar.setGeometry(QtCore.QRect(115, 360, 75, 23))
        self.Cargar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Cargar.setObjectName("Cargar")
        MenuEP.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MenuEP)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 304, 21))
        self.menubar.setObjectName("menubar")
        MenuEP.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MenuEP)
        self.statusbar.setObjectName("statusbar")
        MenuEP.setStatusBar(self.statusbar)

        self.retranslateUi(MenuEP)
        #Boton Limpiar para limpiar todos los campos.
        self.Limpiar.clicked.connect(self.Representante.clear)
        self.Limpiar.clicked.connect(self.Correo.clear)
        self.Limpiar.clicked.connect(self.Telefono.clear)
        self.Limpiar.clicked.connect(self.Direccion.clear)
        self.Limpiar.clicked.connect(self.Nombre.clear)
        self.Limpiar.clicked.connect(self.claveP.clear)
        QtCore.QMetaObject.connectSlotsByName(MenuEP)
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
                #Leer clave de producto que se introduce en nuestra ventana de Eliminar Proveedor.
                Clave = self.claveP.text()
                #Convertir la clave a entero.
                clave = int(Clave)
                #Definir nuestro cursor.
                mi_cursor = conn.cursor()
                #Ejecutar una línea que nos permite obtener todas las claves guardadas en Proveedor.
                c= mi_cursor.execute("SELECT Clave_Proveedor FROM Proveedor")
                #Guardar los resultados en la variable claves.
                claves = mi_cursor.fetchall()
                #Declarar una lista donde se guardaran las claves de proveedores.
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
                    mi_cursor.execute("DELETE FROM Proveedor WHERE Clave_Proveedor = (:clave)",valor)
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
                #Leer clave de producto que se introduce en nuestra ventana de Eliminar Proveedor.
                Clave = self.claveP.text()
                #Convertir la clave a entero.
                clave = int(Clave)
                #Definir nuestro cursor.
                mi_cursor = conn.cursor()
                #Guardar la clave en el diccionario valor, para posteriormente utilizarlo.
                valor = {"clave":clave}
                #Ejecutar una línea que nos permite obtener todas las claves guardadas en proveedor.
                c= mi_cursor.execute("SELECT Clave_Proveedor FROM Proveedor")
                #Guardar los resultados en la variable claves.
                claves = mi_cursor.fetchall()
                #Declarar una lista donde se guardaran las claves de proveedores.
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
                    #Buscar nombre del proveedor en la base de datos según la clave dada por el usuario y mostrarlo.
                    c = mi_cursor.execute("SELECT Nombre FROM Proveedor WHERE Clave_Proveedor = (:clave)",valor)
                    #Guardar el resultado en la variable nombre.
                    nombre = mi_cursor.fetchall()
                    #Ciclo para el unpack del resultado de nombre.
                    for dato in nombre:
                        for n in dato:
                            Nombre = str(n)
                    #Asignar al campo Nombre el valor de Nombre que se obtuvo anteriormente.
                    self.Nombre.setText(Nombre)
                    
                    #Buscar direccion del proveedor en la base de datos según la clave dada por el usuario y mostrarlo.
                    c = mi_cursor.execute("SELECT Dirección FROM Proveedor WHERE Clave_Proveedor = (:clave)",valor)
                    #Guardar el resultado en la variable dirección.
                    dirección = mi_cursor.fetchall()
                    #Ciclo para el unpack del resultado de dirección.
                    for dato in dirección:
                        for n in dato:
                            dire = str(n)
                    #Asignar al campo Direccion el valor de dire que se obtuvo anteriormente.
                    self.Direccion.setText(dire)
                    
                    #Buscar telefono del proveedor en la base de datos según la clave dada por el usuario y mostrarlo.
                    c = mi_cursor.execute("SELECT Teléfono FROM Proveedor WHERE Clave_Proveedor = (:clave)",valor)
                    #Guardar el resultado en la variable telefono.
                    telefono = mi_cursor.fetchall()
                    #Ciclo para el unpack del resultado de telefono.
                    for dato in telefono:
                        for n in dato:
                            tel = str(n)
                    #Asignar al campo Telefono el valor de tel que se obtuvo anteriormente. 
                    self.Telefono.setText(tel)
                    
                    #Buscar correo del proveedor en la base de datos según la clave dada por el usuario y mostrarlo.
                    c = mi_cursor.execute("SELECT Correo FROM Proveedor WHERE Clave_Proveedor = (:clave)",valor)
                    #Guardar el resultado en la variable correo.
                    correo = mi_cursor.fetchall()
                    #Ciclo para el unpack del resultado de correo.
                    for dato in correo:
                        for n in dato:
                            Correo = str(n)
                    #Asignar al campo Correo el valor de Correo que se obtuvo anteriormente. 
                    self.Correo.setText(Correo)
                    
                    #Buscar representante del proveedor en la base de datos según la clave dada por el usuario y mostrarlo.
                    c = mi_cursor.execute("SELECT Representante FROM Proveedor WHERE Clave_Proveedor = (:clave)",valor)
                    #Guardar el resultado en la variable representante.
                    representante= mi_cursor.fetchall()
                    #Ciclo para el unpack del resultado de representante.
                    for dato in representante:
                        for n in dato:
                            Representante = str(n)
                    #Asignar al campo Representante el valor de Representante que se obtuvo anteriormente.
                    self.Representante.setText(Representante)
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
    def retranslateUi(self, MenuEP):
        _translate = QtCore.QCoreApplication.translate
        MenuEP.setWindowTitle(_translate("MenuEP", "MainWindow"))
        self.label_5.setText(_translate("MenuEP", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">ELIMINAR PROVEEDOR</span></p></body></html>"))
        self.label.setText(_translate("MenuEP", "<html><head/><body><p align=\"center\">CLAVE</p></body></html>"))
        self.label_2.setText(_translate("MenuEP", "<html><head/><body><p align=\"center\">NOMBRE</p></body></html>"))
        self.label_3.setText(_translate("MenuEP", "<html><head/><body><p align=\"center\">DIRECCIÓN</p></body></html>"))
        self.label_4.setText(_translate("MenuEP", "<html><head/><body><p align=\"center\">TELÉFONO</p></body></html>"))
        self.label_6.setText(_translate("MenuEP", "<html><head/><body><p align=\"center\">CORREO</p></body></html>"))
        self.Eliminar.setText(_translate("MenuEP", "ELIMINAR"))
        self.label_7.setText(_translate("MenuEP", "<html><head/><body><p align=\"center\">REPRESENTANTE</p></body></html>"))
        self.Limpiar.setText(_translate("MenuEP", "LIMPIAR"))
        self.Cargar.setText(_translate("MenuEP", "CARGAR"))

#Cerrar aplicación.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MenuEP = QtWidgets.QMainWindow()
    ui = Ui_MenuEP()
    ui.setupUi(MenuEP)
    MenuEP.show()
    sys.exit(app.exec_())