# Realice un programa que sume, reste, multiplique (producto punto y producto cruz) y divida dos matrices previamente inicializadas

# Matrices previamente inicializadas

A = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
]

B = [
    [1, 2, 3],
    [2, 1, 4],
    [1, 1, 1]
]

# FUNCION SUMA
def suma_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# FUNCION RESTA
def resta_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# FUNCION DIVISION
def division_matrices(A, B):
    resultado = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            if B[i][j] == 0:
                fila.append("No se puede /0")
            else:
                fila.append(A[i][j] / B[i][j])
        resultado.append(fila)
    return resultado

# FUNCION MULTIPLICACION
def multiplicacion_matricial(A, B):
    # A: m x n
    # B: n x p
    m = len(A)
    n = len(A[0])
    p = len(B[0])

    # Validar compatibilidad
    if len(B) != n:
        return None

    resultado = []
    for i in range(m):
        fila = []
        for j in range(p):
            suma = 0
            for k in range(n):
                suma += A[i][k] * B[k][j]
            fila.append(suma)
        resultado.append(fila)
    return resultado
# FUNCION MULTIPLICACION CRUZ
def producto_cruz_fila_a_fila(A, B):
    # Producto cruz por filas (solo si cada fila tiene 3 elementos)
    if len(A[0]) != 3 or len(B[0]) != 3:
        return None

    resultado = []
    for i in range(len(A)):
        a = A[i]
        b = B[i]
        cruz = [
            a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]
        ]
        resultado.append(cruz)
    return resultado

def imprimir_matriz(M, nombre):
    print(f"\n{nombre}:")
    for fila in M:
        print(fila)


if len(A) != len(B) or len(A[0]) != len(B[0]):
    print("Error: Las matrices deben tener las mismas dimensiones.")
else:
    # SUMA
    suma = suma_matrices(A, B)

    # RESTA
    resta = resta_matrices(A, B)

    # DIVISIÓN
    division = division_matrices(A, B)

    # PRODUCTO PUNTO (multiplicación matricial)
    producto_punto = multiplicacion_matricial(A, B)

    # PRODUCTO CRUZ (fila a fila)
    producto_cruz = producto_cruz_fila_a_fila(A, B)

    # --------------------------
    # MOSTRAR RESULTADOS
    # --------------------------
    imprimir_matriz(A, "Matriz A")
    imprimir_matriz(B, "Matriz B")

    imprimir_matriz(suma, "Suma A + B")
    imprimir_matriz(resta, "Resta A - B")
    imprimir_matriz(division, "División A / B (elemento a elemento)")

    if producto_punto:
        imprimir_matriz(producto_punto, "Producto punto (A x B)")
    else:
        print("\nProducto punto: No se puede multiplicar (dimensiones incompatibles).")

    if producto_cruz:
        imprimir_matriz(producto_cruz, "Producto cruz (fila a fila)")
    else:
        print("\nProducto cruz: No se puede (solo si cada fila tiene 3 elementos).")
