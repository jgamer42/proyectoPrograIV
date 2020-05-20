from tkinter import *
import sys

sys.path.append("C:/Users/CHEZ/Documents/finalProgra/controlador")
import controladorValida

class Apertura():
	def __init__(self,texto):
		self.miframe= Frame()
		self.texto = Label(self.miframe,textvariable=texto).grid(row = 0, column = 1)
		self.boton = Button(text="Leer archivo")
		

		