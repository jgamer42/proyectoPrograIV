from tkinter import *
from vista_base import Vista_base
import sys

class Persona_juridica(Vista_base):
    def __init__(self):
        super().__init__()
        Button(self.frame,text="grafico consumo por dia").grid(row = 1,column=1)
        Button(self.frame,text="grafico consumo por semana").grid(row = 2,column=1)
        Button(self.frame,text="grafico consumo por mes").grid(row = 3,column=1)