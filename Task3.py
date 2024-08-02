import random
import tkinter as tk
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def display_password():
    try:
        password_length = int(password_length_entry.get())
        if 8 <= password_length <= 20:
            password = generate_password(password_length)
            password_window = tk.Toplevel(root)
            password_window.title("Generated Password")
            password_label = tk.Label(password_window, text=f"Your password is: {password}", font=("Arial", 16))
            password_label.pack(padx=20, pady=20)
        else:
            password_length_entry.delete(0, tk.END)
            password_length_entry.insert(0, "Invalid length. Please enter a value between 8 and 20.")
    except ValueError:
        password_length_entry.delete(0, tk.END)
        password_length_entry.insert(0, "Invalid input. Please enter a number.")

root = (link unavailable)()
root.title("Password Generator")
password_length_label = tk.Label(root, text="Enter the desired length of the password (between 8 and 20 characters): ")
password_length_label.pack(padx=10, pady=10)
password_length_entry = tk.Entry(root)
password_length_entry.pack(padx=10, pady=10)
generate_button = tk.Button(root, text="Generate Password", command=display_password)
generate_button.pack(padx=10, pady=10)
root.mainloop()
 
