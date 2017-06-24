# -*- coding: utf-8 -*-
'''
Created on 24 jun. 2017

@author: Steiner
'''

import string

def procesa_fichero(filename, skip_header):
    """ Devuelve un histograma con las
    palabra una archivo de texto.
    
    filename = nombre del archivo <filename> 
    skip_header = Boolean. Si quieres saltar la cabecera del archivo"""
    
    hist = {}
    fin = open(filename, encoding="utf8")
    
    if skip_header:
        # Lee el fichero hasta el fin de la cabecera
        for linea in fin:
            if linea.startswith("*** START OF THIS PROJECT GUTENBERG"):
                break
    
    for linea in fin:
        for pa in (linea.split()):
            # Elimina los signos de puntuación
            palabra = pa.strip(string.punctuation + string.whitespace + "¿¡")
            palabra = palabra.lower()
            # Actualiza el histograma
            hist[palabra] = hist.get(palabra, 0) + 1
            
    return hist

def mas_comunes(hist):
    """ Devuelve una lista de pares (frecuencia - palabra)
    hist = histograma con las palabras y su frecuencia """
    t = []
    
    for key in hist:
        t.append((hist[key], key))
    t.sort()
    t.reverse()
    return t

    
hist = procesa_fichero("LaRegenta.txt", skip_header=True)

print("Número de palabras del archivo %d" % sum(hist.values()))
print("Número de palabras diferentes %d" % len(hist))
print("Las 20 palabras más comunes son:")
print("--------------------------------")
t = mas_comunes(hist)
for frec, palabra in t[:20]:
    print(frec, palabra)
