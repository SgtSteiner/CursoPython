# -*- coding: utf-8 -*-
'''
Created on 26 jun. 2017

@author: antonio.mendez
'''

import shelve
from anagram_sets import all_anagram, ord_cadena

def store_anagrams(filename, anagram_map):
    """ Almacena un map de anagramas en database "shelf"
    
    filename = nombre de la base de datos
    anagram_map = diccionario de anagramas
    """
    shelf = shelve.open(filename, 'c')
    for key in anagram_map:
        if len(anagram_map[key]) > 1:
            shelf[key] = anagram_map[key]

def read_anagrams(filename, palabra):
    """ Devuelve los anagramas almacenados de una palabra 
    
    filename = nombre de la base de datos
    paalbra = palabra a buscar
    """
    shelf = shelve.open(filename)
    palabra_ord = ord_cadena(palabra)
    try:
        return shelf[palabra_ord]
    except KeyError:
        return []

if __name__ == "__main__":
    dic_anagramas = all_anagram("words.txt")
    store_anagrams("anagrams.db", dic_anagramas)
    
    palabra = "opst"
    print(read_anagrams("anagrams.db", palabra))
    