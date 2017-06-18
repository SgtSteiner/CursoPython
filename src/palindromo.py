# -*- coding: utf-8 -*-
'''
Created on 18 jun. 2017

@author: Steiner
'''

def primera(palabra):
    """ Devuelve el primer carácter de una cadena"""
    return palabra[0]

def ultima(palabra):
    """ Devuelve el último carácter de una cadena"""
    return palabra[-1]

def medio(palabra):
    """ Devuelve toda la cadena menos el primer y último carácter"""
    return palabra[1:-1]

def es_palindromo(cadena):
    """ Devuelve verdadero si la cadena es palíndroma"""
    if len(cadena) <= 1:
        return True
    if primera(cadena) != ultima(cadena):
        return False
    return es_palindromo(medio(cadena))
     
palabra = input("Introduce una cadena para comprobar si es un palíndromo: ")
print(es_palindromo(palabra))
