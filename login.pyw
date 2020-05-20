from tkinter import *
from controlador import controlador
   
window = Tk() 
window.title('File Explorer') 
container=Frame(window)
labelText = StringVar(value="Cargue su archivo CSV")
label_file_explorer = Label(container,textvariable = labelText) 
   
       
button_explore = Button(container,text = "Browse Files",command=lambda:(controlador.BuscarArchivo(labelText),controlador.Valida(container,labelText)))
   
button_exit = Button(container,text = "Exit",command = exit)  
    
label_file_explorer.grid(column = 1, row = 1) 
   
button_explore.grid(column = 1, row = 2) 
   
button_exit.grid(column = 1,row = 3) 
   
container.pack()
window.mainloop()