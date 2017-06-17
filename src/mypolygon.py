# Ejercicio para demostrar el uso de la encapsulación,
# la generalización y la refactorización


import turtle
import math

bob = turtle.Turtle()


def cuadrado(t, longitud):
    """ Dibuja un cuadrado de tamaño <longitud>. t es una turtle """
    for i in range(4):
        t.fd(longitud)
        t.lt(90)


def polilinea(t, n, longitud, angulo):
    """ Dibuja un <n> segmentos con tamaño <longitud> y
        ángulo <angulo> entre ellos. t es una turtle"""
    for i in range(n):
        t.fd(longitud)
        t.ld(angulo)


def poligono(t, lados, longitud):
    """ Dibuja un polígono de <lados> y <longitud> dados.longitud.
        t es una turtle """
    angulo = 360 / lados
    polilinea(t, lados, longitud, angulo)


def arco(t, radio, angulo):
    """ Dibuja un arco de <radio> y <angulo> dados. t es una turtle """
    longitud_arco = 2 * math.pi * radio * angulo / 360
    n = int(longitud_arco / 3) + 1    # Nº de segmentos
    paso_longitud = longitud_arco / n
    paso_angulo = angulo / n

    for i in range(n):
        t.fd(paso_longitud)
        t.lt(paso_angulo)


def circulo(t, radio):
    """ Dibuja un arco de <radio> dado. t es una turtle"""
    arco(t, radio, 360)


# poligono(bob, lados=7, longitud=50)
# circulo(bob, 100)
# arco(bob, radio=75, angulo=180)

# turtle.mainloop()
