# Dibuje el nombre de cada uno de los integrantes del grupo en un plot en 2D, teniendo en cuenta
# líneas rectas y/o curvas.

import matplotlib
matplotlib.use("TkAgg")   # Forzar ventana gr�fica en Visual Studio

import matplotlib.pyplot as plt

plt.figure(figsize=(12,4))

# ===== CRISTIAN =====
# C
plt.plot([0,0,1], [0,2,2])
plt.plot([0,1], [0,0])

# R
plt.plot([1.5,1.5], [0,2])
plt.plot([1.5,2.5], [2,2])
plt.plot([2.5,2.5], [1,2])
plt.plot([1.5,2.5], [1,1])
plt.plot([1.5,2.5], [1,0])

# I
plt.plot([3,3], [0,2])

# S
plt.plot([3.5,4.5], [2,2])
plt.plot([3.5,3.5], [1,2])
plt.plot([3.5,4.5], [1,1])
plt.plot([4.5,4.5], [0,1])
plt.plot([3.5,4.5], [0,0])

# T
plt.plot([5,6], [2,2])
plt.plot([5.5,5.5], [0,2])

# I
plt.plot([6.5,6.5], [0,2])

# A
plt.plot([7,7.5,8], [0,2,0])
plt.plot([7.25,7.75], [1,1])

# N
plt.plot([8.5,8.5], [0,2])
plt.plot([8.5,9.5], [2,0])
plt.plot([9.5,9.5], [0,2])

# ===== JOSE =====
offset = 11

# J
plt.plot([offset+1,offset+2], [0,0])
plt.plot([offset+2,offset+2], [0,2])

# O
plt.plot([offset+3,offset+4,offset+4,offset+3,offset+3], [0,0,2,2,0])

# S
plt.plot([offset+5,offset+6], [2,2])
plt.plot([offset+5,offset+5], [1,2])
plt.plot([offset+5,offset+6], [1,1])
plt.plot([offset+6,offset+6], [0,1])
plt.plot([offset+5,offset+6], [0,0])

# E
plt.plot([offset+7,offset+7], [0,2])
plt.plot([offset+7,offset+8], [2,2])
plt.plot([offset+7,offset+8], [1,1])
plt.plot([offset+7,offset+8], [0,0])

# ===== NICOLAS =====
offset = 21

# N
plt.plot([offset,offset], [0,2])
plt.plot([offset,offset+1], [2,0])
plt.plot([offset+1,offset+1], [0,2])

# I
plt.plot([offset+2,offset+2], [0,2])

# C
plt.plot([offset+3,offset+3], [0,2])
plt.plot([offset+3,offset+4], [2,2])
plt.plot([offset+3,offset+4], [0,0])

# O
plt.plot([offset+5,offset+6,offset+6,offset+5,offset+5], [0,0,2,2,0])

# L
plt.plot([offset+7,offset+7], [0,2])
plt.plot([offset+7,offset+8], [0,0])

# A
plt.plot([offset+9,offset+9.5,offset+10], [0,2,0])
plt.plot([offset+9.25,offset+9.75], [1,1])

# S
plt.plot([offset+11,offset+12], [2,2])
plt.plot([offset+11,offset+11], [1,2])
plt.plot([offset+11,offset+12], [1,1])
plt.plot([offset+12,offset+12], [0,1])
plt.plot([offset+11,offset+12], [0,0])

plt.title("Integrantes del Grupo")
plt.axis("equal")
plt.axis("off")
plt.show()

input("Presione ENTER para salir")