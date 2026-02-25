# Realice un programa que calcule la potencia que consume un circuito ingresando por teclado el valor de corriente y voltaje.

print("CALCULO DE POTENCIA ELECTRICA")
print("--------------------------------")

# entrada de datos
V = float(input("Ingrese el valor del voltaje (V): "))
I = float(input("Ingrese el valor de la corriente (A): "))

# calculo
P = V * I

# salida con formato (similar a fprintf)
print(f"La potencia consumida es: {P} W")