# -*- coding: utf-8 -*-
'''
Created on 2 jul. 2017

@author: Steiner
'''

class Time:
    """ Representa la hora del día
    
        atributos: hora, minuto, segundo
    """
    def print_time(self):
        """ Imprime una cadena representado la hora
        t: objeto Time
        """
        print("%.2d:%.2d:%.2d" % (self.hora, self.minuto, self.segundo))

if __name__ == "__main__":
    time1 = Time()
    time1.hora = 23
    time1.minuto = 50
    time1.segundo = 36
    time1.print_time()