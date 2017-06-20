# -*- coding: utf-8 -*-
'''
Created on 20 jun. 2017

@author: antonio.mendez
'''

def nested_sum(t):
    """ Devuelve la suma de todos los enteros de una 
    lista de listas """
    sumatorio = 0
    for n_lista in t:
        sumatorio += sum(n_lista)
    return sumatorio

def cumsum(t):
    """ Devuelve una lista con la suma acumulada de los 
    elementos de una lista """
    res = []
    sumatorio = 0
    for elemento in t:
        sumatorio += elemento
        res.append(sumatorio) 
    return res

def middle(t):
    """ Recibe una lista y la devuelve sin el primer y
    último elemento """
    return t[1:-1]

def chop(t):
    """ Recibe una lista y elimina el primer y último
    elemento """
    del t[0]
    del t[-1]

def is_sorted(t):
    """ Devuelve verdadero si la lista está ordenada """
    return t == sorted(t)

def is_anagram(a, b):
    """ Devuelve verdadero si las dos palabras son anagramas """
    return sorted(a) == sorted(b)
    
def has_duplicates(t):
    """ Devuelve verdadero si cualquier elemento  de la lista
    aparece más de una vez """
    t2 = list(t)
    t2.sort()
    for indice in range(0, len(t2)-1):
        if t2[indice] == t2[indice+1]:
            return True
    return False
    
# suma los enteros de una lista de listas
t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))

# devuelve la suma acumulativa de todos los elementos
t = [1, 3, 6, 3, 2]
print(cumsum(t))

# devuelve la lista sin el primer y último elementos
t = ["E", "s", "t", "o", "e", "s", "u", "n", "a", "l", "i", "s", "t", "a"]
print(middle(t))

# devuelve la lista sin el primer y último elementos
t = ["E", "s", "t", "o", "e", "s", "u", "n", "a", "l", "i", "s", "t", "a"]
chop(t)
print(t)

# Comprueba si una lista está ordenada
t = [1, 3, 6, 8, 14]
print(is_sorted(t))

# Comprueba si dos palabras son anagramas
print(is_anagram('stop', 'pots'))
print(is_anagram('different', 'letters'))
print(is_anagram([1, 2, 2], [2, 1, 2]))

# Comprueba si una lista tiene algún elemento duplicado
print(has_duplicates('cba'))
print(has_duplicates('abba'))