# -*- coding: utf-8 -*-
'''
Created on 20 jun. 2017

@author: antonio.mendez
'''

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
    <num_estudiantes> durante n simulaciones <num_simulaciones>"""