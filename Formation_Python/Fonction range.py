# -------------------
# Fonction range()
# -------------------
# range() nous permet de générer une liste de nombres entiers allant d'une valeur de départ jusqu'à une valeur de fin.
# Nous pouvons également spécifier la taille du pas.
# -------------------
lst = list(range(0,10))
print(lst)
	#	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# -------------------
x =range(0,10)
print(type(x))

# -------------------
start = 0
stop = 20
x = range(start,stop)
lst = list(x)
print(lst)
	#	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# -------------------
x = range(start,stop,2)
lst = list(x)
print(lst)
	#	[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# -------------------
for num in range(10):
    print (num)

# -------------------
