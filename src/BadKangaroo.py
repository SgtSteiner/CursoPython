# -*- coding: utf-8 -*-
'''
Created on 2 jul. 2017

@author: Steiner
'''

class Kangaroo:
    
    def __init__(self, name, pouch_content=[]):
        self.name = name
        self.pouch_content = pouch_content
    
    def __str__(self):
        t = ["Contenido de %s: " % self.name ]
        for obj in self.pouch_content:
            s = "   " + object.__str__(obj)
            t.append(s)
        return "\n".join(t)
            
    def put_in_pouch(self, item):
        self.pouch_content.append(item)
        

kanga = Kangaroo("kanga")
roo = Kangaroo("roo")

a = [23, 3]
kanga.put_in_pouch("Llaves")
kanga.put_in_pouch(25.6)
kanga.put_in_pouch(divmod(25,4))
kanga.put_in_pouch(a)
kanga.put_in_pouch(roo)

print(kanga)
print(roo)
