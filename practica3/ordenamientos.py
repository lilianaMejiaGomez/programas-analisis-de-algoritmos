#todos los ordenamientos


#selection
def selection_sort(lista):
    arr = lista.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
if __name__ == "__main__":
    mi_lista = [38, 27, 43, 3, 9, 82, 10]
    print(f"Lista original: {mi_lista}")
    
    lista_ordenada = selection_sort(mi_lista)
    print(f"Lista ordenada: {lista_ordenada}")

#burbuja
def bubble_sort(lista):
    arr = lista.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    mi_lista = [38, 27, 43, 3, 9, 82, 10]
    print(f"Lista original: {mi_lista}")
    
    lista_ordenada = bubble_sort(mi_lista)
    print(f"Lista ordenada: {lista_ordenada}")

#insertion
def insertion_sort(lista):
    arr = lista.copy()
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > clave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave
    return arr

if __name__ == "__main__":
    mi_lista = [38, 27, 43, 3, 9, 82, 10]
    print(f"Lista original: {mi_lista}")
    
    lista_ordenada = insertion_sort(mi_lista)
    print(f"Lista ordenada: {lista_ordenada}")

#gnome
def gnome_sort(lista):
    arr = lista.copy()
    i = 0
    n = len(arr)
    while i < n:
        if i == 0 or arr[i] >= arr[i - 1]:
            i += 1  
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]  
            i -= 1  
    return arr

if __name__ == "__main__":
    mi_lista = [38, 27, 43, 3, 9, 82, 10]
    print(f"Lista original: {mi_lista}")
    
    lista_ordenada = gnome_sort(mi_lista)
    print(f"Lista ordenada: {lista_ordenada}")


#exchange
def exchange_sort(lista):
    arr = lista.copy()
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

if __name__ == "__main__":
    mi_lista = [38, 27, 43, 3, 9, 82, 10]
    print(f"Lista original: {mi_lista}")
    
    lista_ordenada = exchange_sort(mi_lista)
    print(f"Lista ordenada: {lista_ordenada}")


#stooge
#def stooge_sort_rec(arr, l, h):
    #if l >= h:
        #return
    #if arr[l] > arr[h]:
        #arr[l], arr[h] = arr[h], arr[l]
    #if h - l + 1 > 2:
        #t = (h - l + 1) // 3
        #stooge_sort_rec(arr, l, h - t)       
        #stooge_sort_rec(arr, l + t, h)       
        #stooge_sort_rec(arr, l, h - t)       

#def stooge_sort(lista):
    #arr = lista.copy()
    #stooge_sort_rec(arr, 0, len(arr) - 1)
    #return arr2 

#merge
def merge_sort(lista):
    arr = lista.copy()
    # Caso base: si la lista tiene 1 o 0 elementos, ya está ordenada
    if len(arr) <= 1:
        return

    # 1. DIVIDE: Encontrar el punto medio y dividir la lista en dos mitades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 2. VENCE: Llamadas recursivas para ordenar cada mitad
    merge_sort(left_half)
    merge_sort(right_half)

    # 3. COMBINA (Merge): Fusionar las dos mitades ordenadas en la lista original
    i = j = k = 0

    # Comparar elementos de ambas mitades y colocar el menor en 'arr'
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Verificar si quedaron elementos en la mitad izquierda
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    # Verificar si quedaron elementos en la mitad derecha
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

# --- Ejemplo de uso ---
if __name__ == "__main__":
    mi_lista = [38, 27, 43, 3, 9, 82, 10]
    print(f"Lista original: {mi_lista}")
    
    merge_sort(mi_lista)
    print(f"Lista ordenada: {mi_lista}")

   



    #quicky
def quick_sort(lista):
    arr = lista.copy()
    # Caso base: una lista vacía o con un solo elemento ya está ordenada
    if len(arr) <= 1:
        return arr
    
    # Elección del pivote (en este caso, el elemento central)
    pivot = arr[len(arr) // 2]
    
    # Particionamiento de la lista
    izq = [x for x in arr if x < pivot]
    centro = [x for x in arr if x == pivot]
    der = [x for x in arr if x > pivot]
    
    # Llamada recursiva combinando los resultados
    return quick_sort(izq) + centro + quick_sort(der)

# --- Ejemplo de uso ---
if __name__ == "__main__":
    mi_lista = [38, 27, 43, 3, 9, 82, 10]
    print(f"Lista original: {mi_lista}")
    
    lista_ordenada = quick_sort(mi_lista)
    print(f"Lista ordenada: {lista_ordenada}")




