# -*- coding: utf-8 -*-
'''
Created on 6 jul. 2017

@author: Steiner
'''

from Card import Baraja, Mano

class ManoPoker(Mano):
    """ Representa una mano de póker
    """
    
    def hacer_hist(self):
        """ Devuelve un histograma con los palos y rangos que aparecen en la mano
        
            Almacena el resultado en el atributo <palos> y <rangos>
        """
        self.palos = {}
        self.rangos = {}
        for carta in self.cartas:
            self.palos[carta.palo] = self.palos.get(carta.palo, 0) + 1
            self.rangos[carta.rango] = self.rangos.get(carta.rango, 0) + 1
        
    def tiene_color(self):
        """ Devuelve verdadero si la mano contiene color, es decir,
            cinco cartas del mismo palo
        
            return: boolean
        """
        for valor in self.palos.values():
            if valor >= 5 :
                return True
        return False
    
    def tiene_pareja(self):
        """ Devuelve verdadero si la mano contiene una pareja, es decir
            dos carta con el mismo rango 
        """
        for valor in self.rangos.values():
            if valor == 2:
                return True
        return False
        
    def tiene_doble_pareja(self):
        """ Devuelve verdadero si la mano contiene doble pareja, es decir
            dos pares de cartas con el mismo rango 
        """
        i = 0
        for valor in self.rangos.values():
            if valor == 2:
                i +=1
        return i == 2

    def tiene_trio(self):
        """ Devuelve verdadero si la mano contiene trio, es decir
            tres cartas con el mismo rango 
        """
        i = 0
        for valor in self.rangos.values():
            if valor == 3:
                i +=1
        return i == 3
    
    def tiene_escalera(self):
        """ Devuelve verdadero si la mano contiene escalera, es decir
            cinco cartas consecutivas en el mismo rango, no necesariam.
            del mismo palo. 
        """
        pass
    
        
if __name__ == "__main__":
    # Crea una baraja
    for ronda in range(100):
        baraja = Baraja()
        baraja.barajar_cartas()
    
        # Reparte las cartas y clasifica las manos
        for i in range(7):
            mano = ManoPoker()
            baraja.mueve_cartas(mano, 7)
            mano.ordena_cartas()
            mano.hacer_hist()
            #print(mano.palos)
            print(mano.rangos)
            #print(mano)
            if mano.tiene_color():
                print("Color")
            if mano.tiene_pareja():
                print("Pareja")
            if mano.tiene_doble_pareja():
                print("Doble Pareja")
            if mano.tiene_trio():
                print("Trío")
            if mano.tiene_escalera():
                print("Escalera")
    