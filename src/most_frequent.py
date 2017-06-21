# -*- coding: utf-8 -*-
'''
Created on 21 jun. 2017

@author: Steiner
'''

def make_histogram(cadena):
    """ Crea un diccionario con las veces que 
    aparece cada letra en una cadena """
    hist = dict()
    for c in cadena:
        hist[c] = hist.get(c, 0) + 1
        
    if "\n" in hist:
        del hist["\n"] 
    return hist

def ord_histogram(d):
    """ Devuelve el histograma ordenado según la 
    frecuencia de aparición de las letras """
    
    lista_letras = []
    total_frec = 0
    for letra, frecuencia in d.items():
        lista_letras.append((frecuencia, letra))
        total_frec += frecuencia
        
    lista_letras.sort(reverse = True)
    return lista_letras, total_frec


texto = open("words.txt").read()
d = make_histogram(texto)
frecuencia_letras, total_frec = ord_histogram(d)
for item in frecuencia_letras:
    print("Letra: %s \tFrecuencia: %d \tPorcentaje: %f" % (item[1], item[0], item[0] / total_frec))
    


