import random
import string

print("Welcome to the PyPassword Generator!")
letter_amount = int(input("How many letters would you like in your password?\n"))
symbols_amount = int(input("How many symbols would you like?\n"))
numbers_amount = int(input("How many numbers would you like?\n"))

generated_password = []

if letter_amount > 0:
    for a in range(letter_amount):
        generated_password.append(random.choice(string.ascii_letters))

if symbols_amount > 0:
    for a in range(symbols_amount):
        generated_password.append(random.choice(string.punctuation))

if numbers_amount > 0:
    for a in range(numbers_amount):
        generated_password.append(random.choice(string.digits))

random.shuffle(generated_password)

print(f"Here is your password: {''.join(generated_password)}")
