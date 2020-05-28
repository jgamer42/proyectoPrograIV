import sqlite3
class  conexion():
    _instance = None
    #def __init__(self):
        #conexion = sqlite3.connect("prueba")
        #cursor = conexion.cursor()
        #cursor.execute("CREATE TABLE consumo_agua (fecha DATE,)")
        #conexion.close()


    def foo(self):
        return id(self)

    def printer(self):
        print("hola")

class singelton():
    def __init__(self):
        self.cls = conexion
    def singelton(self):
        if(not self.cls._instance):
            self.cls._instance = self.cls()
        return(self.cls)

