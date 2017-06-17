# Justifica a la derecha un texto


def justifica_der(cadena):
    cols = 80
    print(" " * (cols - len(cadena)), cadena)


justifica_der("Dabuten tío")
