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

for v in dic_anagramas.values():
    if len(v) > 1:
        print(v)
