import csv
import sys
sys.path.append("C:/Users/CHEZ/Documents/finalProgra/controlador/modelo")
from conexion import singleton  
from datoAgua import datoAgua

def validar(texto):
	
	textoAuxiliar = texto.get()	 
	
	if textoAuxiliar[-3,(len(textoAuxiliar)-1)] == "csv" or textoAuxiliar[-3,(len(textoAuxiliar)-1)] == "CSV" :
		leerArchivo(textoAuxiliar)
	else:
		texto.set("Archivo no valido")
		
def leerArchivo(rutaArchivo):
	conector = singleton.Singleton()
	with open (rutaArchivo) as archivoCSV : 
		lector = csv.reader(archivoCSV)
		for dato in lector:
			datoCarga = datoAgua(dato[0], dato[1])
			
		 
leerArchivo('C:/Users/CHEZ/Desktop/ConsumoEnergiaComercial.csv')