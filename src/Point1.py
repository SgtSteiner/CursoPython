# -*- coding: utf-8 -*-
'''
Created on 28 jun. 2017

@author: Steiner
'''

import math
import copy

class Point:
    """ Representa un punto en el espacio 2-D 
        Atributos: x, y
    """

class Rectangle:
    """ Representa un rectángulo
        Atributos: width, height, corner
    """

def print_point(p):
    """ Imprime las coordenadas de un objeto Punto 
        p = Objeto Punto
    """
    print("(%g, %g)" % (p.x, p.y), end="")
     
def distance_between_point(p1, p2):
    """ Devuelve la distancia entre dos objetos punto
     
        p1 y p2 = Objetos Puntos
        
        return: float
    """
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2) 

def find_center(rect):
    """ Devuelve un objeto Punto como centro del rectángulo 
        
        rect = Objeto rectángulo
        
        return: new Point()
    """
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p
    
def grow_rectangle(rect, dwidth, dheight):
    """ Modifica un objeto Rectángulo añadiendo ancho y alto
        
        rect: objeto Rectangulo
        dwidth: incremento de width (puede ser negativo)
        dheight: incremento de height (puede ser negativo
    """
    rect.width += dwidth
    rect.height += dheight

def move_rectangle(rect, dx, dy):
    """ Mueve la posición de un objeto Rectángulo
        
        rect = objeto Rectangulo
        dx = añade a la coordenada x (puede ser negativo)
        dy = añade a la coordenada y (puede ser negativo)
    """
    rect.corner.x += dx
    rect.corner.y += dy

def move_rectangle_copy(rect, dx, dy):
    """ Mueve la posición de un objeto Rectángulo
        
        rect = objeto Rectangulo
        dx = añade a la coordenada x (puede ser negativo)
        dy = añade a la coordenada y (puede ser negativo)
        
        return = new objeto Rectangulo
    """
    new_rect = copy.deepcopy(rect)
    move_rectangle(new_rect, dx, dy)
    return new_rect
    
if __name__ == "__main__":
    punto1 = Point()
    punto1.x = -4
    punto1.y = 0
    
    punto2 = Point()
    punto2.x = 5
    punto2.y = 0

    dist = distance_between_point(punto1, punto2)

    print("La distancia entre los puntos ", end=""), print_point(punto1)
    print(" y ", end=""), print_point(punto2)
    print(" es: %f" % dist)
    
    box = Rectangle()
    box.width = 100    
    box.height = 200
    box.corner = Point()
    box.corner.x = 20
    box.corner.y = 30
    
    p_centro = find_center(box)
    print("El centro del rectángulo es: ", end="")
    print_point(p_centro)
    print()
    
    grow_rectangle(box, 50, 100)
    print(box.width, box.height)
    
    move_rectangle(box, 60, 120)
    print(box.corner.x, box.corner.y)
    
    new_box = move_rectangle_copy(box, 60, 120)
    print(new_box.corner.x, new_box.corner.y)