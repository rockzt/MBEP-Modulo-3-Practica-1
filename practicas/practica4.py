# Prática 4: Escribe un script que solicite un número (n) y calcule el valor de n + nn + nnn:

print("\n")
print("Práctica 4 n + nn + nnn ")
numero = input("Dame un numero: ")
n = float(numero)
resultado = n + n**2 + n**3
print("Tu resultado es ", resultado)
