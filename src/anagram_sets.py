# -*- coding: utf-8 -*-
'''
Created on 21 jun. 2017

@author: Steiner
'''

def ord_cadena(s):
    """ devuelve una cadena ordenada """
    cadena = list(s)
    cadena.sort()
    cadena = "".join(cadena)
    return cadena

def all_anagram(filename):
    
    fin = open(filename)
    d_anagramas = dict()
    
    for linea in fin:
        palabra = linea.strip()
        ord_palabra = ord_cadena(palabra) 
        if ord_palabra not in d_anagramas:
            d_anagramas[ord_palabra] = [palabra]
        else:
            d_anagramas[ord_palabra].append(palabra) 
    return d_anagramas

dic_anagramas = all_anagram("words.txt")

# Imprime todos los anagramas encontrados
for v in dic_anagramas.values():
    if len(v) > 1:
        print(v)

# Imprime los anagramas en orden ascendente
lis_anagramas = []
for valor in dic_anagramas.values():
    if len(valor) > 1:
        lis_anagramas.append((len(valor), valor))

lis_anagramas.sort()
print("-" * 80)
for item in lis_anagramas:
    print(item)
    
# Imprime los anagramas que tiene longitud = 8
print("-" * 80)
for x, y in lis_anagramas:
    if x == 8:
        print(y)