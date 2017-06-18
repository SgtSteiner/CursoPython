# -*- coding: utf-8 -*-
'''
Created on 18 jun. 2017

@author: Steiner

Evalúa la función de Ackermann
'''

def ack(m, n):
    """ evalúa la función de Ackermann"""
    if m == 0:
        return n + 1
    elif n == 0:
        return ack(m - 1, 1)
    else:
        return ack(m - 1, ack(m, n - 1))
    
print(ack(3, 4))
