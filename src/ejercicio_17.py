num = int(input("Ingrese un número: "))
suma = 0
for digito in str(num):
    suma += int(digito)
print("Suma de dígitos:", suma)
