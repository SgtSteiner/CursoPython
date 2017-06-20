# -*- coding: utf-8 -*-
'''
Created on 20 jun. 2017

@author: Steiner
'''

import bisect

def crea_lista():
    """ Crea una lista de palabras usando el m�todo append
    a partir de un archivo de texto """
    fin = open("words.txt")
    lista_palabras = []
    for linea in fin:
        lista_palabras.append(linea.strip())
    return lista_palabras

def in_bisect(lista_palabras, palabra):
    """ Devuelve verdadero si encuentra una palabra en una lista 
    usando el m�todo bisect. Precondici�n: la lista debe estar ordenada """
    i = bisect.bisect_left(lista_palabras, palabra)
    
    if i == len(lista_palabras):
        return False
    
    return lista_palabras[i] == palabra

def interlock(lista_palabras, palabra):
    """ Devuelve verdadero si encuentra una palabra "interlock"
    en una lista de palabras """
    return in_bisect(lista_palabras, palabra[::2]) and in_bisect(lista_palabras, palabra[1::2])

lista_palabras = crea_lista()

for palabra in lista_palabras:
    if interlock(lista_palabras, palabra):
        print(palabra, palabra[::2], palabra[1::2])