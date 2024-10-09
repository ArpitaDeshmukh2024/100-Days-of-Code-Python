#Version1

import numpy as np

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','^','&','*','(',')']

print("Welcome to the Password Generator !!!")
letter_input = int(input("How many letters would you like in your password ?"))
number_input = int(input("How many numbers would you like in your password ?"))
symbol_input = int(input("How many symbols would you like in your password ?"))

password = ""

for char in range(0 , letter_input):
  password += np.random.choice(letters)

for char in range(0 , number_input):
  password += np.random.choice(numbers)

for char in range(0 , symbol_input):
  password += np.random.choice(symbols)

print(password)

#Version2

import numpy as np

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','^','&','*','(',')']

print("Welcome to the Password Generator !!!")
letter_input = int(input("How many letters would you like in your password ?"))
number_input = int(input("How many numbers would you like in your password ?"))
symbol_input = int(input("How many symbols would you like in your password ?"))

password_list = []

for char in range(0 , letter_input):
  password_list.append(np.random.choice(letters))

for char in range(0 , number_input):
  password_list.append(np.random.choice(numbers))

for char in range(0 , symbol_input):
  password_list.append(np.random.choice(symbols))

np.random.shuffle(password_list)

passwords = ""

for char in password_list:
  passwords += char

print(passwords)
