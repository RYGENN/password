import random

chars="qwertyuiopasdfghjklzxcvbnm0123456789ASDFGHJKLZXCVBNMQWERTYUIOP@$%&+=!"
length=int(input("Enter the length of the password:"))
password=" "
for a in range(length):
    password+=random.choice(chars)
print(password)
