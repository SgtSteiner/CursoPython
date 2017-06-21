# -*- coding: utf-8 -*-
'''
Created on 21 jun. 2017

@author: antonio.mendez
'''

def invertir_dic(d):
    dic_inverso = dict()
    for key in d:
        valor = d[key]
        dic_inverso.setdefault(valor,[]).append(key)
    return dic_inverso

fin = open("words.txt")

d = dict()
for palabra in fin:
    d[palabra.strip()]=len(palabra.strip())

inverso = invertir_dic(d)
print(len(inverso))
for key in inverso:
    print("Palaras de long %d: " % key, len(inverso[key]))