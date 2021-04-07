#! /usr/bin/python
# -*- coding: utf-8 -*-
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
#...................................................................
# El programa ejecutor "boton_final.py" ejecuta los programas graficos
# de la mesa interactiva de la seccion tecnologica del MUCYT, dicho 
# programa enlaza con los programas PYTHON ejecutados en el sistema RASPBERRY:
#
#  new_luz_graph_final.py
#  new_presion_graph_final.py
#  new_sonido_graph_final.py
#  nuevo_web_final.py
#  sema_boton_final.py
#  tempe_boton_final.py
# 
# Y con el programa C++ ejecutado en el sistema ARDUINO:
#  
#  programas_arduino_final.ino
#
# Todos ellos en conjunto recopilan, ejecutan y procesan los datos obtenidos 
# por los diferentes sensores digital-analogicos encontrados en la mesa interactiva 
# de la seccion de tecnologia del MUCYT. 
#
#
# Todos los programas dependen de librerias externas que deben ser pre cargadas
# o instaladas en el sistema operativo para poder ser ejecutadas 
# Librerias de : arduino, python y opencv
#
# Programas pensados para ser usados en sistemas linux-GNU
#...................................................................


import sys, os, time, cv
from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT
import os
import pprint
import random
import sys, serial
import wx
from PyQt4 import QtGui, QtCore, uic
       
