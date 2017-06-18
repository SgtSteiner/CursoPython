# -*- coding: utf-8 -*-
'''
Created on 18 jun. 2017

@author: Steiner

Calcula el máximo común divisor, teniendo en cuenta que

mcd(a, 0) = a
mcd(a, b) = mcd (b, a % b)
'''

def mcd(a, b):
    """ Devuelve el máximo común divisor de dos números """
    if b == 0:
        return a
    return mcd(b, a % b)

print(mcd(15, 21)) # Ejemplo
