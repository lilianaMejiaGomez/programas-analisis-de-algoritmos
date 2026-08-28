import tkinter as tk
import matplotlib.pyplot as plt

# Datos para la gráfica
x = [3, 4, 5, 6, 7]
y = [10, 11, 14, 16, 18]

plt.plot(x, y) # Gráfica de línea
plt.scatter(x, y, color="red") # Gráfica de puntos
# plt.bar(x, y) # Gráfica de barras
plt.title("Mi primera grafica")
plt.xlabel("eje x")
plt.ylabel("eje y")
plt.show()

def saludar():
    nombre = entrada.get().strip()
    if not nombre:
        nombre = "Liliana"
    lbl.config(text=f"Hola {nombre}!!! ")

# Configuración de la ventana
root = tk.Tk()
root.title("Saludador")
root.geometry("500x500")

lbl = tk.Label(root, text="EH MIEDOTE, Escribe tu nombre y presiona el botón", background="yellow", foreground="red")
lbl.pack(pady=10)

entrada = tk.Entry(root)
entrada.pack(pady=10)

bot = tk.Button(root, text="Saludar", command=saludar)
bot.pack(pady=10)

root.mainloop()
