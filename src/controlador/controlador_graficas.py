import sys
sys.path.append("/home/crinto/proyectos/proyecto_dani/src/modelo/")
from fabrica import Fabrica
import matplotlib.pyplot as plt
def printer():
    plt.plot([5,6,7,8])
    plt.show()

def consultar_dia(tabla,tipo):
    lista_datos = []
    lista_horas = []
    lector_medicion = Fabrica().crear_fabrica(tipo)
    datos = lector_medicion.consultar_dia(tabla)
    for dato in datos:
        aux = dato[1]
        lista_datos.append(aux)
        aux = dato[0]
        aux = int(aux[11:-3])
        lista_horas.append(aux)
    plt.plot(lista_horas,lista_datos)
    plt.show()
    

def consultar_semana(tabla,tipo):
    lector_medicion = Fabrica().crear_fabrica(tipo)
    datos = lector_medicion.consultar_mes(tabla)
    datos_semana=promediar_semana(datos)
    plt.plot(["lunes","martes","miercoles","jueves","viernes","sabado","domingo"],datos_semana)
    plt.show()

def consultar_mes(tabla,tipo):
    lector_medicion = Fabrica().crear_fabrica(tipo)
    datos = lector_medicion.consultar_mes(tabla)
    datos_grafico = promediar_dia(datos)
    plt.plot(datos_grafico[0],datos_grafico[1])
    plt.show()
    
    
def promediar_semana(datos):
    dia_actual= 16
    consumo_promedio_dia = []
    consumo_promedio=0
    for dato in datos:
        dia = dato[0]
        dia = int(dia[0:2])
        if(dia == dia_actual):
            consumo_promedio = consumo_promedio + dato[1]
        else:
            if(dia <= 23):
                consumo_promedio = consumo_promedio/24
                consumo_promedio_dia.append(consumo_promedio)
                dia_actual = dia_actual + 1
                consumo_promedio = 0
    return(consumo_promedio_dia)

def promediar_dia(datos):
    dia_actual= 16
    lista_dias=[]
    consumo_promedio_dia = []
    consumo_promedio=0
    for dato in datos:
        dia = dato[0]
        dia = int(dia[0:2])
        if(dia == dia_actual):
            consumo_promedio = consumo_promedio + dato[1]
        else:
            lista_dias.append(dia_actual)
            consumo_promedio = consumo_promedio/24
            consumo_promedio_dia.append(consumo_promedio)
            dia_actual = dia_actual + 1
            consumo_promedio = 0
    return([lista_dias,consumo_promedio_dia])
    




