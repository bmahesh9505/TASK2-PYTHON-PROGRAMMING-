import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_gui():
    def generate():
        try:
            pw_length = int(entry_length.get())
            if pw_length <= 0:
                messagebox.showerror("Error", "Please enter a length greater than 0.")
            else:
                password = generate_password(pw_length)
                output_label.config(text=f"Generated Password: {password}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid length (a positive integer).")

    window = tk.Tk()
    window.title("Password Generator")

    label = tk.Label(window, text="Enter the desired length of the password:")
    label.pack()

    entry_length = tk.Entry(window)
    entry_length.pack()

    generate_button = tk.Button(window, text="Generate Password", command=generate)
    generate_button.pack()

    output_label = tk.Label(window, text="")
    output_label.pack()

    window.mainloop()

generate_password_gui()