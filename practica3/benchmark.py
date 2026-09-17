
import time
import random

def generar_datos(tamano):
    # Creamos una lista vacía
    lista = []
    
    #cantidad de tamaño
    for i in range(tamano):
        numero = random.randint(0, 1000) # Número al azar entre 0 y 1000
        lista.append(numero)             # Lo agregamos a la lista de listas
        
    return lista

def medir_tiempo(algoritmo, lista):
    #inico del tiempo
    inicio = time.time()
    
    # se ejecuta algoritmo
    algoritmo(lista)
    
    #fin del tiempo
    fin = time.time()
    
    #se calcula el fin y el inico como resta(-)
    tiempo_total = fin - inicio
    
    return tiempo_total
#retorna en tiempo total del fin e inicio

