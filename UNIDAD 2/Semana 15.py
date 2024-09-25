import tkinter as tk
from tkinter import messagebox, Listbox, END


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        # Lista de tareas
        self.tasks = []

        # Campo de entrada para nuevas tareas
        self.task_input = tk.Entry(root, width=40)
        self.task_input.pack(pady=10)
        self.task_input.bind('<Return>', self.add_task)  # Añadir tarea con Enter

        # Botón para añadir tarea
        self.add_task_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_task_button.pack(pady=5)

        # Botón para marcar como completada
        self.complete_task_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

        # Botón para eliminar tarea
        self.delete_task_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        # Lista de tareas
        self.task_list = Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
        self.task_list.pack(pady=10)

    def add_task(self, event=None):
        task = self.task_input.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_input.delete(0, END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea.")

    def complete_task(self):
        try:
            selected_index = self.task_list.curselection()[0]
            completed_task = self.tasks[selected_index]
            self.tasks[selected_index] = f"✔ {completed_task}"
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcar como completada.")

    def delete_task(self):
        try:
            selected_index = self.task_list.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

    def update_task_list(self):
        self.task_list.delete(0, END)
        for task in self.tasks:
            self.task_list.insert(END, task)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
