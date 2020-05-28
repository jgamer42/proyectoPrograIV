from conexion2 import singelton
class Dato():
	def __init__(self):
		self.consumo = None
		self.fecha = None
		self.lista_observadores = []
		self.estado = None
		self.conexion = singelton().singelton()

	def agregar_observador(self,nuevo_observador):
		self.lista_observadores.append(nuevo_observador)
	
	def set_estado(self,nuevo_estado):
		self.estado = nuevo_estado
		self.notificar()

	def notificar(self):
		for observador in self.lista_observadores:
			observador.notificar()

	def printer(self):
		print(self.fecha,self.consumo)
	
	def insertar(self,fecha,consumo):
		self.set_estado("nuevo dato")
		self.fecha = fecha
		self.consumo = consumo
		self.conexion.insertar(fecha,consumo)
		self.printer()
		