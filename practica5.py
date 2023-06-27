#Prática 5: Escribe un script que solicite un número y devuelva notifique al usuario si el número es par o impar
print("\n")
print("Práctica 5 Es par o impar")
numero=float(input("Ingresa un numero: "))
if numero % 2 == 0:
    print("\t El número es par")
else:
    print("\t El número es impar")