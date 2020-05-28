from tkinter import *
from vista_base import Vista_base
import sys

class Persona_natural(Vista_base):
    def __init__(self):
        super().__init__()
        Button(self.frame,text="grafico consumo por dia agua").grid(row = 1,column=1)
        Button(self.frame,text="grafico consumo por semana agua").grid(row = 2,column=1)
        Button(self.frame,text="grafico consumo por mes agua").grid(row = 3,column=1)
        Button(self.frame,text="grafico consumo por dia energia").grid(row = 1,column=2)
        Button(self.frame,text="grafico consumo por semana energia").grid(row = 2,column=2)
        Button(self.frame,text="grafico consumo por mes energia").grid(row = 3,column=2)