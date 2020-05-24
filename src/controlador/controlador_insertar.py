import csv 
import sys
from tkinter import filedialog
datos_insertar=[]

def leer_archivo(direccion_archivo):
    global datos_insertar
    with open(direccion_archivo,"r") as archivo:
        lector = csv.reader(archivo)
        for dato in lector:
            dato_leido=(dato[0],dato[1])
            datos_insertar.append(datos_insertar)
    archivo.close()
    print(datos_insertar)
