contador = 0
palabra = input("Escriba una palabra: ")
while palabra.lower() != "fin":
    contador += 1
    palabra = input("Escriba una palabra: ")
print("Cantidad de palabras ingresadas:", contador)
