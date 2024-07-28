import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password_length = input("Introduce la longitud de la contraseña: ")

password = ""

for i in range(int(password_length)):
    password += random.choice(characters)

print("Contraseña generada:", password)
