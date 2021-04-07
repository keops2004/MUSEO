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
import serial


class Principalss(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)


        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle('Sonido')
        self.setWindowIcon(QtGui.QIcon('pi.jpg'))
        self.pic = QtGui.QLabel(self)
        self.pic.setGeometry(0, 0, 1920,1080)
        self.pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/temperatura_fondo.png"))
        
        self.data = ''
        self.arduino = serial.Serial('/dev/ttyACM0',9600)
        self.arduino.open()    
        
        quit = QtGui.QPushButton(self)
        quit.setIcon(QtGui.QIcon('sonido_boton_inicio.png'))
        quit.setIconSize(QtCore.QSize(747,48))
        

        self.connect(quit, QtCore.SIGNAL('clicked()'), self.salir)

        self.label = QtGui.QLabel(self)
        self.label.setGeometry(1300, 20, 400, 100) # 600
        self.label.setPixmap(QtGui.QPixmap(os.getcwd() + "/sonido_header.png"))

        self.labe = QtGui.QLabel(self)
        self.labe.setGeometry(0, 430, 303, 403) #740
        self.labe.setPixmap(QtGui.QPixmap(os.getcwd() + "/sonido_icono_volumen.png"))

        self.label11 = QtGui.QLabel(self)
        self.label11.setGeometry(1020, 160, 890, 863) #1000
        self.label11.setPixmap(QtGui.QPixmap(os.getcwd() + "/sonido_cuadro1.png"))

        self.label1 = QtGui.QLabel(self)
        self.label1.setGeometry(1095, 230, 770, 800) #1195
        self.label1.setStyleSheet("font-size:32px;font-family: Verdana;color:#000000")
        self.label1.setText(u"El sonido es cualquier fenómeno que \ninvolucre la propagación en forma de \nondas elásticas, generalmente a través de un \nfluido. El nivel de potencia acústica  es la cantidad \nde energía radiada al medio en forma de ondas. \nEl cual es medído utilizando una unidad \nlogarítmica, adimensional y matemáticamente \nescalar llamada Decibel (dB).\n\nEspectro de frecuencias: permite conocer a que \nfrecuencias se transmite la mayor parte de la \nenergía. El sonido tiene una velocidad de 331,5 \nm/s en el aire apresión atmosférica y \ntemperatura ambiente.\n\nLa velocidad del sonido depende del tipo de \nmaterial, especialmente de su densidad.")

        self.label22 = QtGui.QLabel(self)
        self.label22.setGeometry(3080, 530, 770, 580) #1160
        self.label22.setPixmap(QtGui.QPixmap(os.getcwd() + "/sonido_cuadro2.png"))
        
                
        self.label33 = QtGui.QLabel(self)
        self.label33.setGeometry(840, 380, 600, 500)#560
        self.label33.setPixmap(QtGui.QPixmap(os.getcwd() + "/sonido_icono_microfono.png"))
        
        
        self.label3 = QtGui.QLabel(self)
        self.label3.setGeometry(30, 720, 1000, 290) #630
        self.label3.setText(u"Hable por el micrófono (o aplauda) para \nobtener la intensidad de sonido detectada.")
        self.label3.setStyleSheet("font-size:40px;color:#000000")
        
        self.foton = QtGui.QLabel(self)
        self.foton.setGeometry(160, 550, 1300, 200) #200
        self.foton.setStyleSheet("font-size:50px;font-family: Verdana;color:#000000")
        self.foton.setText('(Decibeles) Intensidad (dB)')

        self.ctimer = QtCore.QTimer()
        self.ctimer.start(400)
        QtCore.QObject.connect(self.ctimer, QtCore.SIGNAL("timeout()"), self.plot)
        
        self.press = QtGui.QLCDNumber(5, self)
        self.press.display(0);     

        grid = QtGui.QGridLayout()
        grid.setColumnStretch(1, 10)
        topBox = QtGui.QVBoxLayout()
        grid.addLayout(topBox, 1, 0)
        topBox.addSpacing(40)
        topBox.addWidget(quit)
        topBox.addSpacing(10)
        topBox.addWidget(self.press)
        topBox.addSpacing(120)
        topBox.addWidget(self.label22)
        self.setLayout(grid)

    def plot(self):
       
        while self.arduino.inWaiting() > 0:
            self.data += self.arduino.read(1)

        if '\n' in self.data:
            lines = self.data.split('\n')
            self.last_received = lines[-2]
            #print self.last_received
            self.data = lines[-1]

        self.press.display(self.last_received)  

        if self.last_received == '#'
            self.salir()       

    def salir(self):
        self.ctimer.stop()
        self.arduino.close()
        self.deleteLater()

    

icont = Principalss()
icont.show()

