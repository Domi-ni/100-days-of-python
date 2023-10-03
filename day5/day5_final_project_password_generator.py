import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
random_password = []
random_selection_caracters = []
for counter in range(1, nr_letters + 1):
  random_letter = random.choice(letters)
  random_password.append(random_letter)
for counter in range(1, nr_symbols + 1):
  random_symbol = random.choice(symbols)
  random_password.append(random_symbol)
for counter in range(1, nr_numbers + 1):
  random_number = random.choice(numbers)
  random_password.append(random_number)
for counter in range (1, len(random_password)+1):
  random_caracter = random.choice(random_password)
  random_selection_caracters.append(random_caracter)
  random_password.remove(random_caracter)
for caracter in random_selection_caracters:
  password = "".join(random_selection_caracters)
print(password)
