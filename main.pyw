from tkinter import *
from src.controlador import controlador

ventana = Tk() 
ventana.title('proyecto progra') 
contenedor=Frame(ventana)
Label(contenedor,text="¿que tipo de cliente es?").grid(column=1, row=1) 
Button(contenedor,text = "Natural",command=lambda:controlador.cargar_vista(contenedor,"natural")).grid(column=1, row = 2)
Button(contenedor,text = "Juridico",command=lambda:controlador.cargar_vista(contenedor,"juridica")).grid(column=1, row = 3)  
Button(contenedor,text = "salir",command = exit).grid(column=1,row=4) 
contenedor.pack()
ventana.mainloop()