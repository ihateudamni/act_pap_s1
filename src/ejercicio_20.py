mayor = -1
edad = int(input("Ingrese una edad: "))
while edad != -1:
    if edad > mayor:
        mayor = edad
    edad = int(input("Ingrese una edad: "))
print("La edad mayor es:", mayor)
