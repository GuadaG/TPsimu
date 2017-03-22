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
        self.Cola1 = []
        self.Cola2 = []
        self.Cola3 = []
        self.Cola4s = []
        self.Cola4p= []
        self.Cola5 = []
        self.EstadoServidor= []
        self.TMArribos = 10.0
        self.TMServidor1 = 6.0
        self.TMServidor2 = 4.0
        self.TMServidor3 = 5.0
        self.TMServidor4n = 5.0
        self.TMServidor4d = 8.0
        self.TMServidor5 = 12.0
        self.TiempoUltimoEvento = 0.0
        self.TiempoTotalServidor = []
        self.TiempoTotalSistema = 0
        self.Tipo = ''
        self.Menor = 0
        self.CantClientesAtendidos = []
        self.TamanioCola = []



    def inicializacion(self):
        self.ListaDeEventos.append(valorExponencial(self.TMArribos))
        for j in range(0, 9):
            self.ListaDeEventos.append(9999.99)
        for i in range(0, 5):
            self.EstadoServidor.append('D')
            self.TiempoTotalServidor.append(0)
            self.CantClientesAtendidos.append(0)
        for k in range(0, 6):
            self.TamanioCola.append(0)
        self.TiempoUltimoEvento = 0


    def programaPrincipal(self):
            self.inicializacion()
            while self.Reloj<600:
                self.tiempos()
                if self.ProximoEvento == 0:
                    self.arriboS1()
                if self.ProximoEvento == 1:
                    self.partidaS1()
                if self.ProximoEvento == 2:
                    self.arriboS2()
                if self.ProximoEvento == 3:
                    self.partidaS2()
                if self.ProximoEvento == 4:
                    self.arriboS3()
                if self.ProximoEvento == 5:
                    self.partidaS3()
                if self.ProximoEvento == 6:
                    self.arriboS4()
                if self.ProximoEvento == 7:
                    self.partidaS4()
                if self.ProximoEvento == 8:
                    self.arriboS5()
                if self.ProximoEvento == 9:
                    self.partidaS5()

            self.reportes()


    def tiempos(self):
        self.ProximoEvento = 0
        self.Menor = 1
        #print ("0  ", self.ListaDeEventos[0])
        #print ("1  ", self.ListaDeEventos[1])
        for i in range(0, 10):
            #print ("i  ", self.ListaDeEventos[i])
            #print ("menor  ", self.ListaDeEventos[self.Menor])
            if self.ListaDeEventos[i] <= self.ListaDeEventos[self.Menor]:
                self.Menor = i
        self.TiempoUltimoEvento = self.Reloj
        self.ProximoEvento = self.Menor
        self.Reloj = self.ListaDeEventos[self.Menor]
        print (self.Menor)



    def arriboS1(self):
        self.ListaDeEventos[0] = valorExponencial(self.TMArribos) + self.Reloj
        if self.EstadoServidor[0] == 'D':
            self.EstadoServidor[0] == 'O'
            self.CantClientesAtendidos[0] += 1
            self.ListaDeEventos[1] = valorExponencial(self.TMServidor1) + self.Reloj
        else:
            self.Cola1.append(self.Reloj)
            self.TamanioCola[0] += 1


    def partidaS1(self):
        if self.TamanioCola[0] > 0:
            self.ListaDeEventos[1] = valorExponencial(self.TMServidor1) + self.Reloj
            self.TamanioCola[0] -= 1
            self.TiempoTotalServidor[0] += self.Reloj - self.Cola1[0]
            self.Cola1.pop(0)
            self.CantClientesAtendidos[0] += 1
        else:
            self.EstadoServidor[0] == 'D'
        self.ListaDeEventos[2] = self.Reloj
        self.ListaDeEventos[4] = self.Reloj
        print ("arribo 2  ", self.ListaDeEventos[2])
        print ("arribo 3  ", self.ListaDeEventos[4])


    def arriboS2(self):
        if self.EstadoServidor[1] == 'D':
            self.EstadoServidor[1] == 'O'
            self.CantClientesAtendidos[1] += 1
            self.ListaDeEventos[3] = valorExponencial(self.TMServidor2) + self.Reloj
        else:
            self.Cola2.append(self.Reloj)
            self.TamanioCola[1] += 1


    def partidaS2(self):
        if self.TamanioCola[1] > 0:
            self.ListaDeEventos[3] = valorExponencial(self.TMServidor2) + self.Reloj
            self.TiempoTotalServidor[1] += self.Reloj - self.Cola2[0]
            self.Cola2.pop(0)
            self.TamanioCola[1] -= 1
            self.CantClientesAtendidos[1] += 1
        else:
            self.EstadoServidor[1] == 'D'
        self.ListaDeEventos[6] = self.Reloj
        self.Tipo = 'S'


    def arriboS3(self):
        if self.EstadoServidor[2] == 'D':
            self.EstadoServidor[2] == 'O'
            self.ListaDeEventos[5] = valorExponencial(self.TMServidor3) + self.Reloj
            self.CantClientesAtendidos[2] += 1
        else:
            self.Cola3.append(self.Reloj)
            self.TamanioCola[2] += 1


    def partidaS3(self):
        if self.TamanioCola[2] > 0:
            self.ListaDeEventos[5] = valorExponencial(self.TMServidor3) + self.Reloj
            self.TiempoTotalServidor[2] += self.Reloj - self.Cola3[0]
            self.Cola3.pop(0)
            self.TamanioCola[2] -= 1
            self.CantClientesAtendidos[2] += 1
        else:
            self.EstadoServidor[2] == 'D'
        self.ListaDeEventos[6] = self.Reloj
        self.Tipo = 'P'


    def arriboS4(self):
        if self.EstadoServidor[3] == 'D':
            if (self.TamanioCola[3]>0) and (self.TamanioCola[4]>0):
                self.EstadoServidor[3] == 'O'
                self.CantClientesAtendidos[3] += 1
                if (random.rand(0, 1) < 0.12) or (random.rand(0, 1) < 0.1):
                    self.ListaDeEventos[7] = valorExponencial(self.TMServidor4d) + self.Reloj
                else:
                    self.ListaDeEventos[7] = valorExponencial(self.TMServidor4n) + self.Reloj
        else:
            if(self.Tipo=='S'):
                self.Cola4s.append(self.Reloj)
                self.TamanioCola[3] += 1
            else:
                self.Cola4p.append(self.Reloj)
                self.TamanioCola[4] += 1


    def partidaS4(self):
        if (self.TamanioCola[3] > 0) and (self.TamanioCola[4] > 0):
            self.CantClientesAtendidos[3] += 1
            if (random.rand(0, 1) < 0.12) or (random.rand(0, 1) < 0.1):
                self.ListaDeEventos[7] = valorExponencial(self.TMServidor4d) + self.Reloj
            else:
                self.ListaDeEventos[7] = valorExponencial(self.TMServidor4n) + self.Reloj
            if self.Cola4s[0] < self.Cola4p[0]:
                self.TiempoTotalServidor[3] += self.Reloj - self.Cola4s[0]
            else:
                self.TiempoTotalServidor[3] += self.Reloj - self.Cola4p[0]
            self.Cola4s.pop(0)
            self.Cola4p.pop(0)
            self.TamanioCola[3] -= 1
            self.TamanioCola[4] -= 1
        else:
            self.EstadoServidor[3] == 'D'
        self.ListaDeEventos[8] = self.Reloj


    def arriboS5(self):
        if self.EstadoServidor[4] == 'D':
            self.EstadoServidor[4] == 'O'
            self.ListaDeEventos[9] = valorExponencial(self.TMServidor5) + self.Reloj
            self.CantClientesAtendidos[4] += 1
        else:
            self.Cola5.append(self.Reloj)
            self.TamanioCola[5] += 1


    def partidaS5(self):
        if self.TamanioCola[5] > 0:
            self.ListaDeEventos[9] = valorExponencial(self.TMServidor5) + self.Reloj
            self.TiempoTotalServidor[4] += self.Reloj - self.Cola5[0]
            self.Cola5.pop(0)
            self.TamanioCola[5] -= 1
            self.CantClientesAtendidos[4] += 1
        else:
            self.EstadoServidor[2] == 'D'


    def reporte(self):
        salida = open('TPSimu.csv', 'w')

        for i in range (0, 5):
            salida.write('Tiempo medio en servidor ('+str(i+1) + ');')
            salida.write(str(self.TiempoTotalServidor[i]/self.CantClientesAtendidos[i]) + ';')
            salida.write('\n')
            self.TiempoTotalSistema += self.TiempoTotalServidor[i]/self.CantClientesAtendidos[i]


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
