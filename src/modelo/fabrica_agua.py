from conexion2 import singelton
#
class Fabrica_agua():
    def consultar_dia(self,tabla):
        conector = singelton().singelton()
        datos = conector.consultar_dia_agua(tabla)
        return(datos)

    def consultar_mes(self,tabla):
        conector = singelton().singelton()
        datos = conector.consultar_mes_agua(tabla)
        return(datos)