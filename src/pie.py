# Dibuja gráfico de tartas con triágulos isósceles

import math
import turtle


def isosceles(t, r, angulo):
    """ Dibuja un triágulo isósceles, donde:
    t = turtle
    r = tamaño de los lados iguales
    angulo = angulo del pico
    """
    y = r * math.sin(angulo * math.pi / 180)

    t.rt(angulo)
    t.fd(r)
    t.lt(90 + angulo)
    t.fd(2 * y)
    t.lt(90 + angulo)
    t.fd(r)
    t.lt(180 - angulo)


def polypie(t, n, r):
    """ Dibuja una tarta dividida en segmento radiales
    t = turtle
    n = número de segmentos
    r = longitud de los radios
    """
    angulo = 360 / n
    for i in range(n):
        isosceles(t, r, angulo / 2)
        t.lt(angulo)


bob = turtle.Turtle()
bob.speed(8)

polypie(bob, 45, 250)

turtle.mainloop()
