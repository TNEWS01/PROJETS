# -------------------
# Listes en compréhension
# -------------------
# Les listes en compréhension nous permettent de construire des listes en utilisant une notation différente.
# C'est essentiellement une façon d'écrire une boucle incluse entre des crochets sur une seule ligne

# -------------------
# Extraire chaque lettre de la chaine
liste = [x for x in 'exemple']
print(liste)

print(10 * "*")

# -------------------
# Liste crée à partir d'un range() de carrés
lst = [x**2 for x in range(0,11)]
print(lst)

print(10 * "*")

# -------------------
# Vérification de nombres pairs
lst = [x for x in range(11) if x % 2 == 0]
print(lst)

print(10 * "*")

# -------------------
# Conversion de Celsius en Fahrenheit
celsius = [0,10,20.1,34.5]

fahrenheit = [ ((float(9)/5)*temp + 32) for temp in celsius ]
print(celsius)
print(fahrenheit)

print(10 * "*")

# -------------------
lst = [ x**2 for x in [x**2 for x in range(11)]]
print(lst)

# -------------------
