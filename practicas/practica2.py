"""
Prática 2:
Escribe un programa que solicite el nombre, el apellido y la edad del usuario e imprima un saludo y su año de nacimiento. Tomar el año actual como constante (2023)
Ejemplo.
input
Nombre: Alfredo
Apellido: Altamirano
Edad: 36

output -> Hola Alfredo Altamirano, naciste en 1986

"""
print("\n")
print("Práctica 2 En que año naciste")
año = 2023
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
print("Hola", nombre + " " + apellido, "naciste en el año: ", año - int(edad))
