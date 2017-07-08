# -*- coding: utf-8 -*-
""" Exercise 6: Strings and Text
"""

tipos_de_personas = 10
x = f"Existen {tipos_de_personas} tipos de personas."

binario = "binario"
no_saben = "no"
y = f"Aquellas que saben {binario} y las que {no_saben}."

print(x)
print(y)

print(f"Dije: {x}")
print(f"También dije: {y}")

divertido = True
evaluacion_broma = "¿No es divertida esta broma? {}"

print(evaluacion_broma.format(divertido))

w = "Este es el lado izquierdo de..."
e = "una cadena con una lado derecho"

print(w + e)
