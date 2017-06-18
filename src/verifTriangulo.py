# -*- coding: utf-8 -*-
'''
Created on 18 jun. 2017

@author: Steiner

Programa que verifica si es posible formar un triángulo
con tres segmentos, cuyos tamaños son dados como parámetros
a, b y c.
Si alguno de los lados es mayor que la suma de los otros dos
no es posible formar un triángulo. En cualquier otro caso sí.
'''

def es_triangulo(a, b, c):
    """ Devuelve si es posible formar un triángulo dados como
    parámetros el tamaño de cada uno de sus lados"""
    if a > b + c:
        return False
    elif b > a + c:
        return False
    elif c > a + b:
        return False
    else:
        return True

# Solicita el tamaño de los tres lados
a = int(input("Introduce lado 1: "))
b = int(input("Introduce lado 2: "))
c = int(input("Introduce lado 3: "))

print(es_triangulo(a, b, c))