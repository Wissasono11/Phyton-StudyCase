import random
import secrets
import string

alphabet = string.ascii_letters
number = string.digits
symbol = string.punctuation

print("=========== Welcome To Pass Generator ===========")

alpha = int(input("How many words do you want to use: "))
num = int(input("How many numeric do you want to use: "))
sym = int(input("How many symbol do you want to use: "))

result = alpha + num + sym 
password = []

for i in range(1, alpha + 1):
    password += random.choice(alphabet)
for i in range(1, num + 1):
    password += random.choice(number)
for i in range(1, sym + 1):
    password += random.choice(symbol)

print("\n{pass}")
random.shuffle(password)
print(password)

print(f"\n\nYour password as much as in: ", result)
key = ""
for i in password:
    key += i

print("Your password is: ", key, "\n\n ======= THANK YOU =======")