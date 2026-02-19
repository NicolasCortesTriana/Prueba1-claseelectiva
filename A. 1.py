# Realice un programa que sume, reste, multiplique (producto punto y producto cruz) y divida dos vectores previamente inicializados.
# Vectores previamente inicializados
A = [2, 4, 6]
B = [1, 2, 3]

# Validar que tengan el mismo tamaño para operar
if len(A) != len(B):
    print("Los vectores deben tener el mismo tamaño.")
else:
    # SUMA es uno a uno
    suma = [A[i] + B[i] for i in range(len(A))]

    # RESTA es uno a uno
    resta = [A[i] - B[i] for i in range(len(A))]

    # DIVISIÓN (elemento a elemento)
    division = []
    for i in range(len(A)):
        if B[i] == 0:
            division.append("No se puede dividir por 0")
        else:
            division.append(A[i] / B[i])

    # PRODUCTO PUNTO
    producto_punto = sum(A[i] * B[i] for i in range(len(A)))

    # PRODUCTO CRUZ (solo si son 3D)
    producto_cruz = None
    if len(A) == 3:
        producto_cruz = [
            A[1]*B[2] - A[2]*B[1],
            A[2]*B[0] - A[0]*B[2],
            A[0]*B[1] - A[1]*B[0]
        ]

    # imprimir resultados
    print("Vector A:", A)
    print("Vector B:", B)

    print("\nSuma:", suma)
    print("Resta:", resta)
    print("División:", division)
    print("Producto punto:", producto_punto)

    if producto_cruz:
        print("Producto cruz:", producto_cruz)
    else:
        print("Producto cruz: No se puede (solo para vectores de 3 elementos)")

