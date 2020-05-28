from tkinter import *
from vista_base import Vista_base
import sys
sys.path.append("/home/crinto/proyectos/proyecto_dani/src/controlador/")
import controlador_graficas as controlador
class Persona_natural(Vista_base):
    def __init__(self):
        super().__init__()
        Button(self.frame,text="grafico consumo por dia agua",command = lambda:controlador.consultar_dia("natural","agua")).grid(row = 1,column=1)
        Button(self.frame,text="grafico consumo por semana agua",command = lambda:controlador.consultar_semana("natural","agua")).grid(row = 2,column=1)
        Button(self.frame,text="grafico consumo por mes agua",command = lambda:controlador.consultar_mes("natural","agua")).grid(row = 3,column=1)
        Button(self.frame,text="grafico consumo por dia energia",command = lambda:controlador.consultar_dia("natural","energia")).grid(row = 1,column=2)
        Button(self.frame,text="grafico consumo por semana energia",command = lambda:controlador.consultar_semana("natural","energia")).grid(row = 2,column=2)
        Button(self.frame,text="grafico consumo por mes energia",command = lambda:controlador.consultar_mes("natural","energia")).grid(row = 3,column=2)