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
    """ Devuelve un mapep con todos los anagramagras del archivo
    
    filename = nombre del archivo a procesar 
    """
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

def print_all_anagram(d):
    """ Imprime los anagramas mapeados en d """
    for v in d.values():
        if len(v) > 1:
            print(v)

def print_all_anagram_ascend(d):
    """ Imprime los anagramas mapeados en d en 
    orden ascendente según el tamaño de la palabra 
    
    d = dict de anagramas
    """
    lis_anagramas = []
    for valor in d.values():
        if len(valor) > 1:
            lis_anagramas.append((len(valor), valor))

    lis_anagramas.sort()
    print("-" * 80)
    for item in lis_anagramas:
        print(item)
        
def print_anagram_size(d, size=8):
    """ Imprime los anagramas de tamaño <size> mapeados en d
    
    d = dict de anagramas
    size = tamaño de los anagramas
    """
    for key in d:
        if len(key) == size and len(d[key]) > 1:
            print(d[key])
    
if __name__ == '__main__':
    dic_anagramas = all_anagram("words.txt")

    # Imprime todos los anagramas encontrados
    print_all_anagram(dic_anagramas)

    # Imprime los anagramas en orden ascendente
    print_all_anagram_ascend(dic_anagramas)
    
    # Imprime los anagramas que tiene longitud = 8
    print_anagram_size(dic_anagramas)
    