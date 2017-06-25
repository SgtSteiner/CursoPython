# -*- coding: utf-8 -*-
'''
Created on 25 jun. 2017

@author: Steiner
'''

import os

def camina(nombre_dir):
    """ Imprime recursivamente los archivos en el interior del directorio dado """
    for nombre in os.listdir(nombre_dir):
        path = os.path.join(nombre_dir, nombre)
        
        if os.path.isfile(path):
            print(path)
        else:
            camina(path)
            
def camina2(nombre_dir):
    """ Imprime recursivamente los archivos en el interior del directorio dado 
    usando os.walk() """
    for root, dirs, files in os.walk(nombre_dir):
        for archivo in files:
            path = os.path.join(root, archivo)
            print(path)

cwd = "C:\\Users\\Steiner\\git"

camina(cwd)
print("*" * 80)
camina2(cwd)
