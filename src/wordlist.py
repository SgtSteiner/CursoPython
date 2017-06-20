# -*- coding: utf-8 -*-
'''
Created on 18 jun. 2017

@author: Steiner
'''
import time

def crea_lista():
    """ Crea una lista de palabras usando el método append
    a partir de un archivo de texto """
    fin = open("words.txt")
    lista_palabras = []
    for linea in fin:
        lista_palabras.append(linea.strip())
    return lista_palabras

def crea_lista_concatenacion():
    """ Crea una lista de palabras usando el método de concatenar
    elementos a partir de un archivo de texto """
    fin = open("words.txt")
    lista_palabras = []
    for linea in fin:
        lista_palabras += [linea.strip()]
    return lista_palabras    

tiempo = time.time()
lista_con_append = crea_lista()
print("contador = %d" % len(lista_con_append))
print(lista_con_append[:10])
tiempo = time.time() - tiempo
print(tiempo)

tiempo = time.time()
lista_con_conca = crea_lista_concatenacion()
print("contador = %d" % len(lista_con_conca))
print(lista_con_conca[:10])
tiempo = time.time() - tiempo
print(tiempo)

