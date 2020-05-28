from conexion2 import singelton
class Fabrica_energia():
    def consultar_dia(self,tabla):
        conector = singelton().singelton()
        datos = conector.consultar_dia_energia(tabla)
        return(datos)

    def consultar_mes(self,tabla):
        conector = singelton().singelton()
        datos = conector.consultar_mes_energia(tabla)
        return(datos)
    