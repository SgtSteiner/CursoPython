# -*- coding: utf-8 -*-
'''
Created on 20 jun. 2017

@author: Steiner

Véase http: // en. wikipedia. org/ wiki/ Birthday_ paradox
'''

import random

def hay_duplicados(t):
    """ Devuelve verdadero si cualquier elemento  de la lista
    aparece más de una vez """
    t2 = list(t)
    t2.sort()
    for indice in range(0, len(t2)-1):
        if t2[indice] == t2[indice+1]:
            return True
    return False

def dias_aleatorios(n):
    """ Devuelve una lista de <n> enteros aleatorios """
    t = []
    for i in range(n):
        # genera un entero aleatorio entre 1 y 365
        t.append(random.randint(1, 365))
    return t

def cuenta_duplicados(num_estudiantes, num_simulaciones):
    """ Devuelve el numero de duplicados en una lista de 
    <num_estudiantes> al cabo de n simulaciones <num_simulaciones>"""
    sumatorio = 0
    for i in range(num_simulaciones):
        # Genera una lista de tamaño <num_estudianetes> de enteros aleatorios
        t = dias_aleatorios(num_estudiantes)
        if hay_duplicados(t):
            sumatorio += 1
    return sumatorio
    
for i in range(100):
    num_simulaciones = 10000
    contador = cuenta_duplicados(i, num_simulaciones)
    print("Con grupos de %d estudiantes " % i, end="")
    print("existen un porcentaje de duplicidad de %f " % (contador / num_simulaciones))
