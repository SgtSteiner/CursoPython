# -*- coding: utf-8 -*-
"""
Exercise 4: Variables and Names
"""

# Asigna 100 a la variable 'coches'
coches = 100
# Asigna 4.0 a la variabla 'capacidad_en_un_coche'
capacidad_en_un_coche = 4.0
# Asigna 30 a la variable 'conductores'
conductores = 30
# Nº de pasajeros
pasajeros = 90

# Calcula el nº de coches sin conductor
coches_sin_conductor = coches - conductores

# Calcula el nº de coches con conductor
coches_con_conductor = conductores

# Calcula la capacidad del pool de coches
capacidad_pool_coches = coches_con_conductor * capacidad_en_un_coche

# Calcula la media de pasajeros por coche
media_pasajeros_por_coche = pasajeros / coches_con_conductor

print("Existen", coches, "coches disponibles.")
print("Existen solo", conductores, "conductores disponibles.")
print("Hoy quedarán", coches_sin_conductor, "coches sin conductor.")
print("Hoy podemos transportar", capacidad_pool_coches, "personas.")
print("Hoy tenemos", pasajeros, "de capacidad en los coches.")
print("Necesitamos meter alrededor de", media_pasajeros_por_coche, "en cada coche.")