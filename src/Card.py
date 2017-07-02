# -*- coding: utf-8 -*-
'''
Created on 2 jul. 2017

@author: Steiner
'''

import random

class Carta:
    """ Representa una carta estándar del juego
    
    Atributos:
        palo: integer 0-3
        rango: integer 1-13
    """
    
    def __init__(self, palo=0, rango=2):
        self.palo = palo
        self.rango = rango
    
    palo_names = ["Tréboles", "Diamantes", "Corazones", "Picas"]
    rango_names = [None, "As", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "Sota", "Reina", "Rey"]
    
    def __str__(self):
        """ Devuelve una representación legible de la Carta """
        return "%s de %s" % (Carta.rango_names[self.rango], 
                             Carta.palo_names[self.palo])
        
    def __lt__(self, other):
        """ Compara esta carta con otra, primero por palo
            y luego por rango
        """
        tupla1 = self.palo, self.rango
        tupla2 = other.palo, other.rango
        return tupla1 < tupla2

class Baraja:
    """ Representa una baraja de cartas 
    
    Atributos:
        cartas: lista de objetos Carta 
    """
    
    def __init__(self):
        self.cartas = []
        for palo in range(4):
            for rango in range(1, 14):
                carta = Carta(palo, rango)
                self.cartas.append(carta)
    
    def __str__(self):
        """ Devuelve una representación legible de la Baraja """
        res = []
        for carta in self.cartas:
            res.append(str(carta))
        return "\n".join(res)            
            
    def borra_carta(self, i=-1):
        """ Borra una carta de la baraja 
        
            i: indice de la carta a borrar; por defecto, la última
        """
        return self.cartas.pop(i)
    
    def add_carta(self, carta):
        """ Añade una carta a la baraja 
        
            carta: objeto Carta
        """
        return self.cartas.append(carta)
    
    def barajar_cartas(self):
        """ Baraja las cartas de la baraja """
        return random.shuffle(self.cartas)
    
    def ordena_cartas(self):
        """ Ordena ascendentemente las cartas de la baraja """
        return self.cartas.sort()
    
    def mueve_cartas(self, mano, num):
        """ Mueve el numero de cartas indicado de la baraja a la mano
        
            mano = objeto Mano
            num = integer número de cartas a mover
        """
        for i in range(num):
            carta = self.borra_carta()
            mano.add_carta(carta)
            
class Mano(Baraja):
    """ Representa una mano de cartas de juego
    """
    def __init__(self, etiqueta=""):
        self.cartas = []
        self.etiqueta = etiqueta
        
if __name__ == "__main__":
    carta1 = Carta(1, 12)
    carta2 = Carta(0, 13)
    
    print(carta1, carta2)
    print(carta1 < carta2)
    
    baraja = Baraja()
    baraja.barajar_cartas()
    
    mano1 = Mano("Primera mano")
    baraja.mueve_cartas(mano1, 5)
    print(mano1)
    print()
    mano2 = Mano("Segunda mano")
    mano1.mueve_cartas(mano2, 3)
    print(mano1)
    print()
    print(mano2)