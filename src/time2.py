# -*- coding: utf-8 -*-
'''
Created on 2 jul. 2017

@author: Steiner
'''

class Time:
    """ Representa la hora del día
    
        atributos: hora, minuto, segundo
    """
    def __init__(self, hora=0, minuto=0, segundo=0):
        """ Inicializa el objeto Time
            
            hora = int
            minuto = int
            segundo = int o float
        """
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
    
    def __str__(self):
        return "%.2d:%.2d:%.2d" % (self.hora, self.minuto, self.segundo)
    
    def __add__(self, other):
        """ Suma dos objetos Time o un objeto Time y un entero o float 
        
            other: objeto Time o número de segundos
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
        
    def __radd__(self, other):
        """ Suma dos objetos Time o un objeto Time y un entero o float """
        return self.__add__(other)
    
    def print_time(self):
        """ Imprime una cadena representado la hora """
        print("%.2d:%.2d:%.2d" % (self.hora, self.minuto, self.segundo))

    def time_to_int(self):
        """ Devuelve el nº de segundos de un objeto Time
        
            return: entero, representando los segundos
        """
        minutos = self.hora * 60 + self.minuto
        segundos = minutos * 60 + self.segundo
        return segundos
     
    def add_time(self, other):
        """ Suma dos objetos Time """
        assert valid_time(self) and valid_time(other)
        segundos = self.time_to_int() + other.time_to_int()
        return int_to_time(segundos)
        
    def increment(self, segundos):
        """ Devuelve un nuevo objeto Time con la suma de los segundos
        
            segundos: segundos
            
            return: objeto Time
        """
        segundos += self.time_to_int()
        return int_to_time(segundos)
    
    def is_after(self, other):
        """ Devuelve verdadero si la hora t1 es posterior a la hora t2 """
        return (self.hora, self.minuto, self.segundo) > (other.hora, other.minuto, other.segundo)   

def int_to_time(n_segundos):
    """ Convierte segundos a un objeto Time
    
        n_segundos: nº de segundos
        
        return: objeto Time
    """
    time = Time()
    time.minuto, time.segundo = divmod(n_segundos, 60)
    time.hora, time.minuto = divmod(time.minuto, 60)
    return time

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
    start = Time()
    print(start)
    
    start.hora = 23
    start.minuto = 50
    start.segundo = 36
    
    start.print_time()
    print(start.time_to_int())
    
    t_increm = start.increment(25)
    t_increm.print_time()
    
    print(start.is_after(t_increm))
    
    print(start + t_increm)
    print(start + 24.7)
    
    total = sum([start, t_increm])
    print(total)