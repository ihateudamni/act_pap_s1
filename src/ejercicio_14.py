import random
numero_secreto = random.randint(1, 10)
intento = int(input("Adivina el número del 1 al 10: "))
while intento != numero_secreto:
    intento = int(input("Intenta otra vez: "))
print("Adivinaste")
