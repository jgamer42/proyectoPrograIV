from tkinter import filedialog 
import sys
sys.path.append("/home/crinto/proyectos/proyecto_dani/src/vista/")
from persona_juridica import Persona_juridica
from persona_natural import Persona_natural
from insertar_datos import Insertar_datos
direccion_archivo = None
def cargar_vista(frame,texto):
    frame.destroy()
    if(texto == "natural"):
        vista = Persona_natural()
    elif(texto == "juridica"):
        vista = Persona_juridica()
    elif(texto == "insertar"):
        vista = Insertar_datos(direccion_archivo)
    frame = vista.frame
    frame.pack()

def buscar_archivo():
    global direccion_archivo
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files","*.txt*"),("all files", "*.*")))
    direccion_archivo = filename