#  Realice un programa que le permita al usuario escoger entre robot Cilíndrico, Cartesiano y esférico, donde como respuesta a la selección conteste con el tipo y número de articulaciones que posee.

# CLASIFICACION DE ROBOTS

def robot_cartesiano():
    print("\nRobot Cartesiano")
    print("Tipo de articulaciones: Prismáticas (P)")
    print("Configuración: PPP")
    print("Número de articulaciones: 3")


def robot_cilindrico():
    print("\nRobot Cilíndrico")
    print("Tipo de articulaciones: 1 Rotacional + 2 Prismáticas")
    print("Configuración: RPP")
    print("Número de articulaciones: 3")


def robot_esferico():
    print("\nRobot Esférico (Polar)")
    print("Tipo de articulaciones: 2 Rotacionales + 1 Prismática")
    print("Configuración: RRP")
    print("Número de articulaciones: 3")

# MAIN

print("TIPOS DE ROBOTS INDUSTRIALES")
print("--------------------------------")
print("1. Robot Cartesiano")
print("2. Robot Cilíndrico")
print("3. Robot Esférico")

opcion = int(input("Seleccione una opción (1-3): "))

if opcion == 1:
    robot_cartesiano()
elif opcion == 2:
    robot_cilindrico()
elif opcion == 3:
    robot_esferico()
else:
    print("Opción no válida.")