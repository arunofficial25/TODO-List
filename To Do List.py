import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        self.task_number = 0

        self.task_list = tk.Listbox(self.root, width=40)
        self.task_list.pack(padx=10, pady=10)

        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack(padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Add task", command=self.add_task)
        self.add_button.pack(padx=10, pady=10)

        self.remove_button = tk.Button(self.root, text="Remove task", command=self.remove_task)
        self.remove_button.pack(padx=10, pady=10)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append(task)
            self.task_list.insert(self.task_number, task)
            self.task_number += 1
            self.entry.delete(0, tk.END)

    def remove_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
            self.tasks.pop(task_index)
        except:
            messagebox.showwarning("Error", "Select a task to remove")

root = tk.Tk()
my_gui = ToDoList(root)
root.mainloop()