# Aplicación gráfica, ventana que permite dar dos ciudades y obtener el clima de ambas

import tkinter as tk
from tkinter import Toplevel, Label
from consultas_api import *
from PIL import Image, ImageTk

def obtener_clima():
    ciudad1 = entry1.get()
    ciudad2 = entry2.get()
    result1, result2 = dar_clima_ciudades(ciudad1, ciudad2)
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry1.insert(0, result1)
    entry2.insert(0, result2)


# Función para mostrar la información del caché en una ventana emergente
def mostrar_cache():
    ventana_cache = Toplevel(root)
    ventana_cache.title("Información del Cache")
    
    # Crear una etiqueta para mostrar la información del caché
    etiqueta_cache = Label(ventana_cache, text=str(cache))
    etiqueta_cache.pack(padx=20, pady=20)


root = tk.Tk()
root.title("Clima de ciudades")
root.configure(bg="#84b6f4")
root.geometry("500x300") 

# Imagen 
can = tk.Canvas(root, width=500, height=200)
can.grid(row=0, column=0, columnspan=2)
img = Image.open("img.jpg")
img = img.resize((500, 200))
img = ImageTk.PhotoImage(img)
can.create_image(500/2, 200/2, image=img)

label1 = tk.Label(root, text="Ciudad 1", bg="#84b6f4")
label1.grid(row=1, column=0)

entry1 = tk.Entry(root, width=50)
entry1.grid(row=1, column=1)

label2 = tk.Label(root, text="Ciudad 2", bg="#84b6f4")
label2.grid(row=2, column=0)

entry2 = tk.Entry(root, width=50)
entry2.grid(row=2, column=1)


button = tk.Button(root, text="Obtener clima", command=obtener_clima)
button.grid(row=3, column=1)

boton_consultar_cache = tk.Button(root, text="Consultar cache", command=mostrar_cache)
boton_consultar_cache.grid(row=4, column=0)


root.mainloop()