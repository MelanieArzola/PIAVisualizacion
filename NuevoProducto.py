#Importación de sql para establecer la conexión y excepciones.
import sqlite3
from sqlite3 import Error
#Importación de ventanas para conectar en las funciones.
from DatosAgregados import Ui_DatosAgregados
from ClaveExistente import Ui_ClaveExistente
from ClaveInexistente import Ui_ClaveInexistente
from ClaveInexistenteProveedor import Ui_ClaveInexistenteProveedor
from Alerta import Ui_Alerta
#Librería para crear nuestra aplicación.
from PyQt5 import QtCore, QtGui, QtWidgets

#Creación de la aplicación. (Menú de producto donde se introducen los datos del producto a agregar.)
class Ui_AgregarProducto(object):
    def setupUi(self, AgregarProducto):
        AgregarProducto.setObjectName("AgregarProducto")
        AgregarProducto.resize(312, 344)
        AgregarProducto.setStyleSheet("background-color: rgb(226, 230, 255);")
        self.centralwidget = QtWidgets.QWidget(AgregarProducto)
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
        self.label_3.setGeometry(QtCore.QRect(20, 150, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 190, 101, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 230, 101, 20))
        self.label_7.setObjectName("label_7")
        self.ClaveP = QtWidgets.QLineEdit(self.centralwidget)
        self.ClaveP.setGeometry(QtCore.QRect(130, 60, 161, 31))
        self.ClaveP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ClaveP.setObjectName("ClaveP")
        self.Nombre = QtWidgets.QLineEdit(self.centralwidget)
        self.Nombre.setGeometry(QtCore.QRect(130, 100, 161, 31))
        self.Nombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Nombre.setObjectName("Nombre")
        self.Precio = QtWidgets.QLineEdit(self.centralwidget)
        self.Precio.setGeometry(QtCore.QRect(130, 140, 161, 31))
        self.Precio.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Precio.setObjectName("Precio")
        self.Inventario = QtWidgets.QLineEdit(self.centralwidget)
        self.Inventario.setGeometry(QtCore.QRect(130, 180, 161, 31))
        self.Inventario.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Inventario.setObjectName("Inventario")
        self.Proveedor = QtWidgets.QLineEdit(self.centralwidget)
        self.Proveedor.setGeometry(QtCore.QRect(130, 220, 161, 31))
        self.Proveedor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Proveedor.setObjectName("Proveedor")
        self.Verificar = QtWidgets.QPushButton(self.centralwidget)
        self.Verificar.setGeometry(QtCore.QRect(120, 271, 75, 23))
        self.Verificar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Verificar.setObjectName("Verificar")
        self.Limpiar = QtWidgets.QPushButton(self.centralwidget)
        self.Limpiar.setGeometry(QtCore.QRect(20, 271, 75, 23))
        self.Limpiar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Limpiar.setObjectName("Limpiar")
        self.Agregar = QtWidgets.QPushButton(self.centralwidget)
        self.Agregar.setGeometry(QtCore.QRect(220, 270, 75, 23))
        self.Agregar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Agregar.setObjectName("Agregar")
        AgregarProducto.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AgregarProducto)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 312, 21))
        self.menubar.setObjectName("menubar")
        AgregarProducto.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AgregarProducto)
        self.statusbar.setObjectName("statusbar")
        AgregarProducto.setStatusBar(self.statusbar)

        self.retranslateUi(AgregarProducto)
        #Boton Limpiar para limpiar todos los campos.
        self.Limpiar.clicked.connect(self.ClaveP.clear)
        self.Limpiar.clicked.connect(self.Nombre.clear)
        self.Limpiar.clicked.connect(self.Precio.clear)
        self.Limpiar.clicked.connect(self.Inventario.clear)
        self.Limpiar.clicked.connect(self.Proveedor.clear)
        QtCore.QMetaObject.connectSlotsByName(AgregarProducto)
        #Botones programados
        #Boton que permite agregar la información a la base de datos.
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
                    #Leer clave de producto que se introduce en nuestra ventana de Agregar Producto.
                    Clave = self.ClaveP.text()
                    #Convertir la clave a entero.Ya que en la base se tiene como Entero.
                    clave = int(Clave)
                    #Ejecutar una línea que nos permite obtener todas las claves guardadas en Producto
                    micursor.execute("SELECT Clave_Producto FROM Producto")
                    #Guardar los resultados en la variable claveP
                    claveP = micursor.fetchall()
                    #Declarar una lista donde se guardaran las claves de producto.
                    listaClaves = []
                    #Ciclo para el unpack del resultado de claveP.
                    for dato in claveP:
                        for n in dato:
                            ClaveP= int(n)
                            #Agregar cada clave a la lista de listaClaves.
                            listaClaves.append(ClaveP)
                    #Leer clave de proveedor que se introduce en nuestra ventana de Agregar Producto.
                    ClaveP = self.Proveedor.text()
                    #Convertir la clave a entero.Ya que en la base se tiene como Entero.
                    clavePro = int(ClaveP)
                    #Ejecutar una línea que nos permite obtener todas las claves guardadas en Proveedor
                    micursor.execute("SELECT Clave_Proveedor FROM Proveedor")
                    #Guardar los resultados en la variable clavePro
                    ClavePro = micursor.fetchall()
                    #Declarar una lista donde se guardaran las claves de proveedores.
                    listaClavesP = []
                    #Ciclo para el unpack del resultado de clavePro
                    for dato in ClavePro:
                        for n in dato:
                            clavepro= int(n)
                            #Agregar cada clave a la lista de listaClavesP.
                            listaClavesP.append(clavepro)        
                    #ESTO ES UNA DOBLE VERIFICACIÓN YA QUE TAMBIÉN SE HACE EN LA FUNCIÓN DE AGREGAR.
                    #Si la clave que introdujo el usuario esta dentro de la lista de claves.
                    if clave in listaClaves:
                        #Se muestra una ventana donde avisa que la clave ya esta ocupada y que intente con otra.
                        self.ventana = QtWidgets.QMainWindow()
                        self.ui = Ui_ClaveExistente()
                        self.ui.setupUi(self.ventana)
                        self.ventana.show()
                    #Si la clave que introdujo el usuario en la clave proveedor NO existe muestra el siguiente mensaje.
                    elif clavePro not in listaClavesP:
                        #Ventana donde muestra que la clave de proveedor es inexistente, por lo tanto NO puede proseguir.
                        self.ventana = QtWidgets.QMainWindow()
                        self.ui = Ui_ClaveInexistenteProveedor()
                        self.ui.setupUi(self.ventana)
                        self.ventana.show()
                    #Si la clave del producto no esta dentro de la lista de claves de Productos.
                    elif clave not in listaClaves:
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
    
    #Función para leer y agregar los datos a la base.
    def LoadData(self):
        try:
            #Conexión a la base de datos
            with sqlite3.connect("PIA_1845788.db") as conn:
                #Definir nuestro cursor.
                micursor = conn.cursor()
                #Leer clave de producto que se introduce en nuestra ventana de Agregar Producto.
                Clave = self.ClaveP.text()
                #Convertir la clave a entero.Ya que en la base se tiene como Entero.
                clave = int(Clave)
                #Ejecutar una línea que nos permite obtener todas las claves guardadas en Producto
                micursor.execute("SELECT Clave_Producto FROM Producto")
                #Guardar los resultados en la variable claveP
                claveP = micursor.fetchall()
                #Declarar una lista donde se guardaran las claves de producto.
                listaClaves = []
                #Ciclo para el unpack del resultado de claveP.
                for dato in claveP:
                    for n in dato:
                        ClaveP= int(n)
                        #Agregar cada clave a la lista de listaClaves.
                        listaClaves.append(ClaveP)
                #Leer clave de proveedor que se introduce en nuestra ventana de Agregar Producto.
                ClaveP = self.Proveedor.text()
                #Convertir la clave a entero.Ya que en la base se tiene como Entero.
                clavePro = int(ClaveP)
                #Ejecutar una línea que nos permite obtener todas las claves guardadas en Proveedor
                micursor.execute("SELECT Clave_Proveedor FROM Proveedor")
                #Guardar los resultados en la variable clavePro
                ClavePro = micursor.fetchall()
                #Declarar una lista donde se guardaran las claves de proveedores.
                listaClavesP = []
                #Ciclo para el unpack del resultado de clavePro
                for dato in ClavePro:
                    for n in dato:
                        clavepro= int(n)
                        #Agregar cada clave a la lista de listaClavesP.
                        listaClavesP.append(clavepro)        
                #ESTO ES UNA DOBLE VERIFICACIÓN YA QUE TAMBIÉN SE HACE EN LA FUNCIÓN DE VERIFICAR.
                #Si la clave que introdujo el usuario esta dentro de la lista de claves.
                if clave in listaClaves:
                    #Se muestra una ventana donde avisa que la clave ya esta ocupada y que intente con otra.
                    self.ventana = QtWidgets.QMainWindow()
                    self.ui = Ui_ClaveExistente()
                    self.ui.setupUi(self.ventana)
                    self.ventana.show()
                #Si la clave que introdujo el usuario en la clave proveedor NO existe muestra el siguiente mensaje.
                elif clavePro not in listaClavesP:
                    #Ventana donde muestra que la clave de proveedor es inexistente, por lo tanto NO puede proseguir.
                    self.ventana = QtWidgets.QMainWindow()
                    self.ui = Ui_ClaveInexistenteProveedor()
                    self.ui.setupUi(self.ventana)
                    self.ventana.show()
                #Si la clave del producto no esta dentro de la lista de claves de Productos.
                elif clave not in listaClaves:
                    #Se lee el nombre que se introduce en la aplicación y se agrega a la variable nombre.
                    nombre = self.Nombre.text()
                    #Se lee el precio que se introduce en la aplicación y se agrega a la variable Precio.
                    Precio = self.Precio.text()
                    #Se cambia el valor a float y se guarda en la variable precio. Ya que en la base se tiene como float.
                    precio = float(Precio)
                    #Se lee el inventario que se introduce en la aplicación y se agrega a la variable Inventario.
                    Inventario = self.Inventario.text()
                    #Se cambia el valor a entero y se guarda en la variable inventario. Ya que en la base se tiene como Entero.
                    inventario = int(Inventario)
                    #Se lee la clave que se introduce en la aplicación y se agrega a la variable Proveedor.
                    Proveedor = self.Proveedor.text()
                    #Se cambia el valor a entero y se guarda en la variable proveedor. Ya que en la base se tiene como Entero.
                    proveedor = int(Proveedor)
                    #Guardar valores en un diccionario, con una clave que distinga cada uno.
                    valores = {"clave": clave, "nombre": nombre, "precio": precio, "inventario": inventario,"proveedor":proveedor}
                    #Ejecutar la linea de INSERT con las llaves del diccionario valores.
                    micursor.execute("INSERT INTO Producto VALUES(:clave,:nombre,:precio,:inventario,:proveedor)", valores)
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
    def retranslateUi(self, AgregarProducto):
        _translate = QtCore.QCoreApplication.translate
        AgregarProducto.setWindowTitle(_translate("AgregarProducto", "MainWindow"))
        self.label_5.setText(_translate("AgregarProducto", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">NUEVO PRODUCTO</span></p></body></html>"))
        self.label.setText(_translate("AgregarProducto", "<html><head/><body><p align=\"center\">CLAVE</p></body></html>"))
        self.label_2.setText(_translate("AgregarProducto", "<html><head/><body><p align=\"center\">NOMBRE</p></body></html>"))
        self.label_3.setText(_translate("AgregarProducto", "<html><head/><body><p align=\"center\">PRECIO</p></body></html>"))
        self.label_6.setText(_translate("AgregarProducto", "<html><head/><body><p align=\"center\">INVENTARIO</p></body></html>"))
        self.label_7.setText(_translate("AgregarProducto", "<html><head/><body><p align=\"center\">PROVEEDOR</p></body></html>"))
        self.Verificar.setText(_translate("AgregarProducto", "VERIFICAR"))
        self.Limpiar.setText(_translate("AgregarProducto", "LIMPIAR"))
        self.Agregar.setText(_translate("AgregarProducto", "AGREGAR"))

#Cerrar aplicación.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AgregarProducto = QtWidgets.QMainWindow()
    ui = Ui_AgregarProducto()
    ui.setupUi(AgregarProducto)
    AgregarProducto.show()
    sys.exit(app.exec_())
