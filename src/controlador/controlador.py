from tkinter import filedialog 
import sys
sys.path.append("/home/crinto/proyectos/proyecto_dani/src/vista/")
dirArchivo = None
from persona_juridica import Persona_juridica
from persona_natural import Persona_natural
def cargar_vista(frame,texto):
    frame.destroy()
    if(texto == "natural"):
        vista = Persona_natural()
    elif(texto == "juridica"):
        vista = Persona_juridica()
    frame = vista.frame
    frame.pack()
def BuscarArchivo(texto): 
	global dirArchivo
	filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files","*.txt*"),("all files", "*.*"))) 
	texto.set("File Opened: " + filename)
	dirArchivo = filename 
	print(dirArchivo)  