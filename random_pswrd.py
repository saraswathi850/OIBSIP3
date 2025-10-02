import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    length = int(input("Enter the password length: "))
    if length > 0:
        password = generate_password(length)
        print("Generated password:", password)
    else:
        print("Length must be greater than 0")
except ValueError:
    print("Invalid input. Please enter a number")