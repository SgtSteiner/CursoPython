# Ejercicio que muestra cómo pasar una función como argumento de otra función


def imprime_texto(cadena):
    print(cadena)


def imprime_dosveces(f, cadena):
    f(cadena)
    f(cadena)

def imprime_cuatro(f, cadena):
	imprime_dosveces(f,cadena)
	imprime_dosveces(f,cadena)


imprime_cuatro(imprime_texto, "Dabuten, tío")
