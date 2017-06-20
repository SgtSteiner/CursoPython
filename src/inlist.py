# -*- coding: utf-8 -*-
'''
Created on 20 jun. 2017

@author: Steiner
'''

import bisect

def crea_lista():
    """ Crea una lista de palabras usando el método append
    a partir de un archivo de texto """
    fin = open("words.txt")
    lista_palabras = []
    for linea in fin:
        lista_palabras.append(linea.strip())
    return lista_palabras

def in_bisect(lista_palabras, palabra):
    """ Busca una palabra en una lista según el algoritmo
    de búsqueda binaria. Precondición: la lista debe estar
    ordenada """
    if len(lista_palabras) == 0:
        return False
    
    i = len(lista_palabras) // 2
    
    if lista_palabras[i] == palabra:
        # Encontrada
        return True    
    elif lista_palabras[i] > palabra:
        # Busca en la mitad izquierda
        return in_bisect(lista_palabras[:i], palabra)
    else:
        # busca en la mitad derecha
        return in_bisect(lista_palabras[i+1:], palabra) 

def in_bisect_chetao(lista_palabras, palabra):
    """ Busca una palabra en una lista usando el método bisect.
    Precondición: la lista debe estar ordenada """
    i = bisect.bisect_left(lista_palabras, palabra)
    
    if i == len(lista_palabras):
        return False
    
    return lista_palabras[i] == palabra
         

lista_palabras = crea_lista()

for palabra in ['aa', 'alien', 'allen', 'zymurgy']:
        print(palabra, 'en lista', in_bisect(lista_palabras, palabra))        

print()
for palabra in ['aa', 'alien', 'allen', 'zymurgy']:
        print(palabra, 'en lista', in_bisect_chetao(lista_palabras, palabra))
