# -*- coding: utf-8 -*-
'''
Created on 18 jun. 2017

@author: Steiner

Evalúa lo que se introduce hasta que el usuario teclea "done" 
'''

while True:
    cadena = input("¿Qué deseas evaluar (fin=<done>)?")
    if cadena.lower() == "done":
        break
    print(eval(cadena))
    