import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import Calendar  # Import Calendar from tkcalendar
import pickle
import os

# File to store tasks
TASK_FILE = "tasks.pkl"

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("350x550")

        self.tasks = []

        # Title Label
        tk.Label(root, text="My TO-DO List", font=('Times New Roman', 16, 'bold')).pack(pady=10)

        # Task Entry
        self.task_entry = tk.Entry(root, font=('Times New Roman', 14), width=22)
        self.task_entry.pack(pady=5)

        # Date Selector (Dropdown with Calendar Popup)
        self.date_selector = ttk.Combobox(root, font=('Times New Roman', 12), state="readonly")
        self.date_selector.set("Select Date")
        self.date_selector.pack(pady=5)
        self.date_selector.bind("<Button-1>", lambda e: self.open_calendar())

        # Category Selector
        self.category_selector = ttk.Combobox(root, values=["Work", "Personal", "Other"], font=('Times New Roman', 12), state="readonly")
        self.category_selector.set("Work")
        self.category_selector.pack(pady=5)

        # Buttons
        self.add_btn = tk.Button(root, text="Add Task", width=20, font=('Times New Roman', 12), command=self.add_task)
        self.add_btn.pack(pady=2)

        self.delete_btn = tk.Button(root, text="Delete Task", width=20, font=('Times New Roman', 12), command=self.delete_task)
        self.delete_btn.pack(pady=2)

        self.mark_btn = tk.Button(root, text="Mark Complete", width=20, font=('Times New Roman', 12), command=self.mark_done)
        self.mark_btn.pack(pady=2)

        self.edit_btn = tk.Button(root, text="Edit Task", width=20, font=('Times New Roman', 12), command=self.edit_task)
        self.edit_btn.pack(pady=2)

        # Task Listbox
        self.listbox = tk.Listbox(root, width=40, height=5, font=('Times New Roman', 12))
        self.listbox.pack(pady=10)

        # Search Bar
        self.search_entry = tk.Entry(root, font=('Times New Roman', 14), width=22)
        self.search_entry.pack(pady=5)

        self.search_btn = tk.Button(root, text="Search", width=20, font=('Times New Roman', 12), command=self.search_task)
        self.search_btn.pack(pady=2)

        self.load_tasks()

    def open_calendar(self):
        def select_date():
            selected_date = calendar.get_date()
            self.date_selector.set(selected_date)
            calendar_window.destroy()

        calendar_window = tk.Toplevel(self.root)
        calendar_window.title("Select Date")
        calendar = Calendar(calendar_window, selectmode="day", date_pattern="mm/dd/y")
        calendar.pack(pady=10)
        tk.Button(calendar_window, text="Select", font=('Times New Roman', 12), command=select_date).pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        date = self.date_selector.get()  # Get the selected date from the date selector
        category = self.category_selector.get()
        if task:
            self.tasks.append(f"{task} ({date}, {category})")
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Enter a task!")

    def mark_done(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            if "✔️" in self.tasks[index]:
                self.tasks[index] = self.tasks[index].replace(" ✔️", "")
            else:
                self.tasks[index] += " ✔️"
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Select a task!")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Select a task!")

    def edit_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            task_details = self.tasks[index]
            task, details = task_details.rsplit(" (", 1)
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(0, task)
            self.tasks.pop(index)
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Select a task!")

    def search_task(self):
        query = self.search_entry.get().lower()
        if query:
            filtered_tasks = [task for task in self.tasks if query in task.lower()]
            self.listbox.delete(0, tk.END)
            for task in filtered_tasks:
                self.listbox.insert(tk.END, task)
        else:
            self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

    def save_tasks(self):
        with open(TASK_FILE, "wb") as f:
            pickle.dump(self.tasks, f)
        messagebox.showinfo("Saved", "Tasks saved successfully.")

    def load_tasks(self):
        if os.path.exists(TASK_FILE):
            with open(TASK_FILE, "rb") as f:
                self.tasks = pickle.load(f)
            self.update_listbox()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()