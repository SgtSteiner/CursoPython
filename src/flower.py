# Ejercicio para demostrar el uso de turtle.

import turtle
from mypolygon import arco


def petalo(t, radio, angulo):
    """ Dibuja un pétalo con dos arcos de <radio> y
    <angulo> dados. t es una turtle """
    for i in range(2):
        arco(t, radio, angulo)
        t.lt(180 - angulo)


def flor(t, n_petalos, radio, angulo):
    """ Dibuja una flor con <n_petalos> y con arcos de
    <radio> y <angulo> dados. t es una turtle """
    for i in range(n_petalos):
        petalo(t, radio, angulo)
        t.lt(360 / n_petalos)


def mueve(t, longitud):
    """ Mueve la turtle <t> hacia adelante la <longitud> dada
    sin dejar trazo """
    t.pu()
    t.fd(longitud)
    t.pd()


bob = turtle.Turtle()

bob.hideturtle()
bob.speed(5)

mueve(bob, -100)
flor(bob, 7, 60, 60)

mueve(bob, 100)
flor(bob, 10, 40, 80)

mueve(bob, 100)
flor(bob, 20, 140, 20)

turtle.mainloop()
