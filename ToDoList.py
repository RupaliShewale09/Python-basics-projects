#--------------------------------TO-DO LIST APPLICATION-----------------------------
# to create GUI-based application using Python, allowing users to create, update, and track their to-do lists

import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")     # heading
        self.root.configure(bg='darkgray')            # background for the window
        self.root.geometry("500x650")                   
        
        self.tasks = []
        #Title
        self.entry_label = tk.Label(root, text="TO-DO LIST", bg='darkgray', fg='black',font=("Centuary",25,"italic","bold"))
        self.entry_label.pack(pady=30)
        #Enter task
        self.entry_label = tk.Label(root, text="Enter the Task:", bg='darkgray', fg='black',font=("Centuary",14,"bold"))
        self.entry_label.pack(pady=20)
        self.entry_label.place_configure(x='30',y='75')
        
        
        self.entry = tk.Entry(root, width=50, bg='gray', fg='white', insertbackground='white')
        self.entry.pack(pady=10)
        
        self.add_button = tk.Button(root, text="Add Task", width=15, command=self.add_task, bg='green', fg='white')
        self.add_button.pack(pady=7)
        
        self.tasks_listbox = tk.Listbox(root, width=50, height=13, bg='gray', fg='white',font=("Centuary",12,"bold"))
        self.tasks_listbox.pack(pady=10)
        
        self.update_button = tk.Button(root, text="Update Task",width=15, command=self.update_task, bg='orange', fg='white',font=("Centuary",12,"bold"))
        self.update_button.pack(pady=7)
        
        self.delete_button = tk.Button(root, text="Delete Task",width=15, command=self.delete_task, bg='red', fg='white',font=("Centuary",12,"bold"))
        self.delete_button.pack(pady=7)
        
        self.completed_button = tk.Button(root, text="Mark Completed",width=15, command=self.mark_completed, bg='blue', fg='white',font=("Centuary",12,"bold"))
        self.completed_button.pack(pady=7)

    def add_task(self):               
        task = self.entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Nothing to add")

    def update_task(self):
        selected = self.tasks_listbox.curselection()
        if selected:
            index = selected[0]
            new_task = self.entry.get()
            if new_task:
                self.tasks[index]["task"] = new_task
                self.update_listbox()
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Enter task")
        else:
            messagebox.showwarning("Warning", "No task selected")

    def delete_task(self):
        selected = self.tasks_listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "No task selected")

    def mark_completed(self):
        selected = self.tasks_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["completed"] = True
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "No task selected")

    def update_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Completed" if task["completed"] else "Pending"
            self.tasks_listbox.insert(tk.END, f"{task['task']} - {status}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
