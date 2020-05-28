import csv 
import sys
sys.path.append("/home/crinto/proyectos/proyecto_dani/src/modelo/")
from dato import Dato
from observador import Observador
from tkinter import filedialog
datos_insertar=[]

def leer_archivo(direccion_archivo):
    global datos_insertar
    with open(direccion_archivo,"r") as archivo:
        lector = csv.reader(archivo)
        for dato in lector:
            dato_leido=(dato)
            datos_insertar.append(dato_leido)
    archivo.close()

def insertar(tabla_insertar):
    global datos_insertar
    dato_insertar = Dato()
    observador_insertar = Observador(dato_insertar)
    dato_insertar.set_estado("creando")
    for medida in datos_insertar:
        dato_insertar.insertar(medida[0],medida[1])

