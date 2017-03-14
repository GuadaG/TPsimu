import numpy as np
import time
from collections import deque
from array import *
import operator



class Simulacion(object):

    def __init__(self):
        self.Reloj = 0.0
        self.ListaDeEventos = []
        self.Cola = []
        self.EstadoServidor= []
        self.TMArribos = 10.0
        self.TMServidor1 = 6.0
        self.TMServidor2 = 4.0
        self.TMServidor3 = 5.0
        self.TMServidor4n = 5.0
        self.TMServidor4d = 8.0
        self.TMServidor5 = 12.0
        self.TiempoUltimoEvento = 0.0
        self.NroDeMaqEnCola = 0
        self.Menor = 0



    def inicializacion(self):
        self.Reloj=0
        for i in range(0, 5):
            self.ListaDeEventos.append(valorExponencial(self.TMArribos))
            self.Cola.append(99999.0)
        for k in range(0, 5):
            self.EstadoOperario.append('D')
            self.ListaDeEventos.append(99999.0)
            self.ListaMaquinaOperario.append('')
        self.TMaqRotas = 0
        self.TiempoUltimoEvento = 0
        self.NroDeMaqEnCola = 0


    def programaPrincipal(self):
        self.inicializacion()
        while True:
            self.tiempos()
            if self.ProximoEvento == "Rotura":
                self.roturaMaquina()
            else:
                self.finReparacion()

            if self.Reloj > 800:
                break
        self.reportes()


    def tiempos(self):
        self.Menor = 0
        for i in range(5 + self.NroOperarios):
            if self.ListaDeEventos[i] < self.ListaDeEventos[self.Menor]:
                self.Menor=i
        self.Reloj=self.ListaDeEventos[self.Menor]
        if (self.Menor<5):
           self.ProximoEvento = "Rotura"
        else:
           self.ProximoEvento = "Reparacion"
        print(self.ProximoEvento)


    def roturaMaquina(self):
        NroOp = None
        for i in range(0, self.NroOperarios):
            print (self.EstadoOperario[i])
            if self.EstadoOperario[i]== 'D':
                NroOp = i

                break
        if (NroOp is not None):
            self.EstadoOperario[NroOp]= 'O'
            self.ListaDeEventos[5 + NroOp] = self.Reloj + valorExponencial(self.TMDeReparacion)
            self.ListaMaquinaOperario[NroOp] = self.Menor
            print(self.ListaDeEventos[5 + NroOp])
        else:
            self.NroDeMaqEnCola += 1
            self.Cola[self.Menor] = valorExponencial(self.TMDeReparacion)


    def finReparacion(self):
        min = 1
        self.TMaqRotas += (self.Reloj - self.ListaDeEventos[self.ListaMaquinaOperario[self.Menor]])
        if (self.NroDeMaqEnCola != 0):
            for i in range(self.Cola.__sizeof__()):
                if (self.Cola[i] < self.Cola[min]):
                    min = i
            #generar prox reparacion desde operario j (self.Menor)
            self.ListaDeEventos[self.Menor] = self.Reloj + self.Cola[min] #creo que esta mal
            #guardo nro de maquina que va a reparar
            self.ListaMaquinaOperario[self.Menor - 5] = min
            self.NroDeMaqEnCola -= 1
        else:
            self.EstadoOperario[self.Menor-5]='D'
            self.ListaDeEventos[self.Menor] = 99999.0
        #generar prox rotura de maquina que repare
        self.ListaDeEventos[self.ListaMaquinaOperario[self.Menor]] = self.Reloj + valorExponencial(self.TMEntreRoturas)



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
