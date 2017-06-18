# -*- coding: utf-8 -*-
'''
Created on 18 jun. 2017

@author: Steiner
'''

import turtle


def dibujaKoch(t, n):
    """ Dibuja una curva de Koch de longitud "n". t es una turtle"""
    if n < 10:
        t.fd(n)
        return
    m = n / 3
    dibujaKoch(t, m)
    t.lt(60)
    dibujaKoch(t, m)
    t.rt(120)
    dibujaKoch(t, m)
    t.lt(60)
    dibujaKoch(t, m)

def coponieve(t, n):
    """ Dibuja un copo de nieve (un triángulo con
    una curva de Koch en su interior)"""
    for i in range(3):
        dibujaKoch(t, n)
        t.rt(120)
    
bob = turtle.Turtle()

coponieve(bob, 250)
turtle.mainloop()
