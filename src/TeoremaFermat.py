# -*- coding: utf-8 -*-
'''
Created on 18 jun. 2017

@author: Steiner

Dados 4 parametros: a, b, c y n, se demuestra que es cierto el último
teorema de Fermat, que dice que si n es un número entero mayor que 2,
entonces no existen números enteros positivos x, y y z, tales que se 
cumpla la igualdad: 

x elevado n + y elevado n = z elevado n
'''

x = int(input("Introduce el valor de x: "))
y = int(input("Introduce el valor de y: "))
z = int(input("Introduce el valor de z: "))
n = int(input("Introduce el valor de n (n>2): "))

if x ** n + y ** n == z ** n:
    print("¡¡Holly shit!! El teorema no es correcto")
else:
    print("El teorema de Fermat es correcto")
    