class Principal(QtGui.QWidget):
      def __init__(self, parent=None):
          QtGui.QWidget.__init__(self, parent)
          self.setGeometry(0, 0, 1920, 1080)
          self.setWindowIcon(QtGui.QIcon('pi.jpg'))  
          self.pic = QtGui.QLabel(self)
          self.pic.setGeometry(0, 0, 1920,1080)
          self.pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/fondo_1_raspberry_arduino.png"))
          self.setWindowTitle('Domotica')
          self.pic1 = QtGui.QLabel(self)
          self.pic1.setGeometry(1660, 5, 250,243)
          self.pic1.setPixmap(QtGui.QPixmap(os.getcwd() + "/intro_logo_gobernacion.png"))
          self.pic2 = QtGui.QLabel(self)
          self.pic2.setGeometry(20, 10, 180,211)
          self.pic2.setPixmap(QtGui.QPixmap(os.getcwd() + "/intro_logo_mucyt.png"))
          self.pic3 = QtGui.QLabel(self)
          self.pic3.setGeometry(20, 550, 183,190)
          self.pic3.setPixmap(QtGui.QPixmap(os.getcwd() + "/intro_logo_raspberry.png"))
          self.pic4 = QtGui.QLabel(self)
          self.pic4.setGeometry(1735, 590, 201,145)
          self.pic4.setPixmap(QtGui.QPixmap(os.getcwd() + "/intro_logo_arduino.png"))

          self.label = QtGui.QLabel(self)
          self.label.setGeometry(620, 10, 662, 122)
          self.label.setPixmap(QtGui.QPixmap(os.getcwd() + "/intro_header.png"))


          self.label11 = QtGui.QLabel(self)
          self.label11.setGeometry(50, 730, 1831,331)
          self.label11.setPixmap(QtGui.QPixmap(os.getcwd() + "/intro_cuadro1.png"))

          self.label1 = QtGui.QLabel(self)
          self.label1.setGeometry(100, 740, 1800,300)
          self.label1.setStyleSheet("font-size:38px;color:#000000")
          self.label1.setText(u"Se entiende por domótica el conjunto de sistemas capaces de automatizar una vivienda, \naportando servicios de gestión energética, seguridad, bienestar y comunicación, y que \npueden estar integrados por medio de redes interiores y exteriores de comunicación,\ncableadas o inalámbricas, y cuyo control goza de cierta ubicuidad, desde dentro y fuera \ndel hogar. Se podría definir como la integración de la tecnología en el diseño inteligente \nde un recinto cerrado")
          
          tem = QtGui.QPushButton('TEMPERATURA', self)
          tem.setGeometry(170,270,400,100)
          tem.setStyleSheet("font-size:45px;color:#000000;background-color:#0065a5;border: 2px solid #222222")
          tem.setFont(QtGui.QFont("Verdana", 50, QtGui.QFont.Bold))
               
          web = QtGui.QPushButton('WEBCAM', self)
          web.setGeometry(770,270,400,100)
          web.setStyleSheet("font-size:45px;color:#000000;background-color:#8A0CA6;\
        border: 2px solid #222222")
          web.setFont(QtGui.QFont("Verdana", 50, QtGui.QFont.Bold))
 
          pre = QtGui.QPushButton('PRESION', self)
          pre.setGeometry(1330,270,400,100)
          pre.setStyleSheet("font-size:45px;color#000000;background-color:#E75112;\
        border: 2px solid #222222")
          pre.setFont(QtGui.QFont("Verdana", 50, QtGui.QFont.Bold))

          sem = QtGui.QPushButton('SEMAFORO', self)
          sem.setGeometry(170,520,400,100)
          sem.setStyleSheet("font-size:45px;color:#000000;background-color:#9a9b9c;\
        border: 2px solid #222222")
          sem.setFont(QtGui.QFont("Verdana", 50, QtGui.QFont.Bold))

          luz = QtGui.QPushButton('LUMINOSIDAD', self)
          luz.setGeometry(770,520,400,100)
          luz.setStyleSheet("font-size:45px;color:#000000;background-color:#E2001A;\
        border: 2px solid #222222")
          luz.setFont(QtGui.QFont("Verdana", 50, QtGui.QFont.Bold))

          son = QtGui.QPushButton('SONIDO', self)
          son.setGeometry(1330,520,400,100)
          son.setStyleSheet("font-size:45px;color:#000000;background-color:#159730;\
        border: 2px solid #222222")
          son.setFont(QtGui.QFont("Verdana", 50, QtGui.QFont.Bold))
          
          self.tem1 = QtGui.QLabel(self)
          self.tem1.setGeometry(300,120, 156, 156)
          self.tem1.setPixmap(QtGui.QPixmap(os.getcwd() + "/intro_icono_temperatura.png"))
          
          self.web1 = QtGui.QLabel(self)
          self.web1.setGeometry(900,120, 156, 156)
          self.web1.setPixmap(QtGui.QPixmap(os.getcwd() + "/intro_icono_webcam.png"))
         
          self.pre1 = QtGui.QLabel(self)
          self.pre1.setGeometry(1460,120, 156, 156)
          self.pre1.setPixmap(QtGui.QPixmap(os.getcwd() + "/intro_icono_presion.png"))

          self.sem1 = QtGui.QLabel(self)
          self.sem1.setGeometry(300,370, 156, 156)
          self.sem1.setPixmap(QtGui.QPixmap(os.getcwd() + "/intro_icono_semaforo.png"))

          self.luz1 = QtGui.QLabel(self)
          self.luz1.setGeometry(900,370, 156, 156)
          self.luz1.setPixmap(QtGui.QPixmap(os.getcwd() + "/intro_icono_luminosidad.png"))

          self.son1 = QtGui.QLabel(self)
          self.son1.setGeometry(1460,370, 156, 156)
          self.son1.setPixmap(QtGui.QPixmap(os.getcwd() + "/intro_icono_sonido.png"))
 
          self.ctimer = QtCore.QTimer()
          self.ctimer.start(500)
          QtCore.QObject.connect(self.ctimer, QtCore.SIGNAL("timeout()"), self.programa)

      def programa(self):        
        
        while self.arduino.inWaiting() > 0:
            self.prog += self.arduino.read(1)

        if self.prog == 'A'
           abrirtem()

        if self.prog == 'B'
           abrirweb()

        if self.prog == 'C'
           abrirpre()

        if self.prog == 'D'
           abrirsem()

        if self.prog == 'E'
           abrirluz()

        if self.prog == 'F'
           abrirson()

        self.prog = ''
          
      def abrirtem(self):
        from tempe_boton import Principalt
        
      def abrirweb(self):
        from nuevo_web import Principalw

      def abrirpre(self):
        from new_presion_graph import Principalp

      def abrirsem(self):
        from sema_boton import Principals
        del(Principals)

      def abrirluz(self):
        from new_luz_graph import Principall

      def abrirson(self):
        from new_sonido_graph import Principalss


app = QtGui.QApplication(sys.argv)
icon = Principal()
icon.show()
sys.exit(app.exec_())
