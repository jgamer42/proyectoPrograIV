from tkinter import *
from vista_base import Vista_base
import sys

class Persona_natural(Vista_base):
    def __init__(self):
        super().__init__()
        Label(self.frame,text="graficar").grid(row = 0,column=0)
        Button(self.frame,text="consumo agua").grid(row = 1,column=0)
        Button(self.frame,text="consumo energia").grid(row = 2,column=0)