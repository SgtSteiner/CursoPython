# -*- coding: utf-8 -*-
'''
Created on 2 jul. 2017

@author: Steiner
'''

class Point:
    """ Representa un punto en el espacio 2-D 
        Atributos: x, y
    """
    def __init__(self, x=0, y=0):
        """ Inicializa el objeto Point
        
            x: int
            y: int
        """
        self.x = x
        self.y = y
        
    def __str__(self):
        """ Imprime las coordenadas de un objeto Point """
        return "(%g, %g)" % (self.x, self.y)
        
if __name__ == "__main__":
    p1 = Point()
    print(p1)