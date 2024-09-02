import random
import string

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

print(generate_password())