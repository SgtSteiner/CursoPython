# -*- coding: utf-8 -*-
'''
Created on 29 jun. 2017

@author: Steiner
'''

from Point1 import Point, Rectangle, print_point, distance_between_point
import copy

class Circle:
    """ Representa un círculo
    
    atributos: center, radius"""
    
def point_in_circle(punto, circulo):
    """ Devuelve verdadero si el punto está dentro del círculo
        
        punto = objeto Point
        circulo = objeto Circulo
        
        return: boolean
    """
    d = distance_between_point(circulo.center, punto)
    return d <= circulo.radius

def rect_in_circle(rectangulo, circulo):
    """ Devuelve verdadero si el rectángulo está dentro del círculo
    
        rectangulo = objeto Rectangle
        circulo = objeto Circle
        
        return: boolean
    """
    p = copy.copy(rectangulo.corner)
    print_point(p)
    if not point_in_circle(p, circulo):
        return False
    
    p.x += rectangulo.width
    print_point(p)
    if not point_in_circle(p, circulo):
        return False
    
    p.y -= rectangulo.height
    print_point(p)
    if not point_in_circle(p, circulo):
        return False
    
    p.x -= rectangulo.width
    print_point(p)
    if not point_in_circle(p, circulo):
        return False
    
    return True
    
def rect_in_circle_overlap(rectangulo, circulo):
    """ Devuelve verdadero si algún vértice del rectángulo 
        está dentro del círculo
    
        rectangulo = objeto Rectangle
        circulo = objeto Circle
        
        return: boolean
    """
    p = copy.copy(rectangulo.corner)
    print_point(p)
    if point_in_circle(p, circulo):
        return True
    
    p.x += rectangulo.width
    print_point(p)
    if point_in_circle(p, circulo):
        return True
    
    p.y -= rectangulo.height
    print_point(p)
    if point_in_circle(p, circulo):
        return True
    
    p.x -= rectangulo.width
    print_point(p)
    if point_in_circle(p, circulo):
        return True
    
    return False

if __name__ == "__main__":
    circulo = Circle()
    circulo.center = Point()
    circulo.center.x = 150
    circulo.center.y = 100
    circulo.radius = 75
    
    print("Centro del círculo: ", end="")
    print_point(circulo.center)
    print()
    print("Radius: %d" % circulo.radius)
    
    punto1 = Point()
    punto1.x = 125
    punto1.y = 70
    print(point_in_circle(punto1,circulo))
    
    box = Rectangle()
    box.width = 10    
    box.height = 100
    box.corner = Point()
    box.corner.x = 150
    box.corner.y = 100
    print(rect_in_circle(box, circulo))
    print(rect_in_circle_overlap(box, circulo))