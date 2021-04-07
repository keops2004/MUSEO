#! /usr/bin/python
#-*- coding: utf-8 -*-
#******************************************************************
# Programas desarrolados para el Museo de Ciencias y Tecnologia
# (MUCYT). Dicha entidad se reserva el derecho de reproducir, modificar
# y autorizar el uso de dichos programas para cualquier fin distinto
# al educativo y que sea en beneficio cientifico-tecnologico de la nacion
# venezolana.
# De igual forma se prohibe la comercializacion de dicho producto al ser
# de origen softwarelibre y hardwarelibre. 
#
#                      copyleft  INTEDAS  Venezuela-2014
#*******************************************************************
import sys, os, time, cv, serial
from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT


class Principalt(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle('Temperatura')
        self.setWindowIcon(QtGui.QIcon('pi.jpg'))
        self.pic = QtGui.QLabel(self)
        self.pic.setGeometry(0, 0, 1920,1080)
        self.pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/temperatura_fondo.png"))
        self.arduino = serial.Serial('/dev/ttyACM0',9600)
        self.arduino.open()
        self.data = ''
        
        quit = QtGui.QPushButton(self)       
        quit.setIcon(QtGui.QIcon('temperatura_boton_inicio2.png'))
        quit.setIconSize(QtCore.QSize(230,121))
       
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(600, 10, 400, 100)
        self.label.setPixmap(QtGui.QPixmap(os.getcwd() + "/titulo_temperatura_400x100_72dpisombra_negro.png"))

        self.labe = QtGui.QLabel(self)
        self.labe.setGeometry(740, 150, 303, 403)
        self.labe.setPixmap(QtGui.QPixmap(os.getcwd() + "/temperatura_cuadro_termometro.png"))

        self.label11 = QtGui.QLabel(self)
        self.label11.setGeometry(1160, 10, 750, 580)
        self.label11.setPixmap(QtGui.QPixmap(os.getcwd() + "/temperatura_cuadro_1.png"))

        self.label1 = QtGui.QLabel(self)
        self.label1.setGeometry(1195, 40, 770, 580)
        self.label1.setStyleSheet("font-size:32px;font-family: Verdana;color:#000000")
        self.label1.setText(u"La temperatura es una magnitud referida \na las nociones comunes de caliente, tibio \no frío que puede ser medida con un \ntermómetro. En física, se define como una \nmagnitud escalar relacionada con la \nenergía interna de un sistema \ntermodinámico.\nMás especificamente, esta relacionada \ndirectamente con la  energía cinética, es \ndecir asociada a los movimientos de las \npartículas del sistema.")

        self.label22 = QtGui.QLabel(self)
        self.label22.setGeometry(1160, 530, 770, 580)
        self.label22.setPixmap(QtGui.QPixmap(os.getcwd() + "/temperatura_cuadro_2.png"))
        
        self.label2 = QtGui.QLabel(self)
        self.label2.setGeometry(1190, 406, 770, 570)
        self.label2.setStyleSheet("font-size:24px;color:#000000")
        self.label2.setText(u"En esta escala se ha fijado el valor de cero grados Celsius \npara el punto de fusión y el de cien grados Celsius para \nel punto de ebullición del agua.")

        self.label5 = QtGui.QLabel(self)
        self.label5.setGeometry(1190, 535, 770, 570)
        self.label5.setStyleSheet("font-size:24px;color:#000000")
        self.label5.setText("Es la unidad de temperatura  creada por Lord Kelvin, en el \naño 1848, sobre la base del grado Celsius, estableciendo \nel punto cero a -273 °C.")

        self.label6 = QtGui.QLabel(self)
        self.label6.setGeometry(1190, 675, 770, 570)
        self.label6.setStyleSheet("font-size:24px;color:#000000")
        self.label6.setText(u"Es una escala de temperatura propuesta por Daniel \nFahrenheir, estableciendo como las temperaturas \nde congelación y ebullición del agua, 32 F y 212 F.")
        
        self.label33 = QtGui.QLabel(self)
        self.label33.setGeometry(590, 570, 600, 500)
        self.label33.setPixmap(QtGui.QPixmap(os.getcwd() + "/temperatura_cuadro_3.png"))
        
        
        self.label3 = QtGui.QLabel(self)
        self.label3.setGeometry(630, 630, 500, 290)
        self.label3.setText(u"Colocar la mano sobre la semi \nesfera de metal y observar los \ncambios de la temperatura \nmostrados en la pantalla, en las \nprincipales unidades de medida.")
        self.label3.setStyleSheet("font-size:30px;color:#000000")
     
        self.cent = QtGui.QLabel(self)
        self.cent.setGeometry(0, 240, 600, 110)
        self.cent.setPixmap(QtGui.QPixmap(os.getcwd() + "/temperatura_banner_celsius.png"))

        self.kelv = QtGui.QLabel("Grados Kelvin", self)
        self.kelv.setGeometry(0, 560, 600, 110)
        self.kelv.setPixmap(QtGui.QPixmap(os.getcwd() + "/temperatura_banner_kelvin.png"))

        self.fahr = QtGui.QLabel(" Grados Fahrenheit", self)
        self.fahr.setGeometry(0, 876, 600, 100)
        self.fahr.setPixmap(QtGui.QPixmap(os.getcwd() + "/temperatura_banner_fahrenheit.png"))

        self.centigrados = QtGui.QLCDNumber(5, self)        
        self.kelvin = QtGui.QLCDNumber(5, self)       
        self.Fahrenheit = QtGui.QLCDNumber(5, self)
       
        grid = QtGui.QGridLayout()
        grid.setColumnStretch(1, 10)
        topBox = QtGui.QVBoxLayout()
        grid.addLayout(topBox, 1, 0)
        topBox.addWidget(quit)
        topBox.addWidget(self.centigrados)
        topBox.addWidget(self.kelvin)
        topBox.addWidget(self.Fahrenheit)
        self.setLayout(grid)
        
        self.connect(quit, QtCore.SIGNAL('clicked()'), self.salir)

        self.ctimer = QtCore.QTimer()
        self.ctimer.start(500)
        QtCore.QObject.connect(self.ctimer, QtCore.SIGNAL("timeout()"), self.constantUpdate)
        

    def constantUpdate(self):
        self.arduino.write("A")         
        while self.arduino.inWaiting() > 0:
            self.data += self.arduino.read(1)

        if '\n' in self.data:
            lines = self.data.split('\n')
            self.last_received = lines[-2]
            
            self.data = lines[-1]
       
        self.centigrados.display(int(self.last_received) -70)        
        self.kelvin.display(int(self.last_received) + 273.15 - 70)           
        self.Fahrenheit.display((int(self.last_received) -70)* 1.8 + 32)

        if self.last_received == '#'
            self.salir()


    def salir(self):
        self.arduino.close()
        self.ctimer.stop()
        self.deleteLater()
        
           

    

icont = Principalt()
icont.show()

