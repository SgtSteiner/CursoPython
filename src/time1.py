# -*- coding: utf-8 -*-
'''
Created on 29 jun. 2017

@author: Steiner
'''

from datetime import datetime

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

def time_to_int(time):
    """ Convierte a numérico un objeto Time
    
        time: objeto Time
        
        return: entero, representando los segundos
    """
    minutos = time.hora * 60 + time.minuto
    segundos = minutos * 60 + time.segundo
    return segundos
    
def int_to_time(n_segundos):
    """ Convierte segundos a un objeto Time
    
        n_segundos: nº de segundos
        
        return: objeto Time
    """
    time = Time()
    time.minuto, time.segundo = divmod(n_segundos, 60)
    time.hora, time.minuto = divmod(time.minuto, 60)
    return time
        
def add_time(t1, t2):
    """ Suma dos objetos Time
    
        t1: objeto Time
        t2: objeto Time
        
        return: objeto Time
    """
    assert valid_time(t1) and valid_time(t2)
    segundos = time_to_int(t1) + time_to_int(t2)
    return int_to_time(segundos)
              
def increment(time, segundos):
    """ Añade segundos a un objeto Time 
    
        time: objeto Time
        segundos: segundos
        
        return: objeto Time
    """
    segundos += time_to_int(time)
    return int_to_time(segundos)

def mul_time(time, i):
    """ Multiplica un objeto Time por un factor
        
        time: objeto Time
        i: entero 
        
    return: objeto Time
    """
    assert valid_time(time)
    segundos = time_to_int(time) * i
    return int_to_time(segundos)
    
def valid_time(time):
    """ Devuelve verdadero si es un objeto Time 
        correctamente formado 
        
        time= objeto Time
        
        return: boolean
    """
    if time.hora < 0 or time.minuto < 0 or time.segundo < 0:
        return False
    if time.minuto >= 60 or time.segundo >= 60:
        return False
    return True
        
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
    
    # Suma dos tiempos
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
    
    # Incrementa segundos a un tiempo dado
    t_increm = increment(done, 140)
    print_time(t_increm)
    
    print_time(mul_time(t_increm,7))
    
    # Calcula la velocidad media por km
    race = Time()
    race.hora = 1
    race.minuto = 24
    race.segundo = 30
    dist = 10  # km
    print("Tiempo en recorrer %g km.: " % dist, end="")
    print_time(race)
    tiempo_medio = mul_time(race, 1/dist)
    print("Velocidad media de ", end="")
    print_time(tiempo_medio)
    
    # Muestra el día de la semana
    hoy = datetime.today()
    print(hoy.weekday())
    print(hoy.strftime("%A"))
    
    # Calcula la edad
    birthday = datetime(1967, 12, 5)
    hoy = datetime.today()
    print("Tienes %d años" % (hoy.year - birthday.year))