import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '@', '_', '*', '+']

print("Welcome to the Python Password generator!")
pass_len = int(input("How many letters would you like in your password: "))
pass_sym = int(input("How many symbols would you like in your password: "))
pass_digit = int(input("How many numbers would you like in your password: "))

#Eazy Level
password = ""

for char in range(1, pass_len + 1):
  password += random.choice(letters)

for char in range(1, pass_sym + 1):
  password += random.choice(symbols)

for char in range(1, pass_digit + 1):
  password += random.choice(numbers)

print(f"Your easy level generated password is {password}")

#Hard Level
password_list = []

for char in range(1, pass_len + 1):
  password_list.append(random.choice(letters))

for char in range(1, pass_sym + 1):
  password_list.append(random.choice(symbols))

for char in range(1, pass_digit + 1):
  password_list.append(random.choice(numbers))

random.shuffle(password_list)  

password = ""
for char in password_list:
          password += char


print(f"Your hard level generated password is {password}")