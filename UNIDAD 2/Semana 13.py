import tkinter as tk
from tkinter import messagebox

# Función para agregar el texto a la lista
def agregar():
    texto = entry.get()
    if texto:
        lista.insert(tk.END, texto)
        entry.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío.")

# Función para limpiar la lista o el campo de texto
def limpiar():
    entry.delete(0, tk.END)  # Limpiar el campo de texto
    lista.delete(0, tk.END)  # Limpiar la lista

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación de Ejemplo")

# Etiqueta para el campo de texto
label = tk.Label(root, text="Ingrese información:")
label.pack(pady=5)

# Campo de texto
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Botón para agregar información
btn_agregar = tk.Button(root, text="Agregar", command=agregar)
btn_agregar.pack(pady=5)

# Lista para mostrar los datos agregados
lista = tk.Listbox(root, width=50, height=10)
lista.pack(pady=5)

# Botón para limpiar la lista
btn_limpiar = tk.Button(root, text="Limpiar", command=limpiar)
btn_limpiar.pack(pady=5)

# Ejecutar la ventana principal
root.mainloop()
