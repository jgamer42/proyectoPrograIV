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
    
    def consultar_mes_agua(tabla):
        print("mes agua")
        entrada_BD = sqlite3.connect("mediciones")
        puntero = entrada_BD.cursor()
        if(tabla == "natural"):
            puntero.execute("SELECT * FROM agua_residencial WHERE fecha LIKE '%%/05/2020 %%' ")
        else:
            puntero.execute("SELECT * FROM agua_comercial WHERE fecha LIKE '%%/05/2020 %%' ")
        datos = puntero.fetchall()
        entrada_BD.close()
        return(datos)
    
    def consultar_dia_agua(tabla):
        print("dia agua")
        entrada_BD = sqlite3.connect("mediciones")
        puntero = entrada_BD.cursor()
        if(tabla == "natural"):
            puntero.execute("SELECT * FROM agua_residencial WHERE fecha LIKE '16/05/2020 %%' ")
        else:
            puntero.execute("SELECT * FROM agua_comercial WHERE fecha LIKE '16/05/2020 %%' ")
        datos = puntero.fetchall()
        entrada_BD.close()
        return(datos)
    
    def consultar_mes_energia(tabla):
        print("mes energia")
        entrada_BD = sqlite3.connect("mediciones")
        puntero = entrada_BD.cursor()
        if(tabla == "natural"):
            puntero.execute("SELECT * FROM energia_residencial WHERE fecha LIKE '%%/05/2020 %%' ")
        else:
            puntero.execute("SELECT * FROM energia_comercial WHERE fecha LIKE '%%/05/2020 %%' ")
        datos = puntero.fetchall()
        entrada_BD.close()
        return(datos)
    
    def consultar_dia_energia(tabla):
        print("dia energia")
        entrada_BD = sqlite3.connect("mediciones")
        puntero = entrada_BD.cursor()
        if(tabla == "natural"):
            puntero.execute("SELECT * FROM energia_residencial WHERE fecha LIKE '16/05/2020 %%' ")
        else:
            puntero.execute("SELECT * FROM energia_comercial WHERE fecha LIKE '16/05/2020 %%' ")
        datos = puntero.fetchall()
        entrada_BD.close()
        return(datos)


class singelton():
    def __init__(self):
        self.cls = conexion
    def singelton(self):
        if(not self.cls._instance):
            self.cls._instance = self.cls()
        return(self.cls)

