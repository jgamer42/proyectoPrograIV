import sqlite3
class conexion:
    _instance = None
    def foo(self):
        return id(self)
     #esta clase lleva la logica de la conexion
    def printer(self):
     	print("aqui")
     	
    def insertar(self,datosInsertar):
    	pass
    	
     	
     	
class singleton():
	sel.cls = conexion
	def Singleton(self):
		if (not self.cls._instance):
			self.cls._instance = cls()
		return self.cls._instance	


