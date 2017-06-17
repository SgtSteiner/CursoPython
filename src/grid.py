# Dibuja una tabla de 4 filas y cuatro columnas


def imprime_eje():
    print("+----+----+", end="")
    print("----+----+")


def imprime_blancos():
    print("|    |    |", end="")
    print("    |    |")


def imprime_blancos_cuatroveces():
    imprime_blancos()
    imprime_blancos()
    imprime_blancos()
    imprime_blancos()


def imprime_tabla():
    imprime_eje()
    imprime_blancos_cuatroveces()
    imprime_eje()
    imprime_blancos_cuatroveces()


imprime_tabla()
imprime_tabla()
imprime_eje()

