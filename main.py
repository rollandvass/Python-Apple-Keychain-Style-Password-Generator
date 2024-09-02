import random
import string
import csv

filename = "Python Passwords.csv"

def generate_password():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits

    password_chars = random.choices(lowercase, k = 18)

    uppercase_letter = random.choice(uppercase)
    digit = random.choice(digits)

    upper_position = random.randint(0, 17)
    digit_position = random.randint(0, 17)

    while digit_position == upper_position:
        digit_position = random.randint(0,17)

    password_chars.insert(upper_position, uppercase_letter)
    password_chars.insert(digit_position, digit)

    password = ''.join(password_chars)

    formatted_password = f"{password[:6]}-{password[6:12]}-{password[12:18]}"

    return formatted_password

def get_user_input():
    name = input("Enter the website name: ")
    url = input("Enter the website URL: ")
    username = input("Enter your email/username: ")
    note = input("Enter any additional note (optional): ")
    return {"name": name, "url": url, "username": username, "note": note}

with open(filename, 'a', newline='') as file:
    writer = csv.writer(file)

    file.seek(0, 2)
    if file.tell() == 0:
        writer.writerow(["name", "url", "username", "password", "note"])

    entry = get_user_input()

    password = generate_password()
    writer.writerow([entry["name"], entry["url"], entry["username"], password, entry["note"]])

print(f"\nPassword for {entry['name']} saved successfully.\nYou can copy it below:\n\n{password}\n")