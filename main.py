import random
import string
import csv
import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox

filename = "Python Passwords.csv"

def generate_password():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits

    password_chars = random.choices(lowercase, k=18)

    uppercase_letter = random.choice(uppercase)
    digit = random.choice(digits)

    upper_position = random.randint(0, 17)
    digit_position = random.randint(0, 17)

    while digit_position == upper_position:
        digit_position = random.randint(0, 17)

    password_chars.insert(upper_position, uppercase_letter)
    password_chars.insert(digit_position, digit)

    password = ''.join(password_chars)

    formatted_password = f"{password[:6]}-{password[6:12]}-{password[12:18]}"

    return formatted_password

def save_to_csv(name, url, email, password, note):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        file.seek(0, 2)
        if file.tell() == 0:
            writer.writerow(["name", "url", "username", "password", "note"])
        writer.writerow([name, url, email, password, note])

def copy_to_clipboard(password):
    root.clipboard_clear()
    root.update()
    root.clipboard_append(password)

def handle_on_copy():
    copy_to_clipboard(password_label.cget("text"))

def handle_on_generate():
    name = name_entry.get()
    url = url_entry.get()
    email = email_entry.get()
    note = note_entry.get()

    if not name and not url and not email:
        messagebox.showerror("Input Error", "Please fill every field correctly.")
        return
    if not name:
        messagebox.showerror("Input Error", "Website name is a required field.")
        return
    elif not url:
        messagebox.showerror("Input Error", "Website URL is a required field.")
        return
    elif not email:
        messagebox.showerror("Input Error", "Email is a required field.")
        return

    password = generate_password()
    save_to_csv(name, url, email, password, note)

    password_label.config(text=password)
    copy_button.config(state=tk.NORMAL)
    copy_button.pack(pady=10)

def clear_fields():
    name_entry.delete(0, tk.END)
    url_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    note_entry.delete(0, tk.END)
    password_label.config(text="")
    copy_button.pack_forget()

root = tk.Tk()
root.configure(bg="#161616")
root.title("Password Generator")
icon = PhotoImage(file="assets/password.png")
root.iconphoto(False, icon)

window_width = 450
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_position = int((screen_width / 2) - (window_width / 2))
y_position = int((screen_height / 2) - (window_height / 2))

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

tk.Label(root, text="Website Name:", font=("Arial", 13), fg="white", bg="#161616").pack(pady=5)
name_entry = tk.Entry(root, width=50, bg="#505050", fg="white", insertbackground="white")
name_entry.pack(pady=5)

tk.Label(root, text="Website URL:", font=("Arial", 13), fg="white", bg="#161616").pack(pady=5)
url_entry = tk.Entry(root, width=50, bg="#505050", fg="white", insertbackground="white")
url_entry.pack(pady=5)

tk.Label(root, text="Email/Username:", font=("Arial", 13), fg="white", bg="#161616").pack(pady=5)
email_entry = tk.Entry(root, width=50, bg="#505050", fg="white", insertbackground="white")
email_entry.pack(pady=5)

tk.Label(root, text="Note (optional):", font=("Arial", 13), fg="white", bg="#161616").pack(pady=5)
note_entry = tk.Entry(root, width=50, bg="#505050", fg="white", insertbackground="white")
note_entry.pack(pady=5)

buttons_frame = tk.Frame(root, bg="#161616")
buttons_frame.pack(pady=20)
tk.Button(buttons_frame, text="Generate Password", command=handle_on_generate, font=("Arial", 13), fg="white", bg="#003300").pack(side="left", padx=10)
tk.Button(buttons_frame, text="Clear", command=clear_fields, font=("Arial", 13), fg="white", bg="#800000").pack(side="left", padx=10)

password_label = tk.Label(root, text="", font=("Arial", 18, "bold"), bg="#161616", fg="green")
password_label.pack(pady=20)

copy_button = tk.Button(root, text="Copy", command=handle_on_copy, font=("Arial", 13), state=tk.DISABLED, bg="#505050", fg="white")
copy_button.pack_forget()

root.mainloop()