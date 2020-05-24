from vista_base import Vista_base
from tkinter import *
import sys
sys.path.append("/home/crinto/proyectos/proyecto_dani/src/controlador/")
import controlador_insertar
class Menu_insertar(Vista_base):
    def __init__(self,direccion_archivo):
        super().__init__()
        Label(self.frame,text="en donde quiere insertar").grid(row=0,column=0,columnspan = 2)
        Label(self.frame,text=direccion_archivo).grid(row=1,column=0,columnspan=2)
        Button(self.frame,text="consumo agua persona juridica").grid(row=2,column=0)
        Button(self.frame,text="consumo energia persona juridica").grid(row=3,column=0)
        Button(self.frame,text="consumo agua persona natural").grid(row=2,column=1)
        Button(self.frame,text="consumo energia persona natural").grid(row=3,column=1)
        #TODO conectar esto al controlador