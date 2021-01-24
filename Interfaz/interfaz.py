from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Recursos\ICO\icono.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-image: url(:/Fondo/PNG/Fondo.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.QLabel_logotipo = QtWidgets.QLabel(self.centralwidget)
        self.QLabel_logotipo.setGeometry(QtCore.QRect(0, 0, 400, 130))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.QLabel_logotipo.sizePolicy().hasHeightForWidth())
        self.QLabel_logotipo.setSizePolicy(sizePolicy)
        self.QLabel_logotipo.setMinimumSize(QtCore.QSize(400, 130))
        self.QLabel_logotipo.setSizeIncrement(QtCore.QSize(1, 1))
        self.QLabel_logotipo.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"image: url(:/Logo_texto/PNG/Logo_texto.png);")
        self.QLabel_logotipo.setText("")
        self.QLabel_logotipo.setObjectName("QLabel_logotipo")
        self.QPushbutton_generar_informe = QtWidgets.QPushButton(self.centralwidget)
        self.QPushbutton_generar_informe.setGeometry(QtCore.QRect(550, 400, 211, 61))
        self.QPushbutton_generar_informe.setStyleSheet("QPushButton {\n"
"    background-color: rgb(5, 184, 204);\n"
"    font: 12pt \"Calibri\";\n"
"    border: 1px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 1px solid rgb(5, 184, 204);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    border: 2px solid rgb(6, 231, 255);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Generar/PNG/Generar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.QPushbutton_generar_informe.setIcon(icon1)
        self.QPushbutton_generar_informe.setIconSize(QtCore.QSize(45, 45))
        self.QPushbutton_generar_informe.setObjectName("QPushbutton_generar_informe")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(40, 350, 721, 41))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    color: rgb(255, 255, 255);\n"
