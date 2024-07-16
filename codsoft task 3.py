import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password(length):
    if length < 1:
        raise ValueError("Password length must be at least 1")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_gui():
    try:
        length = int(length_entry.get())
        password = generate_password(length)
        result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the password length.")

root = tk.Tk()
root.title("Password Generator")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

length_label = tk.Label(frame, text="Enter the desired length of the password:")
length_label.pack()

length_entry = tk.Entry(frame)
length_entry.pack(pady=5)

generate_button = tk.Button(frame, text="Generate Password", command=generate_password_gui)
generate_button.pack(pady=5)

result_label = tk.Label(frame, text="")
result_label.pack(pady=5)

root.mainloop()
