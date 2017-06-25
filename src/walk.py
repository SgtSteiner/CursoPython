# -*- coding: utf-8 -*-
'''
Created on 25 jun. 2017

@author: Steiner
'''

import os
from test.support import change_cwd

def camina(nombre_dir):
    for nombre in os.listdir(nombre_dir):
        path = os.path.join(nombre_dir, nombre)
        
        if os.path.isfile(path):
            print(path)
        else:
            camina(path)
            
cwd = "C:\\Users\\Steiner\\git"
camina(cwd)