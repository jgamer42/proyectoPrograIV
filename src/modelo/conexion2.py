import sqlite3
class  conexion():
    _instance = None
    def __init__(self):
        conexion = sqlite3.connect("mediciones")
        cursor = conexion.cursor()
        try:
            cursor.execute("CREATE TABLE auxiliar (fecha Date, consumo INTEGER)")
            print("tabla creada")
        except:
            pass
        conexion.close()
    def foo(self):
        return id(self)

    def printer(self):
        print("hola")
    
    def insertar(fecha_dato,consumo_dato):
        entrada_BD = sqlite3.connect("mediciones")
        puntero = entrada_BD.cursor()
        instruccion_sql = "INSERT INTO auxiliar(fecha,consumo)VALUES(?,?);"
        try:
            datos_insertar =(fecha_dato,consumo_dato)
            puntero.execute(instruccion_sql,datos_insertar)
            entrada_BD.commit()
        except:
            print("algo salio mal")
        entrada_BD.close()

class singelton():
    def __init__(self):
        self.cls = conexion
    def singelton(self):
        if(not self.cls._instance):
            self.cls._instance = self.cls()
        return(self.cls)

