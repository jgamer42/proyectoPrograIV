from conexion2 import singelton
class datoBase():
	def __init__(self, fecha, consumo):
		self.consumo = consumo
		self.fecha = fecha
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