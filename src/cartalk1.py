# -*- coding: utf-8 -*-
'''
Created on 19 jun. 2017

@author: Steiner

Este programa prueba si una palabr contiene tres consecutivas
dobles letras
'''

def es_triple_doble(palabra):
    """ Devuelve verdadero si la palabra contiene 
    tres dobles letras consecutivas """
    
    contador = 0
    indice = 0
    
    while indice < len(palabra)-1:
        if palabra[indice] == palabra[indice+1]:
            contador += 1
            if contador == 3:
                return True
            indice += 2
        else:
            contador = 0
            indice += 1
    return False

fin = open("words.txt")

for linea in fin:
    if es_triple_doble(linea):
        print(linea)            