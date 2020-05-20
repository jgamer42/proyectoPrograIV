import tkinter
#from conrolador import controladorBotones

class vistaPrincipal():
	"""docstring for vistaPrincipal"""
	def __init__(self):
		
		self.miframe= tkinter.Frame()
		#miframe.pack()
		self.dia = tkinter.Button(self.miframe, text="dia").grid(row=1,column=0)
		self.semana = tkinter.Button(self.miframe, text="semana").grid(row=2,column=0 )
		self.Mes = tkinter.Button(self.miframe, text="Mes").grid(row=3,column=0)