"    font: 12pt \"Calibri\";\n"
"    border: 1px solid white;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #05B8CC;\n"
"    width: 15px;\n"
"}")
        self.progressBar.setProperty("value", 60)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.QPushButton_archivo_de_entrada = QtWidgets.QPushButton(self.centralwidget)
        self.QPushButton_archivo_de_entrada.setGeometry(QtCore.QRect(680, 170, 82, 40))
        self.QPushButton_archivo_de_entrada.setMinimumSize(QtCore.QSize(82, 40))
        self.QPushButton_archivo_de_entrada.setMaximumSize(QtCore.QSize(40, 40))
        self.QPushButton_archivo_de_entrada.setStyleSheet("QPushButton {\n"
"    border: 1px solid #8f8f91;\n"
"    border-radius: 4px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 1px solid rgb(5, 184, 204);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    border: 2px solid rgb(6, 231, 255);\n"
"}\n"
"\n"
"image: url(:/Nuevo/PNG/Nuevo.png);")
        self.QPushButton_archivo_de_entrada.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Abrir/PNG/Abrir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.QPushButton_archivo_de_entrada.setIcon(icon2)
        self.QPushButton_archivo_de_entrada.setIconSize(QtCore.QSize(30, 30))
        self.QPushButton_archivo_de_entrada.setObjectName("QPushButton_archivo_de_entrada")
        self.QLineEdit_ruta_de_salida = QtWidgets.QLineEdit(self.centralwidget)
        self.QLineEdit_ruta_de_salida.setGeometry(QtCore.QRect(40, 290, 630, 40))
        self.QLineEdit_ruta_de_salida.setMinimumSize(QtCore.QSize(630, 40))
        self.QLineEdit_ruta_de_salida.setMaximumSize(QtCore.QSize(630, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.QLineEdit_ruta_de_salida.setFont(font)
        self.QLineEdit_ruta_de_salida.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(5, 184, 204);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(5, 209, 231);\n"
"}")
        self.QLineEdit_ruta_de_salida.setObjectName("QLineEdit_ruta_de_salida")
        self.QPushButton_imagen_de_portada = QtWidgets.QPushButton(self.centralwidget)
        self.QPushButton_imagen_de_portada.setGeometry(QtCore.QRect(680, 230, 82, 40))
        self.QPushButton_imagen_de_portada.setMinimumSize(QtCore.QSize(82, 40))
        self.QPushButton_imagen_de_portada.setMaximumSize(QtCore.QSize(40, 40))
        self.QPushButton_imagen_de_portada.setStyleSheet("QPushButton {\n"
"    border: 1px solid #8f8f91;\n"
"    border-radius: 4px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 1px solid rgb(5, 184, 204);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    border: 2px solid rgb(6, 231, 255);\n"
"}")
        self.QPushButton_imagen_de_portada.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Imagen/PNG/Imagen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.QPushButton_imagen_de_portada.setIcon(icon3)
        self.QPushButton_imagen_de_portada.setIconSize(QtCore.QSize(70, 70))
        self.QPushButton_imagen_de_portada.setObjectName("QPushButton_imagen_de_portada")
        self.QLineEdit_archivo_de_entrada = QtWidgets.QLineEdit(self.centralwidget)
        self.QLineEdit_archivo_de_entrada.setGeometry(QtCore.QRect(40, 170, 630, 40))
        self.QLineEdit_archivo_de_entrada.setMinimumSize(QtCore.QSize(0, 40))
        self.QLineEdit_archivo_de_entrada.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.QLineEdit_archivo_de_entrada.setFont(font)
        self.QLineEdit_archivo_de_entrada.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(5, 184, 204);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(5, 209, 231);\n"
"}")
        self.QLineEdit_archivo_de_entrada.setObjectName("QLineEdit_archivo_de_entrada")
        self.QLineEdit_imagen_de_portada = QtWidgets.QLineEdit(self.centralwidget)
        self.QLineEdit_imagen_de_portada.setGeometry(QtCore.QRect(40, 230, 630, 40))
        self.QLineEdit_imagen_de_portada.setMinimumSize(QtCore.QSize(630, 40))
        self.QLineEdit_imagen_de_portada.setMaximumSize(QtCore.QSize(630, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.QLineEdit_imagen_de_portada.setFont(font)
        self.QLineEdit_imagen_de_portada.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(5, 184, 204);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(5, 209, 231);\n"
"}")
        self.QLineEdit_imagen_de_portada.setObjectName("QLineEdit_imagen_de_portada")
        self.QPushButton_ruta_de_salida = QtWidgets.QPushButton(self.centralwidget)
        self.QPushButton_ruta_de_salida.setGeometry(QtCore.QRect(680, 290, 82, 40))
        self.QPushButton_ruta_de_salida.setMinimumSize(QtCore.QSize(82, 40))
        self.QPushButton_ruta_de_salida.setMaximumSize(QtCore.QSize(40, 40))
        self.QPushButton_ruta_de_salida.setStyleSheet("QPushButton {\n"
"    border: 1px solid #8f8f91;\n"
"    border-radius: 4px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 1px solid rgb(5, 184, 204);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    border: 2px solid rgb(6, 231, 255);\n"
"}")
        self.QPushButton_ruta_de_salida.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Guardar/PNG/Guardar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.QPushButton_ruta_de_salida.setIcon(icon4)
        self.QPushButton_ruta_de_salida.setIconSize(QtCore.QSize(30, 30))
        self.QPushButton_ruta_de_salida.setObjectName("QPushButton_ruta_de_salida")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menu_Bar = QtWidgets.QMenuBar(MainWindow)
        self.menu_Bar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menu_Bar.setObjectName("menu_Bar")
        self.menu_Ayuda = QtWidgets.QMenu(self.menu_Bar)
        self.menu_Ayuda.setObjectName("menu_Ayuda")
        self.menu_Configuracion = QtWidgets.QMenu(self.menu_Bar)
        self.menu_Configuracion.setObjectName("menu_Configuracion")
        self.menu_Preferencias = QtWidgets.QMenu(self.menu_Configuracion)
        self.menu_Preferencias.setObjectName("menu_Preferencias")
        self.menu_Graficas = QtWidgets.QMenu(self.menu_Configuracion)
        self.menu_Graficas.setObjectName("menu_Graficas")
        self.menu_Archivo = QtWidgets.QMenu(self.menu_Bar)
        self.menu_Archivo.setObjectName("menu_Archivo")
        MainWindow.setMenuBar(self.menu_Bar)
        self.action_Ayuda = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Ayuda/PNG/Ayuda.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Ayuda.setIcon(icon5)
        self.action_Ayuda.setObjectName("action_Ayuda")
        self.action_Solucionar_problemas = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Soporte/PNG/Soporte.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Solucionar_problemas.setIcon(icon6)
        self.action_Solucionar_problemas.setObjectName("action_Solucionar_problemas")
        self.action_Fuente_de_texto = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Fuentes/PNG/Fuente.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Fuente_de_texto.setIcon(icon7)
        self.action_Fuente_de_texto.setObjectName("action_Fuente_de_texto")
        self.action_Nuevo = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/Nuevo/PNG/Nuevo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Nuevo.setIcon(icon8)
        self.action_Nuevo.setObjectName("action_Nuevo")
        self.action_Abrir = QtWidgets.QAction(MainWindow)
        self.action_Abrir.setIcon(icon2)
        self.action_Abrir.setObjectName("action_Abrir")
        self.action_Imprimir = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/Imprimir/Imprimir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Imprimir.setIcon(icon9)
        self.action_Imprimir.setObjectName("action_Imprimir")
        self.action_Guardar = QtWidgets.QAction(MainWindow)
        self.action_Guardar.setIcon(icon4)
        self.action_Guardar.setObjectName("action_Guardar")
        self.action_Quitar = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/Quitar/cruz-quitar-signo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Quitar.setIcon(icon10)
        self.action_Quitar.setObjectName("action_Quitar")
        self.action_Salir = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/Salir/PNG/Salir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Salir.setIcon(icon11)
        self.action_Salir.setObjectName("action_Salir")
        self.action_Espaciado_de_texto = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/Espaciado/PNG/Espaciado.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Espaciado_de_texto.setIcon(icon12)
        self.action_Espaciado_de_texto.setObjectName("action_Espaciado_de_texto")
        self.action_Colores = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/Colores/PNG/Colores.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Colores.setIcon(icon13)
        self.action_Colores.setObjectName("action_Colores")
        self.action_Linea = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/Linea/PNG/Linea.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Linea.setIcon(icon14)
        self.action_Linea.setObjectName("action_Linea")
        self.action_Grilla = QtWidgets.QAction(MainWindow)
        self.action_Grilla.setCheckable(True)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/Grilla/PNG/Grilla.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Grilla.setIcon(icon15)
        self.action_Grilla.setObjectName("action_Grilla")
        self.actionUsuario = QtWidgets.QAction(MainWindow)
        self.actionUsuario.setObjectName("actionUsuario")
        self.action_Sobre_Cohemo_GMP = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/PNG/PNG/Informacion.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Sobre_Cohemo_GMP.setIcon(icon16)
        self.action_Sobre_Cohemo_GMP.setObjectName("action_Sobre_Cohemo_GMP")
        self.menu_Ayuda.addAction(self.action_Ayuda)
        self.menu_Ayuda.addAction(self.action_Sobre_Cohemo_GMP)
        self.menu_Ayuda.addAction(self.action_Solucionar_problemas)
        self.menu_Preferencias.addAction(self.action_Fuente_de_texto)
        self.menu_Preferencias.addAction(self.action_Espaciado_de_texto)
        self.menu_Graficas.addAction(self.action_Colores)
        self.menu_Graficas.addAction(self.action_Linea)
        self.menu_Graficas.addAction(self.action_Grilla)
        self.menu_Configuracion.addAction(self.menu_Preferencias.menuAction())
        self.menu_Configuracion.addAction(self.menu_Graficas.menuAction())
        self.menu_Archivo.addAction(self.action_Nuevo)
        self.menu_Archivo.addAction(self.action_Abrir)
        self.menu_Archivo.addAction(self.action_Guardar)
        self.menu_Archivo.addSeparator()
        self.menu_Archivo.addAction(self.action_Salir)
        self.menu_Bar.addAction(self.menu_Archivo.menuAction())
        self.menu_Bar.addAction(self.menu_Configuracion.menuAction())
        self.menu_Bar.addAction(self.menu_Ayuda.menuAction())

        self.retranslateUi(MainWindow)
        self.action_Nuevo.triggered.connect(self.QLineEdit_archivo_de_entrada.clear)
        self.action_Nuevo.triggered.connect(self.QLineEdit_ruta_de_salida.clear)
        self.action_Nuevo.triggered.connect(self.QLineEdit_imagen_de_portada.clear)
        self.action_Abrir.triggered.connect(self.QPushButton_archivo_de_entrada.click)
        self.action_Salir.triggered.connect(MainWindow.close)
        self.action_Guardar.triggered.connect(self.QPushButton_ruta_de_salida.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cohemo - Generador de informes GMP"))
        self.QPushbutton_generar_informe.setText(_translate("MainWindow", "Generar informe"))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.QLineEdit_ruta_de_salida.setPlaceholderText(_translate("MainWindow", "Guardar informe en..."))
        self.QLineEdit_archivo_de_entrada.setPlaceholderText(_translate("MainWindow", "Abrir archivo..."))
        self.QLineEdit_imagen_de_portada.setPlaceholderText(_translate("MainWindow", "Abrir imagen de portada..."))
        self.menu_Ayuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.menu_Configuracion.setTitle(_translate("MainWindow", "Preferencias"))
        self.menu_Preferencias.setTitle(_translate("MainWindow", "Texto"))
        self.menu_Graficas.setTitle(_translate("MainWindow", "Gráficas"))
        self.menu_Archivo.setTitle(_translate("MainWindow", "Archivo"))
        self.action_Ayuda.setText(_translate("MainWindow", "Ayuda"))
        self.action_Solucionar_problemas.setText(_translate("MainWindow", "Solucionar problemas"))
        self.action_Fuente_de_texto.setText(_translate("MainWindow", "Fuente de texto"))
        self.action_Nuevo.setText(_translate("MainWindow", "Nuevo..."))
        self.action_Nuevo.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_Abrir.setText(_translate("MainWindow", "Abrir..."))
        self.action_Abrir.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.action_Imprimir.setText(_translate("MainWindow", "Imprimir..."))
        self.action_Guardar.setText(_translate("MainWindow", "Guardar"))
        self.action_Guardar.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.action_Quitar.setText(_translate("MainWindow", "Quitar"))
        self.action_Salir.setText(_translate("MainWindow", "Salir"))
        self.action_Salir.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.action_Espaciado_de_texto.setText(_translate("MainWindow", "Espaciado de texto"))
        self.action_Colores.setText(_translate("MainWindow", "Colores"))
        self.action_Linea.setText(_translate("MainWindow", "Línea"))
        self.action_Grilla.setText(_translate("MainWindow", "Grilla"))
        self.actionUsuario.setText(_translate("MainWindow", "Usuario"))
        self.action_Sobre_Cohemo_GMP.setText(_translate("MainWindow", "Sobre Cohemo GMP"))
        
import Recursos.Python.Abrir
import Recursos.Python.Ayuda
import Recursos.Python.Colores
import Recursos.Python.Espaciado
import Recursos.Python.Fondo
import Recursos.Python.Fuentes
import Recursos.Python.Generar
import Recursos.Python.Grilla
import Recursos.Python.Guardar
import Recursos.Python.Icono
import Recursos.Python.Imagen
import Recursos.Python.Linea
import Recursos.Python.Logo
import Recursos.Python.Informacion
import Recursos.Python.Nuevo
import Recursos.Python.Salir
import Recursos.Python.Soporte


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
