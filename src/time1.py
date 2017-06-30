# -*- coding: utf-8 -*-
'''
Created on 29 jun. 2017

@author: Steiner
'''

import copy

class Time:
    """ Representa la hora del día
    
        atributos: hora, minuto, segundo
    """

def print_time(t):
    """ Imprime una cadena representado la hora
    
        t: objeto Time
    """
    print("%.2d:%.2d:%.2d" % (t.hora, t.minuto, t.segundo))

def is_after(t1, t2):
    """ Devuelve verdadero si la hora t1 es posterior a la hora t2
    
        t1: objeto Time
        t2: objeto Time
    """
    return (t1.hora, t1.minuto, t1.segundo) > (t2.hora, t2.minuto, t2.segundo)

def add_time(t1, t2):
    """ Suma dos objetos Time
    
        t1: objeto Time
        t2: objeto Time
        
        return: objeto Time
    """
    sum = Time()
    sum.hora = t1.hora + t2.hora
    sum.minuto = t1.minuto + t2.minuto
    sum.segundo = t1.segundo + t2.segundo
    
    if sum.segundo >= 60:
        sum.segundo -= 60
        sum.minuto += 1
        
    if sum.minuto >= 60:
        sum.minuto -= 60
        sum.hora += 1
        
    return sum
              
def increment(time, segundos):
    """ Añade segundos a un objeto Time 
    
        time: objeto Time
        segundos: segundos
        
        return: objeto Time
    """
    t1 = copy.copy(time)
    t1.segundo += segundos
    minutos, t1.segundo = divmod(t1.segundo, 60)
    t1.minuto += minutos
    horas, t1.minuto = divmod(t1.minuto, 60)
    t1.hora += horas
    return t1
    
if __name__ == "__main__":
    time1 = Time()
    time1.hora = 23
    time1.minuto = 50
    time1.segundo = 36
    
    print_time(time1)
    
    time2 = Time()
    time2.hora = 15
    time2.minuto = 59
    time2.segundo = 25
    
    print(is_after(time1, time2))
    
    start = Time()
    start.hora = 15
    start.minuto = 10
    start.segundo = 20
    
    duration = Time()
    duration.hora = 1
    duration.minuto = 55
    duration.segundo = 50
    
    done = add_time(start, duration)
    print_time(done)
    
    t_increm = increment(done, 140)
    print_time(t_increm)