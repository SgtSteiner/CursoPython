# -*- coding: utf-8 -*-
""" Exercise 8: Printing, Printing
"""

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("uno", "dos", "tres", "cuatro"))
print(formatter.format(True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
	"con diez cañones por banda,",
	"viento en popa",
	"a toda vela,",
	"no corta el mar sino vuela"
	))
