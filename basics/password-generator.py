import random
import string

def generate_password(length):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    all_chars = uppercase_letters + lowercase_letters + digits + symbols

    password = "".join(random.choices(all_chars, k=length))

    return password

length = int(input("Enter the length of the password: "))

password = generate_password(length)

print(f"Random Password Generated: {password}")