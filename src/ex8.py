# Ejercicio nº 8 - Printing, printing

formatter = "%s %r %r %r"

print(formatter % (1, 2, 3, 4))
print(formatter % ("uno", "dos", "tres", "cuatro"))
print(formatter % (True, False, True, False))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
	"Tuve esta cosa.",
	"Línea 2",
	"Línea 3",
	"y línea 4")
)
