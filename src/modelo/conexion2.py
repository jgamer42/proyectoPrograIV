import sqlite3
class  conexion():
    _instance = None

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

