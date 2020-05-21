from tkinter import *
from vista_base import Vista_base
import sys

class Insertar_datos(Vista_base):
    def __init__(self,texto):
        super().__init__()
        Label(self.frame,text="insertar datos").grid(row=0,column=0, columnspan=3)
        Label(self.frame,text=texto).grid(row=1,column=0, columnspan=3)
        Button(self.frame,text="grafico consumo residencial agua").grid(row = 2,column=1)
        Button(self.frame,text="grafico consumo residencial energia").grid(row = 3,column=1)
        Button(self.frame,text="grafico consumo empresarial agua").grid(row = 2,column=2)
        Button(self.frame,text="grafico consumo empresarial energia").grid(row = 3,column=2)