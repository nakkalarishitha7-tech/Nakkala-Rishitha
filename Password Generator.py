import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','#','$','&','%','*','+']


print("Welcome to the PyPassword Generator!")
no_letters=int(input("How many letters would you like inyour password?\n"))
no_symbols=int(input("How many symbols would you like?\n"))
no_numbers=int(input("How many numbers would you like?\n"))

password=""

for char in range(0, no_letters):
     password += random.choice(letters)

for char in range(0, no_symbols):
     password += random.choice(symbols)

for char in range(0, no_numbers):
     password += random.choice(numbers)

print(password)
