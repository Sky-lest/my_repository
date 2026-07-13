import random
senha = ''
char = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

com = int(input('escreva o comprimento da senha em números'))

for i in range(com):
    senha += random.choice(char)
print(senha)
