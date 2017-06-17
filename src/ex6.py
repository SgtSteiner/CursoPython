# Ejercicio nº 6 - Strings and Text

x = "Existen %d tipo de personas." % 10
binario = "binario"
no_saben = "no"
y = "Aquellas que saben %s y las que %s." % (binario, no_saben)

print(x)
print(y)

print("Dije: %r" % x)
print("También dije: '%s'" % y)

divertido = True
evaluacion_broma = "¿No es divertida esta broma? %s"

print(evaluacion_broma % divertido)

w = "Este es el lado izquierdo de..."
e = "una cadena con una lado derecho"

print(w + e)
