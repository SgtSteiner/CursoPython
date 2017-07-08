# -*- coding: utf-8 -*-
''' Exercise 15: Reading Files
'''

from sys import argv

script, filename = argv
fin = open(filename)

print(f"Aquí está tu archivo {filename}:")
print(fin.read())
fin.close()

print("Teclee el nombre del archivo de nuevo:")
file_again = input("> ")

fin = open(file_again)
print(fin.read())
fin.close()