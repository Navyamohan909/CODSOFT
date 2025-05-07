import tkinter as tk
from tkinter import messagebox

# Initialize the contact book as a dictionary
contacts = {}

def add_contact():
    """Add a new contact to the contact book."""
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if not name or not phone:
        messagebox.showerror("Error", "Name and Phone are required!")
        return

    contacts[name] = {"phone": phone, "email": email, "address": address}
    messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
    clear_entries()
    display_contacts()

def display_contacts():
    """Display all contacts in the listbox."""
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name} - {details['phone']}")

def search_contact():
    """Search for a contact by name or phone."""
    query = search_entry.get()
    if not query:
        messagebox.showerror("Error", "Please enter a name or phone number to search!")
        return

    results = [f"{name} - {details['phone']}" for name, details in contacts.items()
               if query.lower() in name.lower() or query in details['phone']]
    
    if results:
        contact_list.delete(0, tk.END)
        for result in results:
            contact_list.insert(tk.END, result)
    else:
        messagebox.showinfo("No Results", "No contacts found matching your search.")

def update_contact():
    """Update the selected contact's details."""
    selected = contact_list.curselection()
    if not selected:
        messagebox.showerror("Error", "Please select a contact to update!")
        return

    name = contact_list.get(selected).split(" - ")[0]
    if name in contacts:
        contacts[name] = {
            "phone": phone_entry.get(),
            "email": email_entry.get(),
            "address": address_entry.get()
        }
        messagebox.showinfo("Success", f"Contact '{name}' updated successfully!")
        clear_entries()
        display_contacts()

def delete_contact():
    """Delete the selected contact."""
    selected = contact_list.curselection()
    if not selected:
        messagebox.showerror("Error", "Please select a contact to delete!")
        return

    name = contact_list.get(selected).split(" - ")[0]
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", f"Contact '{name}' deleted successfully!")
        display_contacts()

def clear_entries():
    """Clear all input fields."""
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x500")

# Input fields
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Phone:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
phone_entry = tk.Entry(root, width=30)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Address:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
address_entry = tk.Entry(root, width=30)
address_entry.grid(row=3, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Add Contact", command=add_contact).grid(row=4, column=0, padx=10, pady=10)
tk.Button(root, text="Update Contact", command=update_contact).grid(row=4, column=1, padx=10, pady=10)
tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=5, column=0, padx=10, pady=10)
tk.Button(root, text="Search", command=search_contact).grid(row=5, column=1, padx=10, pady=10)
tk.Button(root, text="Clear", command=clear_entries).grid(row=6, column=0, padx=10, pady=10)

# Search field
tk.Label(root, text="Search:").grid(row=7, column=0, padx=10, pady=5, sticky="w")
search_entry = tk.Entry(root, width=30)
search_entry.grid(row=7, column=1, padx=10, pady=5)

# Contact list
contact_list = tk.Listbox(root, width=50, height=15)
contact_list.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

# Run the main loop
root.mainloop()