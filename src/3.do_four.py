# Ejercicio que muestra c�mo pasar una funci�n como argumento de otra funci�n


def imprime_texto(cadena):
    print(cadena)


def imprime_dosveces(f, cadena):
    f(cadena)
    f(cadena)

def imprime_cuatro(f, cadena):
	imprime_dosveces(f,cadena)
	imprime_dosveces(f,cadena)


imprime_cuatro(imprime_texto, "Dabuten, t�o")
