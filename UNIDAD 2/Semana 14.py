import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime


class GestorEventos:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Eventos")
        self.root.geometry("700x500")

        self.crear_widgets()

    def crear_widgets(self):
        # Frame para la lista de eventos
        self.eventos_frame = ttk.LabelFrame(self.root, text="Eventos Programados", padding=(10, 10))
        self.eventos_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Treeview para mostrar los eventos
        columnas = ("Fecha", "Hora", "Descripción")
        self.eventos_tree = ttk.Treeview(self.eventos_frame, columns=columnas, show="headings")
        for col in columnas:
            self.eventos_tree.heading(col, text=col)
            self.eventos_tree.column(col, width=150 if col != "Descripción" else 250)
        self.eventos_tree.pack(fill="both", expand=True)

        # Frame para la entrada de datos
        self.entrada_frame = ttk.LabelFrame(self.root, text="Agregar Nuevo Evento", padding=(10, 10))
        self.entrada_frame.pack(fill="x", padx=10, pady=5)

        # Campo de entrada para la fecha
        ttk.Label(self.entrada_frame, text="Fecha:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.fecha_entry = DateEntry(self.entrada_frame, width=12, background='darkblue', foreground='white',
                                     borderwidth=2)
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        # Campo de entrada para la hora
        ttk.Label(self.entrada_frame, text="Hora (HH:MM):").grid(row=0, column=2, sticky="w", padx=5, pady=5)
        self.hora_entry = ttk.Entry(self.entrada_frame)
        self.hora_entry.grid(row=0, column=3, padx=5, pady=5)

        # Campo de entrada para la descripción
        ttk.Label(self.entrada_frame, text="Descripción:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.descripcion_entry = ttk.Entry(self.entrada_frame, width=60)
        self.descripcion_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        # Frame para los botones
        self.botones_frame = ttk.Frame(self.root, padding=(10, 10))
        self.botones_frame.pack(fill="x", padx=10, pady=5)

        # Botón para agregar evento
        self.agregar_btn = ttk.Button(self.botones_frame, text="Agregar Evento", command=self.agregar_evento)
        self.agregar_btn.pack(side="left", padx=5, pady=5)

        # Botón para eliminar evento seleccionado
        self.eliminar_btn = ttk.Button(self.botones_frame, text="Eliminar Evento Seleccionado",
                                       command=self.eliminar_evento)
        self.eliminar_btn.pack(side="left", padx=5, pady=5)

        # Botón para salir de la aplicación
        self.salir_btn = ttk.Button(self.botones_frame, text="Salir", command=self.root.quit)
        self.salir_btn.pack(side="right", padx=5, pady=5)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        # Validar formato de hora
        if not self.validar_hora(hora):
            messagebox.showwarning("Hora inválida", "El formato de la hora debe ser HH:MM.")
            return

        # Verificar que todos los campos estén llenos
        if not (fecha and hora and descripcion):
            messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos.")
            return

        # Agregar el evento al Treeview
        self.eventos_tree.insert("", "end", values=(fecha, hora, descripcion))
        self.limpiar_campos()

    def eliminar_evento(self):
        selected_item = self.eventos_tree.selection()
        if selected_item:
            respuesta = messagebox.askyesno("Confirmación",
                                            "¿Está seguro de que desea eliminar el evento seleccionado?")
            if respuesta:
                self.eventos_tree.delete(selected_item)
        else:
            messagebox.showwarning("Selección vacía", "Por favor, seleccione un evento para eliminar.")

    def limpiar_campos(self):
        self.fecha_entry.set_date(datetime.now())
        self.hora_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)

    def validar_hora(self, hora):
        """Valida el formato de la hora como HH:MM."""
        try:
            datetime.strptime(hora, '%H:%M')
            return True
        except ValueError:
            return False


# Crear la ventana principal
root = tk.Tk()
app = GestorEventos(root)
root.mainloop()

