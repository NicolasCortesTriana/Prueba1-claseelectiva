# Obtenga las coordenadas X y Y de los contornos de dos logos de automóviles (Chevrolet, Hyundai,
# Mazda, etc.), a través de Python.

import cv2
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

def dibujar_logo(ax, imagen, nombre):
    img = cv2.imread(imagen, 0)
    bordes = cv2.Canny(img, 50, 150)

    contornos, _ = cv2.findContours(
        bordes,
        cv2.RETR_TREE,
        cv2.CHAIN_APPROX_NONE
    )

    for cnt in contornos:
        if cv2.contourArea(cnt) > 80:
            X = cnt[:, 0, 0]
            Y = cnt[:, 0, 1]
            ax.plot(X, Y, '.', markersize=1)

    ax.invert_yaxis()
    ax.set_title(nombre)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.axis("equal")
    ax.grid()

# figura
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

dibujar_logo(axs[0], "chevrolet.png", "Chevrolet")
dibujar_logo(axs[1], "mazda.png", "Mazda")

plt.suptitle("Contornos")
plt.show()

input("Presione ENTER para salir")