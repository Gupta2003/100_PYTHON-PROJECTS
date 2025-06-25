import random
import string
print("Welcome to the PyPassword Generator!\n")
letter = int(input("How many letters would you like in your password?\n"))
symbol = int(input("How many symbols would you like?\n"))
number = int(input("How many numbers would you like?\n"))
password_list = []
for num in range(0,number):
    password_list.append(random.randint(0,9))

for lett in range(0,letter):
    password_list.append(random.choice(string.ascii_letters))

for sym in range(0,symbol):
    password_list.append(random.choice(string.punctuation))

print(password_list)
random.shuffle(password_list)
print(password_list)
print("Your password is: " + "".join(str(i) for i in password_list))