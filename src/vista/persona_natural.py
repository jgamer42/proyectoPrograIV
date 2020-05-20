from tkinter import *
from vista_base import Vista_base
import sys

class Persona_natural(Vista_base):
    def __init__(self):
        super().__init__()
        Button(self.frame,text="graficar").grid(row = 1,column=1)