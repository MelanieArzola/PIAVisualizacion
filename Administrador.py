#Importación de ventanas para conectar en las funciones.
from Proveedor import Ui_Proveedores
from Clientes import Ui_Clientes
from Trabajador import Ui_Trabajadores
from Productos import Ui_Productos
#Librería para crear nuestra aplicación.
from PyQt5 import QtCore, QtGui, QtWidgets

#Creación de la aplicación. (Menú del administrador)
class Ui_Administrador(object):
    def setupUi(self, Administrador):
        Administrador.setObjectName("Administrador")
        Administrador.resize(464, 130)
        Administrador.setStyleSheet("background-color: rgb(226, 230, 255);")
        self.centralwidget = QtWidgets.QWidget(Administrador)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 461, 31))
        self.label.setObjectName("label")
        self.BProveedores = QtWidgets.QPushButton(self.centralwidget)
        self.BProveedores.setGeometry(QtCore.QRect(30, 70, 80, 23))
        self.BProveedores.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BProveedores.setObjectName("BProveedores")
        self.BClientes = QtWidgets.QPushButton(self.centralwidget)
        self.BClientes.setGeometry(QtCore.QRect(140, 70, 75, 23))
        self.BClientes.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BClientes.setObjectName("BClientes")
        self.BTrabajadores = QtWidgets.QPushButton(self.centralwidget)
        self.BTrabajadores.setGeometry(QtCore.QRect(250, 70, 85, 23))
        self.BTrabajadores.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BTrabajadores.setObjectName("BTrabajadores")
        self.BProductos = QtWidgets.QPushButton(self.centralwidget)
        self.BProductos.setGeometry(QtCore.QRect(360, 70, 75, 23))
        self.BProductos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BProductos.setObjectName("BProductos")
        Administrador.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Administrador)
        self.statusbar.setObjectName("statusbar")
        Administrador.setStatusBar(self.statusbar)

        self.retranslateUi(Administrador)
        QtCore.QMetaObject.connectSlotsByName(Administrador)
        #PROGRAMACIÓN DE BOTONES PARA CONECTAR A LAS FUNCIONES
        
        #Boton programado para conectar a la función Proveedores, la cual nos permitira entrar a su menú.
        self.BProveedores.clicked.connect(self.Proveedores)
        #Boton programado para conectar a la función Clientes, la cual nos permitira entrar a su menú.
        self.BClientes.clicked.connect(self.Clientes)
        #Boton programado para conectar a la función Trabajadores, la cual nos permitira entrar a su menú.
        self.BTrabajadores.clicked.connect(self.Trabajadores)
        #Boton programado para conectar a la función Productos, la cual nos permitira entrar a su menú.
        self.BProductos.clicked.connect(self.Productos)

    #Función que conecta al menú proveedores.
    def Proveedores(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_Proveedores()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
    
    #Función que conecta al menú clientes.
    def Clientes(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_Clientes()
        self.ui.setupUi(self.ventana)
        self.ventana.show()    
    
    #Función que conecta al menú trabajadores.
    def Trabajadores(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_Trabajadores()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        
    #Función que conecta al menú productos.
    def Productos(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_Productos()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        
    #Asignación de texto a los botones.
    def retranslateUi(self, Administrador):
        _translate = QtCore.QCoreApplication.translate
        Administrador.setWindowTitle(_translate("Administrador", "MainWindow"))
        self.label.setText(_translate("Administrador", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">MENÚ PRINCIPAL</span></p></body></html>"))
        self.BProveedores.setText(_translate("Administrador", "PROVEEDORES"))
        self.BClientes.setText(_translate("Administrador", "CLIENTES"))
        self.BTrabajadores.setText(_translate("Administrador", "TRABAJADORES"))
        self.BProductos.setText(_translate("Administrador", "PRODUCTOS"))

#Cerrar aplicación.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Administrador = QtWidgets.QMainWindow()
    ui = Ui_Administrador()
    ui.setupUi(Administrador)
    Administrador.show()
    sys.exit(app.exec_())
