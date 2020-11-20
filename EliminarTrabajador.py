#Importación de sql para establecer la conexión y excepciones.
import sqlite3
from sqlite3 import Error
#Importación de ventanas para conectar en las funciones.
from DatosEliminados import Ui_DatosEliminados
from ClaveInexistenteEP import Ui_ClaveInexistenteEP
from Alerta import Ui_Alerta
#Librería para crear nuestra aplicación.
from PyQt5 import QtCore, QtGui, QtWidgets

#Creación de la aplicación. (Menú de trabajador donde se introduce la clave a eliminar.)
class Ui_EliminarTrabajador(object):
    def setupUi(self, EliminarTrabajador):
        EliminarTrabajador.setObjectName("EliminarTrabajador")
        EliminarTrabajador.resize(292, 500)
        EliminarTrabajador.setStyleSheet("background-color: rgb(226, 230, 255);")
        self.centralwidget = QtWidgets.QWidget(EliminarTrabajador)
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
        self.label_4.setGeometry(QtCore.QRect(20, 270, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 150, 101, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 190, 101, 20))
        self.label_7.setObjectName("label_7")
        self.Nombre = QtWidgets.QTextBrowser(self.centralwidget)
        self.Nombre.setGeometry(QtCore.QRect(120, 100, 161, 31))
        self.Nombre.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.Nombre.setObjectName("Nombre")
        self.Telefono = QtWidgets.QTextBrowser(self.centralwidget)
        self.Telefono.setGeometry(QtCore.QRect(120, 260, 161, 31))
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
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 230, 81, 16))
        self.label_8.setObjectName("label_8")
        self.FechaIngreso = QtWidgets.QTextBrowser(self.centralwidget)
        self.FechaIngreso.setGeometry(QtCore.QRect(120, 220, 161, 31))
        self.FechaIngreso.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.FechaIngreso.setObjectName("FechaIngreso")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 350, 81, 16))
        self.label_9.setObjectName("label_9")
        self.Contra = QtWidgets.QTextBrowser(self.centralwidget)
        self.Contra.setGeometry(QtCore.QRect(120, 340, 161, 31))
        self.Contra.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.Contra.setObjectName("Contra")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 390, 81, 16))
        self.label_10.setObjectName("label_10")
        self.Puesto = QtWidgets.QTextBrowser(self.centralwidget)
        self.Puesto.setGeometry(QtCore.QRect(120, 380, 161, 31))
        self.Puesto.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.Puesto.setObjectName("Puesto")
        self.claveT = QtWidgets.QLineEdit(self.centralwidget)
        self.claveT.setGeometry(QtCore.QRect(120, 60, 161, 31))
        self.claveT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.claveT.setObjectName("claveT")
        self.Usuario = QtWidgets.QTextBrowser(self.centralwidget)
        self.Usuario.setGeometry(QtCore.QRect(120, 300, 161, 31))
        self.Usuario.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.Usuario.setObjectName("Usuario")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 310, 81, 16))
        self.label_11.setObjectName("label_11")
        self.Limpiar = QtWidgets.QPushButton(self.centralwidget)
        self.Limpiar.setGeometry(QtCore.QRect(20, 430, 75, 23))
        self.Limpiar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Limpiar.setObjectName("Limpiar")
        self.Eliminar = QtWidgets.QPushButton(self.centralwidget)
        self.Eliminar.setGeometry(QtCore.QRect(200, 429, 75, 23))
        self.Eliminar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Eliminar.setObjectName("Eliminar")
        self.Cargar = QtWidgets.QPushButton(self.centralwidget)
        self.Cargar.setGeometry(QtCore.QRect(110, 430, 75, 23))
        self.Cargar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Cargar.setObjectName("Cargar")
        EliminarTrabajador.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EliminarTrabajador)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 292, 21))
        self.menubar.setObjectName("menubar")
        EliminarTrabajador.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EliminarTrabajador)
        self.statusbar.setObjectName("statusbar")
        EliminarTrabajador.setStatusBar(self.statusbar)

        self.retranslateUi(EliminarTrabajador)
        #Boton Limpiar para limpiar todos los campos.
        self.Limpiar.clicked.connect(self.claveT.clear)
        self.Limpiar.clicked.connect(self.Nombre.clear)
        self.Limpiar.clicked.connect(self.ApellidoP.clear)
        self.Limpiar.clicked.connect(self.ApellidoM.clear)
        self.Limpiar.clicked.connect(self.FechaIngreso.clear)
        self.Limpiar.clicked.connect(self.Telefono.clear)
        self.Limpiar.clicked.connect(self.Usuario.clear)
        self.Limpiar.clicked.connect(self.Contra.clear)
        self.Limpiar.clicked.connect(self.Puesto.clear)
        QtCore.QMetaObject.connectSlotsByName(EliminarTrabajador)
        #Botones programados
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
                #Leer clave de producto que se introduce en nuestra ventana de Eliminar Trabajador.
                Clave = self.claveT.text()
                #Convertir la clave a entero.
                clave = int(Clave)
                #Definir nuestro cursor.
                mi_cursor = conn.cursor()
                #Ejecutar una línea que nos permite obtener todas las claves guardadas en trabajador.
                c= mi_cursor.execute("SELECT Clave_Trabajador FROM Trabajador")
                #Guardar los resultados en la variable claves.
                claves = mi_cursor.fetchall()
                #Declarar una lista donde se guardaran las claves de trabajadores.
                ClaveT = []
                #Ciclo para el unpack del resultado de claves.
                for dato in claves:
                    for n in dato:
                        CLAVET = int(n)
                        #Agregar cada clave en la lista ClaveP.
                        ClaveT.append(CLAVET)        
                
                #ESTO ES UNA DOBLE VERIFICACIÓN YA QUE TAMBIÉN SE HACE EN LA FUNCIÓN DE VERIFICAR.
                #Si la clave que introdujo el usuario esta dentro de la lista de claves.
                if clave in ClaveT:
                    #Guardar la clave en el diccionario valor, para posteriormente utilizarlo.
                    valor = {"clave":clave}
                    #Ejecutar la linea donde se elimina toda la información guardada con la clave que el usuario otorgo.
                    mi_cursor.execute("DELETE FROM Trabajador WHERE Clave_Trabajador= (:clave)",valor)
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
                #Leer clave de producto que se introduce en nuestra ventana de Eliminar Trabajador.
                Clave = self.claveT.text()
                #Convertir la clave a entero.
                clave = int(Clave)
                #Definir nuestro cursor.
                mi_cursor = conn.cursor()
                #Ejecutar una línea que nos permite obtener todas las claves guardadas en Trabajador.
                c= mi_cursor.execute("SELECT Clave_Trabajador FROM Trabajador")
                #Guardar los resultados en la variable claves.
                claves = mi_cursor.fetchall()
                #Declarar una lista donde se guardaran las claves de trabajador.
                ClaveT = []
                #Ciclo para el unpack del resultado de claves.
                for dato in claves:
                    for n in dato:
                        CLAVET = int(n)
                        #Agregar cada clave a la lista de Claves.
                        ClaveT.append(CLAVET)        
                #ESTO ES UNA DOBLE VERIFICACIÓN YA QUE TAMBIÉN SE HACE EN LA FUNCIÓN DE ELIMINAR.
                #Si la clave que introdujo el usuario esta dentro de la lista de claves.
                if clave in ClaveT:
                    #Guardar la clave en el diccionario valor, para posteriormente utilizarlo.
                    valor = {"clave":clave}
                    
                    #Buscar nombre del trabajador en la base de datos según la clave dada por el usuario y mostrarlo.
                    c = mi_cursor.execute("SELECT Nombre FROM Trabajador WHERE Clave_Trabajador = (:clave)",valor)
                    #Guardar el resultado en la variable de nombre.
                    nombre = mi_cursor.fetchall()
                    #Ciclo para el unpack del resultado de nombre.
                    for dato in nombre:
                        for n in dato:
                            Nombre = str(n)
                    #Asignar al campo de Nombre el valor de Nombre que se obtuvo anteriormente.
                    self.Nombre.setText(Nombre)
                    
                    #Buscar el apellido paterno del trabajador en la base de datos según la clave dada por el usuario y mostrarlo.
                    c = mi_cursor.execute("SELECT ApellidoPaterno FROM Trabajador WHERE Clave_Trabajador = (:clave)",valor)
                    #Guardar el resultado en la variable de apP.
                    apP = mi_cursor.fetchall()
                    #Ciclo para el unpack del resultado de apP.
                    for dato in apP:
                        for n in dato:
                            paterno = str(n)
                    #Asignar al campo de ApellidoP el valor de paterno que se obtuvo anteriormente.
                    self.ApellidoP.setText(paterno)
                    
                    #Buscar el apellido materno del trabajador en la base de datos según la clave dada por el usuario y mostrarlo.
                    c = mi_cursor.execute("SELECT ApellidoMaterno FROM Trabajador WHERE Clave_Trabajador = (:clave)",valor)
                    #Guardar el resultado en la variable de apM.
                    apM = mi_cursor.fetchall()
                    #Ciclo para el unpack del resultado de apM.
                    for dato in apM:
                        for n in dato:
                            materno = str(n)
                    #Asignar al campo de ApellidoM el valor de materno que se obtuvo anteriormente.        
                    self.ApellidoM.setText(materno)
                    
                    #Buscar la fecha de ingreso del trabajador en la base de datos según la clave dada por el usuario y mostrarlo.
                    c = mi_cursor.execute("SELECT Fecha_Ingreso FROM Trabajador WHERE Clave_Trabajador = (:clave)",valor)
                    #Guardar el resultado en la variable de fI.
                    fI = mi_cursor.fetchall()
                    #Ciclo para el unpack del resultado de fI.
                    for dato in fI:
                        for n in dato:
                            fechaIngreso = str(n)
                    #Asignar al campo de FechaIngreso el valor de fechaIngreso que se obtuvo anteriormente. 
                    self.FechaIngreso.setText(fechaIngreso)
                    
                    #Buscar el telefono del trabajador en la base de datos según la clave dada por el usuario y mostrarlo.
                    c = mi_cursor.execute("SELECT Telefono FROM Trabajador WHERE Clave_Trabajador = (:clave)",valor)
                    #Guardar el resultado en la variable de tel.
                    tel = mi_cursor.fetchall()
                    #Ciclo para el unpack del resultado de tel.
                    for dato in tel:
                        for n in dato:
                            Telefono = str(n)
                    #Asignar al campo de Telefono el valor de Telefono que se obtuvo anteriormente. 
                    self.Telefono.setText(Telefono)
                    
                    #Buscar el usuario del trabajador en la base de datos según la clave dada por el usuario y mostrarlo.
                    c = mi_cursor.execute("SELECT Usuario FROM Trabajador WHERE Clave_Trabajador = (:clave)",valor)
                    #Guardar el resultado en la variable de Usuario.
                    Usuario = mi_cursor.fetchall()
                    #Ciclo para el unpack del resultado de Usuario.
                    for dato in Usuario:
                        for n in dato:
                            usuario = str(n)
                    #Asignar al campo de Usuario el valor de usuario que se obtuvo anteriormente. 
                    self.Usuario.setText(usuario)
                    
                    #Buscar la contraseña del trabajador en la base de datos según la clave dada por el usuario y mostrarlo.
                    c = mi_cursor.execute("SELECT Contraseña FROM Trabajador WHERE Clave_Trabajador = (:clave)",valor)
                    #Guardar el resultado en la variable de Contraseña.
                    Contraseña = mi_cursor.fetchall()
                    #Ciclo para el unpack del resultado de Contraseña.
                    for dato in Contraseña:
                        for n in dato:
                            contraseña = str(n)
                    #Asignar al campo de Contra el valor de contraseña que se obtuvo anteriormente. 
                    self.Contra.setText(contraseña)
                    
                    #Buscar el nombre del puesto del trabajador en la base de datos según la clave dada por el usuario y mostrarlo.
                    c = mi_cursor.execute("SELECT p.Nombre FROM Trabajador t INNER JOIN Puesto p ON t.Puesto = p.Clave WHERE Clave_Trabajador = (:clave)",valor)
                    #Guardar el resultado en la variable de puesto.
                    puesto= mi_cursor.fetchall()
                    #Ciclo para el unpack del resultado de puesto.
                    for dato in puesto:
                        for n in dato:
                            Puesto = str(n)
                    #Asignar al campo de Puesto el valor de Puesto que se obtuvo anteriormente.
                    self.Puesto.setText(Puesto)
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
    def retranslateUi(self, EliminarTrabajador):
        _translate = QtCore.QCoreApplication.translate
        EliminarTrabajador.setWindowTitle(_translate("EliminarTrabajador", "MainWindow"))
        self.label_5.setText(_translate("EliminarTrabajador", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">ELIMINAR TRABAJADOR</span></p></body></html>"))
        self.label.setText(_translate("EliminarTrabajador", "<html><head/><body><p align=\"center\">CLAVE</p></body></html>"))
        self.label_2.setText(_translate("EliminarTrabajador", "<html><head/><body><p align=\"center\">NOMBRE</p></body></html>"))
        self.label_4.setText(_translate("EliminarTrabajador", "<html><head/><body><p align=\"center\">TELÉFONO</p></body></html>"))
        self.label_6.setText(_translate("EliminarTrabajador", "<html><head/><body><p align=\"center\">APELLIDO PATERNO</p></body></html>"))
        self.label_7.setText(_translate("EliminarTrabajador", "<html><head/><body><p align=\"center\">APELLIDO MATERNO</p></body></html>"))
        self.label_8.setText(_translate("EliminarTrabajador", "<html><head/><body><p align=\"center\">FECHA INGRESO</p></body></html>"))
        self.label_9.setText(_translate("EliminarTrabajador", "<html><head/><body><p align=\"center\">CONTRASEÑA</p></body></html>"))
        self.Contra.setHtml(_translate("EliminarTrabajador", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_10.setText(_translate("EliminarTrabajador", "<html><head/><body><p align=\"center\">PUESTO</p></body></html>"))
        self.Puesto.setHtml(_translate("EliminarTrabajador", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Usuario.setHtml(_translate("EliminarTrabajador", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_11.setText(_translate("EliminarTrabajador", "<html><head/><body><p align=\"center\">USUARIO</p></body></html>"))
        self.Limpiar.setText(_translate("EliminarTrabajador", "LIMPIAR"))
        self.Eliminar.setText(_translate("EliminarTrabajador", "ELIMINAR"))
        self.Cargar.setText(_translate("EliminarTrabajador", "CARGAR"))

#Cerrar aplicación.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EliminarTrabajador = QtWidgets.QMainWindow()
    ui = Ui_EliminarTrabajador()
    ui.setupUi(EliminarTrabajador)
    EliminarTrabajador.show()
    sys.exit(app.exec_())
