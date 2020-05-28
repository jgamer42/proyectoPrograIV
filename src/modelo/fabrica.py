from fabrica_agua import Fabrica_agua
from fabrica_energia import Fabrica_energia
class Fabrica():
    def crear_fabrica(self,tipo):
        fabrica = None
        if(tipo == "agua"):
            fabrica = Fabrica_agua()
        else:
            fabrica = Fabrica_energia()
        return(fabrica)