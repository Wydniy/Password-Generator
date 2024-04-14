import random

print('Your Password: ')

chars = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'

password = ''
for x in range(12):
    password += random.choice(chars)

print(password)