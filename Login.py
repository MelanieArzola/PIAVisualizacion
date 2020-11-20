#Importación de sql para establecer la conexión y excepciones.
import sqlite3
from sqlite3 import Error
#Importación de ventanas para conectar en las funciones.
from DatosIncorrectos import Ui_DatosIncorrectos
from Administrador import Ui_Administrador
from Contador import Ui_Contador
from Vendedor import Ui_Vendedor
#Librería para crear nuestra aplicación.
from PyQt5 import QtCore, QtGui, QtWidgets

#Creación de la aplicación. (Menú de login, donde se permite ingresar al sistema según el puesto del usuario.)
class Ui_Ventana_Login(object):
    def setupUi(self, Ventana_Login):
        Ventana_Login.setObjectName("Ventana_Login")
        Ventana_Login.resize(351, 358)
        Ventana_Login.setStyleSheet("background-color: rgb(255, 254, 230);\n"
"background-color: rgb(226, 230, 255);")
        self.centralwidget = QtWidgets.QWidget(Ventana_Login)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 100, 351, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 220, 41, 41))
        self.label_2.setStyleSheet("background-color: rgb(181, 181, 181);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 160, 41, 41))
        self.label_3.setStyleSheet("background-color: rgb(181, 181, 181);")
        self.label_3.setObjectName("label_3")
        self.Login = QtWidgets.QPushButton(self.centralwidget)
        self.Login.setGeometry(QtCore.QRect(140, 290, 75, 23))
        self.Login.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"text-decoration: underline;\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.Login.setObjectName("Login")
        self.usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.usuario.setGeometry(QtCore.QRect(80, 160, 231, 41))
        self.usuario.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.usuario.setObjectName("usuario")
        self.contra = QtWidgets.QLineEdit(self.centralwidget)
        self.contra.setGeometry(QtCore.QRect(80, 220, 231, 41))
        self.contra.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.contra.setEchoMode(QtWidgets.QLineEdit.Password)
        self.contra.setObjectName("contra")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 20, 91, 81))
        self.label_5.setObjectName("label_5")
        self.label_2.raise_()
        self.label_3.raise_()
        self.Login.raise_()
        self.label.raise_()
        self.usuario.raise_()
        self.contra.raise_()
        self.label_5.raise_()
        Ventana_Login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ventana_Login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 351, 21))
        self.menubar.setObjectName("menubar")
        Ventana_Login.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ventana_Login)
        self.statusbar.setObjectName("statusbar")
        Ventana_Login.setStatusBar(self.statusbar)

        self.retranslateUi(Ventana_Login)
        QtCore.QMetaObject.connectSlotsByName(Ventana_Login)
        #Programación de boton para verificar el login.
        self.Login.clicked.connect(self.Entrada)
     
    #Función donde sucede el login. 
    def Entrada(self):
        #Ciclo while que se utiliza para marcar error de datos
        while True:
            #Try para excepciones.
            try:
                #Leer usuario y contraseña que se introducen en nuestra ventana de Login.
                usuario = self.usuario.text()
                contra = self.contra.text()
                #Establecer conexión con nuestra base de datos.
                with sqlite3.connect("PIA_1845788.db") as conn:
                    #Establecimiento de nuestro cursor.
                    c = conn.cursor()
                    #Linea donde se busca la clave de puesto según la información otorgada por el usuario.
                    encontrarUsuario = ("SELECT Puesto FROM Trabajador WHERE Usuario = ? AND Contraseña = ?")
                    #Línea donde se ejecuta el select y se sustituyen los valores, por los valores otorgados por el usuario.
                    c.execute(encontrarUsuario,[(usuario),(contra)])
                    #Se guarda el resultado de la busqueda en una variable.
                    resultado = c.fetchall()
                    #Unpacked del resultado.
                    if resultado:
                        for i in resultado:
                            for n in i:
                                decision = int(n)
                        #Si el puesto obtenido y guardado en decision es igual a 1, se abre el menú de administrador.        
                        if decision == 1:
                            self.ventana = QtWidgets.QMainWindow()
                            self.ui = Ui_Administrador()
                            self.ui.setupUi(self.ventana)
                            self.ventana.show()
                        #Si el puesto obtenido y guardado en decision es igual a 2, se abre el menú de contador.  
                        elif decision == 2:
                            self.ventana = QtWidgets.QMainWindow()
                            self.ui = Ui_Contador()
                            self.ui.setupUi(self.ventana)
                            self.ventana.show()
                        #Si el puesto obtenido y guardado en decision es igual a 3, se abre el menú de vendedor.  
                        elif decision ==3:
                            self.ventana = QtWidgets.QMainWindow()
                            self.ui = Ui_Vendedor()
                            self.ui.setupUi(self.ventana)
                            self.ventana.show()
                    #Si los datos introducidos, no coinciden con los datos en la base de datos, se muestra una ventana con aviso de datos incorrectos.
                    else:
                        self.ventana = QtWidgets.QMainWindow()
                        self.ui = Ui_DatosIncorrectos()
                        self.ui.setupUi(self.ventana)
                        self.ventana.show()
                    #Break para salir del ciclo.
                    break
            #Excepcion con error de sqlite3.
            except Error as e:
                print(e)
    
    #Asignación de texto a los botones.
    def retranslateUi(self, Ventana_Login):
        _translate = QtCore.QCoreApplication.translate
        Ventana_Login.setWindowTitle(_translate("Ventana_Login", "MainWindow"))
        self.label.setText(_translate("Ventana_Login", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">BIENVENIDO</span></p></body></html>"))
        self.label_2.setText(_translate("Ventana_Login", "<html><head/><body><p><img src=\":/SamBigotes/password.png\"/></p></body></html>"))
        self.label_3.setText(_translate("Ventana_Login", "<html><head/><body><p><img src=\":/SamBigotes/usuario.png\"/></p></body></html>"))
        self.Login.setText(_translate("Ventana_Login", "LOGIN"))
        self.label_5.setText(_translate("Ventana_Login", "<html><head/><body><p><img src=\":/SamBigotes/Sam.png\"/></p></body></html>"))

#Importacion de las imagenes utilizadas en la ventana de Login.
import imagenesLogin_rc

#Cerrar aplicación.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ventana_Login = QtWidgets.QMainWindow()
    ui = Ui_Ventana_Login()
    ui.setupUi(Ventana_Login)
    Ventana_Login.show()
    sys.exit(app.exec_())
