import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 1:
            messagebox.showerror("Error", "Password length must be at least 1.")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=f"Generated Password: {password}", fg="green")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

tk.Label(root, text="Enter password length:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.grid(row=0, column=1, padx=10, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12))
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Generated Password: ", font=("Arial", 12))
result_label.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()