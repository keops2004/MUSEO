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
import sys, serial, time, os
from PyQt4 import uic, QtGui, QtCore
import cv2.cv as cv
 
class Principalw(QtGui.QWidget): 
     def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.first = True
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle('Webcam')
        self.setWindowIcon(QtGui.QIcon('pi.jpg'))  
        self.pic = QtGui.QLabel(self)
        self.pic.setGeometry(0, 0, 1920,1080)
        self.pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/fondo_1_raspberry_arduino.png"))  
     
        quit = QtGui.QPushButton(self)
        quit.setGeometry(1680,940,200,70)
        quit.setIcon(QtGui.QIcon('camara_boton_inicio.png'))
        quit.setIconSize(QtCore.QSize(230,121))

        self.connect(quit, QtCore.SIGNAL('clicked()'), self.salir)

        self.label = QtGui.QLabel(self)
        self.label.setGeometry(800, 15, 381, 106)
        self.label.setPixmap(QtGui.QPixmap(os.getcwd() + "/camara_header.png"))

        self.label11 = QtGui.QLabel(self)
        self.label11.setGeometry(1200, 10, 692, 414)
        self.label11.setPixmap(QtGui.QPixmap(os.getcwd() + "/camara_cuadro1.png"))

        self.icono = QtGui.QLabel(self)
        self.icono.setGeometry(860, 150, 264, 264)
        self.icono.setPixmap(QtGui.QPixmap(os.getcwd() + "/camara_icono.png"))

       
        self.label1 = QtGui.QLabel(self)
        self.label1.setGeometry(1240, 20, 692, 414)
        self.label1.setStyleSheet("font-size:35px;color:#000000")
        self.label1.setText(u"Es una pequeña cámara digital \nconectada a una computadora, \nla cual puede capturar imágenes \ny transmitirlas a través de Internet, \nya sean a una pagina web u \notras computadoras de forma \nprivada.")
        
        self.label22 = QtGui.QLabel(self)
        self.label22.setGeometry(1200, 420, 691, 414)
        self.label22.setPixmap(QtGui.QPixmap(os.getcwd() + "/camara_cuadro2.png"))
        
        self.label2 = QtGui.QLabel(self)
        self.label2.setGeometry(1240, 420, 691, 414)
        self.label2.setStyleSheet("font-size:35px;color:#000000")
        self.label2.setText(u"En su forma mas elemental el CCD \nes un sensor el cual actúa como un \nojo electrónico que recoje la luz y \nla convierte en una señal electrica.")
        
        self.label33 = QtGui.QLabel(self)
        self.label33.setGeometry(35, 830, 1107, 189)
        self.label33.setPixmap(QtGui.QPixmap(os.getcwd() + "/camara_cuadro3.png"))
        
        self.label3 = QtGui.QLabel(self)
        self.label3.setGeometry(65, 855, 1107, 189)
        self.label3.setStyleSheet("font-size:32px;color:#000000")
        self.label3.setText(u"Posicione la mano sobre el circulo verde (indicado en \nla pantalla) para encender el LED y sobre el circulo rojo \npara apagarlo")

        self.ctimer = QtCore.QTimer();
        self.connect(self.ctimer, QtCore.SIGNAL('timeout()'), self.show_frame)
        self.ctimer.start(250);    
         
    
        self.capture = cv.CaptureFromCAM(-1)
        cv.SetCaptureProperty(self.capture, cv.CV_CAP_PROP_FRAME_HEIGHT, 300)
        cv.SetCaptureProperty(self.capture, cv.CV_CAP_PROP_FRAME_WIDTH, 380)
             

        self.window1 = "Color"
        self.window2 = "HLS"
        self.window3 = "HSV"
        self.window4 = "Negativo"

           
     def show_frame(self):        
                 
         color_image = cv.QueryFrame(self.capture)
        
         color_image1 = cv.CreateImage(cv.GetSize(color_image), 8, 3)
         grey_image = cv.CreateImage(cv.GetSize(color_image), cv.IPL_DEPTH_8U, 1)
         moving_average = cv.CreateImage(cv.GetSize(color_image), cv.IPL_DEPTH_32F, 3)

         grey = cv.CreateImage(cv.GetSize(color_image), 8, 3)
         HSV = cv.CreateImage(cv.GetSize(color_image), 8, 3)
         red = cv.CreateImage(cv.GetSize(color_image), 8, 3)         

         cv.CvtColor(color_image, grey, cv.CV_RGB2HLS)
         cv.CvtColor(color_image, HSV, cv.CV_RGB2HSV)
         cv.Not(color_image, red)

         cv.ShowImage(self.window1, color_image)
         cv.ShowImage(self.window2, grey) 
         cv.ShowImage(self.window3, HSV) 
         cv.ShowImage(self.window4, red)

         cv.MoveWindow(self.window1, 30, 120) 
         cv.MoveWindow(self.window2, 430, 120)
         cv.MoveWindow(self.window3, 430, 470)
         cv.MoveWindow(self.window4, 30, 470)

         while self.arduino.inWaiting() > 0:
            self.data += self.arduino.read(1)

        if '\n' in self.data:
            lines = self.data.split('\n')
            self.last_received = lines[-2]
            self.data = lines[-1]

        self.press.display(self.last_received)  

        if self.last_received == '#'
            self.salir()
                          
     def salir(self):
         self.ctimer.stop()       
         cv.DestroyWindow(self.window1)
         cv.DestroyWindow(self.window2) 
         cv.DestroyWindow(self.window3)
         cv.DestroyWindow(self.window4)
         self.deleteLater()        
           
         
   

iconw = Principalw()
iconw.show()

