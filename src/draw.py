# -*- coding: utf-8 -*-
'''
Created on 29 jun. 2017

@author: Steiner
'''

import turtle

from Point1 import Point, Rectangle
from circle import Circle
import mypolygon

def draw_rect(t, rect):
    """ Dibuja un rectángulo usando turtle
    
        r: objeto Turtle
        rect: objeto Rectangle
    """
    
    t.pu()
    t.goto(rect.corner.x, rect.corner.y)
    t.pd()
    
    for length in rect.width, rect.height, rect.width, rect.height:
        t.fd(length)
        t.rt(90)

def draw_circle(t, circle):
    """ Dibuja un círculo usando turtle
    
        r: objeto Turtle
        circle: objeto Circulo
    """
    t.pu()
    t.goto(circle.center.x, circle.center.y)
    t.rt(90)
    t.fd(circle.radius)
    t.lt(90)
    t.pd()
    
    mypolygon.circulo(t, circle.radius)
    
if __name__ == "__main__":
    box = Rectangle()
    box.width = 170    
    box.height = 100
    box.corner = Point()
    box.corner.x = 150
    box.corner.y = 100
    
    bob = turtle.Turtle()
    draw_rect(bob, box)
    
    circle = Circle()
    circle.center = Point()
    circle.center.x = 0
    circle.center.y = 0
    circle.radius = 150
    
    draw_circle(bob, circle)
    
    turtle.mainloop()
    
    