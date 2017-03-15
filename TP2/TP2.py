import numpy as np
import random
import time
from collections import deque
from array import *
import operator



class Simulacion(object):

    def __init__(self):
        self.Reloj = 0.0
        self.ListaDeEventos = []
        self.TamañoCola = []
        self.EstadoServidor= []
        self.TMArribos = 10.0
        self.TMServidor1 = 6.0
        self.TMServidor2 = 4.0
        self.TMServidor3 = 5.0
        self.TMServidor4n = 5.0
        self.TMServidor4d = 8.0
        self.TMServidor5 = 12.0
        self.TiempoUltimoEvento = 0.0
        self.Tipo = ''
        self.Menor = 0



    def inicializacion(self):
        self.Reloj=0
        for i in range(0, 5):
            self.ListaDeEventos.append(valorExponencial(self.TMArribos))
            self.EstadoServidor.append('D')
            self.ListaDeEventos.append(99999.0)
        for k in range(0, 6):
            self.TamañoCola.append(0)
        self.TiempoUltimoEvento = 0


    def programaPrincipal(self):
        self.inicializacion()
        while True:
            self.tiempos()
            if self.ProximoEvento == 1:
                self.arriboS1()
            if self.ProximoEvento == 2:
                self.partidaS1()
            if self.ProximoEvento == 3:
                self.arriboS2()
            if self.ProximoEvento == 4:
                self.partidaS2()
            if self.ProximoEvento == 5:
                self.arriboS3()
            if self.ProximoEvento == 6:
                self.partidaS3()
            if self.ProximoEvento == 7:
                self.arriboS4()
            if self.ProximoEvento == 8:
                self.partidaS4()
            if self.ProximoEvento == 9:
                self.arriboS5()
            if self.ProximoEvento == 10:
                self.partidaS5()
            if self.Reloj > 800:
                break
        self.reportes()


    def tiempos(self):
        self.Proximo = 0
        self.Menor = 1
        for i in range(0, 10):
            if self.ListaDeEventos(i) < self.ListaDeEventos(self.Menor):
                self.Menor = i
        self.TiempoUltimoEvento = self.Reloj
        self.Proximo = self.Menor
        self.Reloj = self.ListaDeEventos(self.Menor)


    def arriboS1(self):
        self.ListaDeEventos[0] = valorExponencial(self.TMArribos) + self.Reloj
        if self.EstadoServidor[0] == 'D':
            self.EstadoServidor[0] == 'O'
            self.ListaDeEventos[1] = valorExponencial(self.TMServidor1) + self.Reloj
        else:
            self.TamañoCola[0] += 1


    def partidaS1(self):
        if self.TamañoCola[0] > 0:
            self.ListaDeEventos[1] = valorExponencial(self.TMServidor1) + self.Reloj
            self.TamañoCola[0] -= 1
        else:
            self.EstadoServidor[0] == 'D'
        self.ListaDeEventos[2] = self.Reloj
        self.ListaDeEventos[4] = self.Reloj


    def arriboS2(self):
        if self.EstadoServidor[1] == 'D':
            self.EstadoServidor[1] == 'O'
            self.ListaDeEventos[3] = valorExponencial(self.TMServidor2) + self.Reloj
        else:
            self.TamañoCola[1] += 1


    def partidaS2(self):
        if self.TamañoCola[1] > 0:
            self.ListaDeEventos[3] = valorExponencial(self.TMServidor2) + self.Reloj
            self.TamañoCola[1] -= 1
        else:
            self.EstadoServidor[1] == 'D'
        self.ListaDeEventos[6] = self.Reloj
        self.Tipo = 'S'


    def arriboS3(self):
        if self.EstadoServidor[2] == 'D':
            self.EstadoServidor[2] == 'O'
            self.ListaDeEventos[5] = valorExponencial(self.TMServidor3) + self.Reloj
        else:
            self.TamañoCola[2] += 1


    def partidaS3(self):
        if self.TamañoCola[2] > 0:
            self.ListaDeEventos[5] = valorExponencial(self.TMServidor3) + self.Reloj
            self.TamañoCola[2] -= 1
        else:
            self.EstadoServidor[2] == 'D'
        self.ListaDeEventos[6] = self.Reloj
        self.Tipo = 'P'


    def arriboS4(self):
        if self.EstadoServidor[3] == 'D':
            if (self.TamañoCola[3]>0) and (self.TamañoCola[4]>0):
                self.EstadoServidor[3] == 'O'
                if (random.rand(0, 1) < 0.12) or (random.rand(0, 1) < 0.1):
                    self.ListaDeEventos[7] = valorExponencial(self.TMServidor4d) + self.Reloj
                else:
                    self.ListaDeEventos[7] = valorExponencial(self.TMServidor4n) + self.Reloj
        else:
            if(self.Tipo=='S'):
                self.TamañoCola[3] += 1
            else:
                self.TamañoCola[4] += 1


    def partidaS4(self):
        if (self.TamañoCola[3] > 0) and (self.TamañoCola[4] > 0):
            if (random.rand(0, 1) < 0.12) or (random.rand(0, 1) < 0.1):
                self.ListaDeEventos[7] = valorExponencial(self.TMServidor4d) + self.Reloj
            else:
                self.ListaDeEventos[7] = valorExponencial(self.TMServidor4n) + self.Reloj
            self.TamañoCola[3] -= 1
            self.TamañoCola[4] -= 1
        else:
            self.EstadoServidor[3] == 'D'
        self.ListaDeEventos[8] = self.Reloj


    def arriboS5(self):
        if self.EstadoServidor[4] == 'D':
            self.EstadoServidor[4] == 'O'
            self.ListaDeEventos[9] = valorExponencial(self.TMServidor5) + self.Reloj
        else:
            self.TamañoCola[5] += 1


    def partidaS5(self):
        if self.TamañoCola[5] > 0:
            self.ListaDeEventos[9] = valorExponencial(self.TMServidor5) + self.Reloj
            self.TamañoCola[5] -= 1
        else:
            self.EstadoServidor[2] == 'D'





#---------------------------------------------
# Funciones
#---------------------------------------------
def valorExponencial(media):
    return np.random.exponential(media)


#---------------------------------------------
# Ejecucion del modelo
#---------------------------------------------

sim1 = Simulacion()
sim1.programaPrincipal()
