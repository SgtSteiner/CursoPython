# -*- coding: utf-8 -*-
'''
Created on 18 jun. 2017

@author: Steiner

Calcula la raiz cuadrada de un número por el método de Newton
'''

import math

def miraiz(a, x):
    """ Calcula la raiz cuadrada de <a> dado un valor aproximado <x>
    usando el método de Newton"""
    epsilon = 0.0000001
    while True:
        raiz = (x + a/x) / 2
        if abs(raiz - x) < epsilon:
            return raiz
        x = raiz

print("a\t miraiz(a)\t math.sqrt(a)\t dif")
print("-\t ---------\t ------------\t ---")

for i in range(1, 10):
    print("%d\t" % i, end="")
    y = miraiz(i, i+10)
    y2 = math.sqrt(i)
    print("%f\t" % y, end="")
    print("%f\t" % y2, end="")
    print("%f" % (y-y2))    
        