#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
n_letters= int(input("How many letters would you like in your password?\n")) 
n_symbols = int(input(f"How many symbols would you like?\n"))
n_numbers = int(input(f"How many numbers would you like?\n"))
total_characters = n_letters + n_numbers + n_symbols
#make a random letter generator
#make a random symbol generator
#make a random number generator
random_numbers = random.choice(numbers)
password = ""
for i in range(0, n_letters):
  random_letters = random.choice(letters)
  password += random_letters
for i in range(0, n_symbols):
  random_symbols = random.choice(symbols)
  password += random_symbols
for i in range(0, n_numbers):
  random_numbers = random.choice(numbers)
  password += random_numbers
print(password)
list_password = list(password)
print(list_password)
random.shuffle(list_password)
list_password = "".join(list_password)
print(list_password)
