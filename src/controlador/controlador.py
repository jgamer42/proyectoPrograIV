from tkinter import filedialog 
import sys
sys.path.append("/home/crinto/proyectos/proyecto_dani/src/vista/")
from persona_juridica import Persona_juridica
from persona_natural import Persona_natural
from menu_insertar import Menu_insertar
direccion_archivo = None
def cargar_vista(frame,texto):
    frame.destroy()
    if(texto == "natural"):
        vista = Persona_natural()
    elif(texto == "juridica"):
        vista = Persona_juridica()
    elif(texto == "insertar"):
        vista = Menu_insertar(direccion_archivo)
    frame = vista.frame
    frame.pack()

def buscar_archivo():
    global direccion_archivo
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("CSV","*.csv*"),("all files", "*.*")))
    direccion_archivo = filename
    print(direccion_archivo)

