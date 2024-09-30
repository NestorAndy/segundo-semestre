import tkinter as tk
from tkinter import messagebox

# Función para añadir una nueva tarea
def add_task(event=None):
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "Por favor ingrese una tarea.")

# Función para marcar una tarea como completada
def complete_task(event=None):
    try:
        index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(index)
        listbox_tasks.delete(index)
        listbox_tasks.insert(tk.END, f"✔️ {task}")
    except IndexError:
        messagebox.showwarning("Selección", "Por favor seleccione una tarea.")

# Función para eliminar una tarea
def delete_task(event=None):
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        messagebox.showwarning("Selección", "Por favor seleccione una tarea.")

# Función para cerrar la aplicación
def close_app(event=None):
    window.destroy()

# Crear ventana principal
window = tk.Tk()
window.title("Gestor de Tareas")

# Crear el campo de entrada de tareas
entry_task = tk.Entry(window, width=40)
entry_task.grid(row=0, column=0, padx=10, pady=10)

# Crear botón para añadir tareas
button_add_task = tk.Button(window, text="Añadir Tarea", command=add_task)
button_add_task.grid(row=0, column=1, padx=10)

# Crear la lista donde se mostrarán las tareas
listbox_tasks = tk.Listbox(window, height=10, width=50, selectmode=tk.SINGLE)
listbox_tasks.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Crear botones para marcar como completada y eliminar
button_complete_task = tk.Button(window, text="Marcar como Completada", command=complete_task)
button_complete_task.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

button_delete_task = tk.Button(window, text="Eliminar Tarea", command=delete_task)
button_delete_task.grid(row=2, column=1, padx=10, pady=5, sticky=tk.E)

# Atajos de teclado
window.bind("<Return>", add_task)  # Enter para añadir tarea
window.bind("<c>", complete_task)  # Tecla "C" para completar tarea
window.bind("<d>", delete_task)    # Tecla "D" para eliminar tarea
window.bind("<Escape>", close_app) # Tecla "Escape" para cerrar la aplicación

# Ejecutar la ventana principal
window.mainloop()
