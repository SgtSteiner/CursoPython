# -*- coding: utf-8 -*-
'''
Created on 18 jun. 2017

@author: Steiner

Un número <a> es potencia de otro número <b> si:
a es divisible por b y
a / b es potencia de b
'''

def esPotencia(a, b):
    """ Devuelve verdadero si <a> es potencia de <b>"""
    if a <= 1:
        return True
    if a % b != 0:
        return False
    return esPotencia(a/b, b)

print(esPotencia(1296, 6)) # Ejemplo
