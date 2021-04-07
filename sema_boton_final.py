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
 

class Principals(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
      
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle('Semaforo')
        self.setWindowIcon(QtGui.QIcon('pi.jpg'))
        self.pic = QtGui.QLabel(self)
        self.pic.setGeometry(0, 0, 1920,1080)
        self.pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/fondo_1_raspberry_arduino.png"))
        quit = QtGui.QPushButton(self)
        #quit.setFont(QtGui.QFont("Times", 50, QtGui.QFont.Bold))
        #border: 2px solid #222222")
        quit.setIcon(QtGui.QIcon('semaforo_boton_inicio.png'))
        quit.setIconSize(QtCore.QSize(230,121))

        self.arduino = serial.Serial('/dev/ttyACM0',9600)
        self.arduino.open()


        self.label = QtGui.QLabel(self)
        self.label.setGeometry(680, 10, 382, 105)
        #self.label.setStyleSheet("font-size:45px;color:#000000;background-color:#ff7800;\
        #border: 2px solid #222222")
        #self.label.setText("Semaforo")
        self.label.setPixmap(QtGui.QPixmap(os.getcwd() + "/semaforo_header.png"))

        self.label11 = QtGui.QLabel(self)
        self.label11.setGeometry(1100, 0, 821, 574)
        self.label11.setPixmap(QtGui.QPixmap(os.getcwd() + "/semaforo_cuadro1.png"))

        self.label1 = QtGui.QLabel(self)
        self.label1.setGeometry(1250, 0, 821, 574)
        self.label1.setStyleSheet("font-size:28px;color:#000000")
        self.label1.setText("Los semaforos, tambien conocido \ntecnicamente como senales de control de \ntrafico, son dispositivos de senales que se \nsituan en intersecciones viales y otros lugares \npara regular el trafico. \n\nRojo: Detenerse inmediatamente. \n\nAmarillo: Avanzar con cautela y/o \n               disminuir la velocidad \n\nVerde: Via libre de obstaculos, avanzar")
        
        self.label22 = QtGui.QLabel(self)
        self.label22.setGeometry(1110, 420, 821, 763)
        self.label22.setPixmap(QtGui.QPixmap(os.getcwd() + "/semaforo_cuadro2.png"))
                 
        self.label2 = QtGui.QLabel(self)
        self.label2.setGeometry(1150, 420, 821, 763)
        self.label2.setStyleSheet("font-size:28px;color:#000000")
        self.label2.setText("Los semaforos han ido evolucionando con el paso \ndel tiempo, actualmente y debido a su rentabilidad, \nse estan utilizando lamparas a LED para la \nsenalizacion luminosa, puesto que las lamparas de \nLED utilizan solo 10% de la energia consumida por \nlas lamparas incandescentes, tienen una vida \nestimada 50 veces superior, y por tanto generan \nimportantes ahorros de energia y de mantenimiento, \nsatisfaciendo el objetivo de conseguir una mayor \nfiabilidad y seguridad publica")


        self.label33 = QtGui.QLabel(self)
        self.label33.setGeometry(590, 565, 569, 474)
        self.label33.setPixmap(QtGui.QPixmap(os.getcwd() + "/semaforo_cuadro3.png"))

        self.label3 = QtGui.QLabel(self)
        self.label3.setGeometry(620, 510, 569, 474)
        self.label3.setStyleSheet("font-size:28px;color:#000000")
        self.label3.setText("1) Seleccionar por cada color el \ntiempo de activacion del mismo. \n\n2) Pulsar el boton fuscia para \nactivar el semaforo del tablero")
    

        self.roj = QtGui.QLabel(self)
        self.roj.setGeometry(0, 200, 586, 168)
        self.roj.setPixmap(QtGui.QPixmap(os.getcwd() + "/semaforo_back_rojo_contador.png"))

        self.roj = QtGui.QLabel("Tiempo (segundos) \n     Color Rojo", self)
        self.roj.setGeometry(280, 200, 586, 168)
       
        self.roj.setStyleSheet("font-size:26px;color:#000000")

        self.ama = QtGui.QLabel(self)
        self.ama.setGeometry(0, 500, 586, 168)
        self.ama.setPixmap(QtGui.QPixmap(os.getcwd() + "/semaforo_back_amarillo_contador.png"))

        self.ama = QtGui.QLabel("Tiempo (segundos) \n   Color Amarillo", self)
        self.ama.setGeometry(280, 500, 586, 168)
        
        self.ama.setStyleSheet("font-size:26px;color:#000000")

        self.ver = QtGui.QLabel(self)			
        self.ver.setGeometry(10, 800, 586, 168)
        self.ver.setPixmap(QtGui.QPixmap(os.getcwd() + "/semaforo_back_verde_contador.png"))

        self.ver = QtGui.QLabel("Tiempo (segundos) \n     Color Verde", self)			
        self.ver.setGeometry(280, 810, 586, 168)
        
        self.ver.setStyleSheet("font-size:26px;color:#000000")

        activar = QtGui.QPushButton( self)
        activar.setGeometry(710,140,300,70)
        #activar.setStyleSheet("font-size:25px;color:#000000;background-color:#ff00f6;\
        #border: 2px solid #222222")
        activar.setIcon(QtGui.QIcon('semaforo_boton_activar.png'))
        activar.setIconSize(QtCore.QSize(230,121))

        self.logo = QtGui.QLabel(self)
        self.logo.setGeometry(710, 250, 284, 287)
        self.logo.setPixmap(QtGui.QPixmap(os.getcwd() + "/semaforo_imagen.png"))

        lcd1 = QtGui.QLCDNumber(3,self)  
        lcd2 = QtGui.QLCDNumber(3,self)
        lcd3 = QtGui.QLCDNumber(3,self)

        grid = QtGui.QGridLayout()
        grid.setColumnStretch(1, 10)
        grid.setRowStretch(1, 1)
        grid.setVerticalSpacing(2) 
        grid.setHorizontalSpacing(20)
        leftBox = QtGui.QVBoxLayout()
        grid.addLayout(leftBox, 1, 0)
        leftBox.addWidget(quit)
        leftBox.addWidget(lcd1)
        leftBox.addSpacing(30)
        leftBox.addWidget(lcd2)
        leftBox.addSpacing(30)
        leftBox.addWidget(lcd3)        
        leftBox.addSpacing(30)
        self.setLayout(grid)
        self.setLayout(leftBox)      

        self.connect(quit, QtCore.SIGNAL('clicked()'), self.salir)
        

    def plot(self):        
       
        while self.arduino.inWaiting() > 0:
            self.data += self.arduino.read(1)

        if '\n' in self.data:
            lines = self.data.split('\n')
            self.last_received = lines[-2]
            #print self.last_received
            self.data = lines[-1]


        if self.last_received == '#'
            self.salir()

        if self.last_received == '#'
            lcd1.display(1);

        if self.last_received == '#'
            lcd2.display(1);

        if self.last_received == '#'
            lcd3.display(1);
            

    def salir(self):        
        self.ctimer.stop()
        self.arduino.close()
        self.deleteLater()

   
icons = Principals()
icons.show()

