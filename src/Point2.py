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
        
    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_point(other)
        elif isinstance(other, tuple):
            return self.add_tupla(other)
        else:
            msg = "Point no sabe cómo sumar el tipo" + type(other)
            raise TypeError(msg)
        
    def add_point(self, other):
        """ Suma dos objetos Point """
        return Point(self.x + other.x, self.y + other.y)
    
    def add_tupla(self, other):
        """ Suma una tupa a un objeto Point """
        return Point(self.x + other[0], self.y + other[1])
    
if __name__ == "__main__":
    p1 = Point()
    print(p1)
    p2 = Point(3, 4)
    print(p2)
    
    print (p1 + p2)
    p3 = p2 + (2,3)
    print(p3)
    print(vars(p3))
    