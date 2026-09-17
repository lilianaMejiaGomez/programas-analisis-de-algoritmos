import matplotlib.pyplot as plt
import ordenamientos
import benchmark

#lista
tamanos = [10, 100, 200, 300, 350]

#algoritmo
tiempos_selection = []
tiempos_bubble = []
tiempos_insertion = []
tiempos_gnome = []
tiempos_exchange = []
#tiempos_stooge = []
tiempos_merge = []
tiempos_quick = []

#tamaño
for n in tamanos:
    datos = benchmark.generar_datos(n)
    
    tiempo = benchmark.medir_tiempo(ordenamientos.selection_sort, datos)
    tiempos_selection.append(tiempo)
    
    tiempo = benchmark.medir_tiempo(ordenamientos.bubble_sort, datos)
    tiempos_bubble.append(tiempo)
    
    tiempo = benchmark.medir_tiempo(ordenamientos.insertion_sort, datos)
    tiempos_insertion.append(tiempo)
    
    tiempo = benchmark.medir_tiempo(ordenamientos.gnome_sort, datos)
    tiempos_gnome.append(tiempo)
    
    tiempo = benchmark.medir_tiempo(ordenamientos.exchange_sort, datos)
    tiempos_exchange.append(tiempo)
    
    #tiempo = benchmark.medir_tiempo(ordenamientos.stooge_sort, datos)
    #tiempos_stooge.append(tiempo)

    tiempo = benchmark.medir_tiempo(ordenamientos.merge_sort, datos)
    tiempos_merge.append(tiempo)

    tiempo = benchmark.medir_tiempo(ordenamientos.quick_sort, datos)
    tiempos_quick.append(tiempo)
    
#grafica algoritmo
plt.plot(tamanos, tiempos_selection, label="Selection", marker="o")
plt.plot(tamanos, tiempos_bubble, label="Bubble", marker="o")
plt.plot(tamanos, tiempos_insertion, label="Insertion", marker="o")
plt.plot(tamanos, tiempos_gnome, label="Gnome", marker="o")
plt.plot(tamanos, tiempos_exchange, label="Exchange", marker="o")
#plt.plot(tamanos, tiempos_stooge, label="Stooge", marker="o")
plt.plot(tamanos, tiempos_merge, label="Merge", marker="o")
plt.plot(tamanos, tiempos_quick, label="Quick", marker="o")
plt.title("Comparación de Tiempos de Ordenamiento")
plt.xlabel("Cantidad de números en la lista (N)")
plt.ylabel("Tiempo que tardó (segundos)")
plt.legend()
plt.grid(True)
plt.show()
