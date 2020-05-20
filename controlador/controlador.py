#from modelo import conexion
from .vista.apertura import Apertura
from tkinter import filedialog 

dirArchivo = None

def Valida(frame,texto):
	
	frame.destroy()
	vista = Apertura(texto)
	frame = vista.miframe
	frame.pack()
	
def BuscarArchivo(texto): 
	global dirArchivo
	filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files","*.txt*"),("all files", "*.*"))) 
	texto.set("File Opened: " + filename)
	dirArchivo = filename 
	print(dirArchivo)  