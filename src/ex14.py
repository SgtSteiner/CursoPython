# -*- coding: utf-8 -*-
''' Exercise 14: Prompting and Passing
'''

from sys import argv

script, user_name = argv
prompt = "> "

print(f"Hola {user_name}, soy el script {script}.")
print("Me gustaría hacerte unas preguntas.")
print(f"¿Te gusto {user_name}?")
likes = input(prompt)

print(f"¿Dónde vives {user_name}?")
lives = input(prompt)

print(f"¿Qué tipo de computador tienes {user_name}?")
computer = input(prompt)

print(f"""
Ok, has dicho {likes} sobre si te gusto.
Vives en {lives}. No estoy seguro dónde está.
y tienes un {computer}. Fenomenal.
""")