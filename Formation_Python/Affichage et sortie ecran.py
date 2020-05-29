# -------------------
# Affichage et sortie écran
# -------------------
print('Ceci est une chaine de caractères')
	# Ceci est une chaine de caractères

# -------------------
# Format %s
c = 'CHAINE'
print ("Insérer une chaine à partir d'une variable: %s" %(c))
	# Insérer une chaine à partir d'une variable: CHAINE

# -------------------
# format %n1.n2f pour lequel n1 représente le nombre minimum de chiffres à représenter (substitués par des espaces si le nombre est plus petit)
# et n2 représente le nombre de chiffres à afficher après la virgule.
print('Nombre à virgule flottante : %1.2f' %(13.144))
	# Nombre à virgule flottante : 13.14
print('Nombre à virgule flottante : %1.0f' %(13.144))
	# Nombre à virgule flottante : 13

# -------------------
# Il faut noter que les deux méthodes %s et %r convertiront tout objet Python en chaine de caractères (string)
# en utilisant chacune une métode différente : str() et repr() respectivement.
print('Voici un nombre : %s. Voici une chaine : %s' %(123.1,'hi'))
	# Voici un nombre : 123.1. Voici une chaine : hi

print('Voici un nombre : %r. Voici une chaine : %r' %(123.1,'hi'))
	# Voici un nombre : 123.1. Voici une chaine : 'hi'

print('Premier : %s, Deuxième : %1.2f, Troisième : %r' %('hi!',3.14,22))
	# Premier : hi!, Deuxième : 3.14, Troisième : 22

# -------------------
# Utilisation de la méthode string .format()
print ('Voici une chaine avec un élement {p}'.format(p='inséré'))
	# Voici une chaine avec un élement inséré
print ('Un: {p}, Deux: {p}, Trois: {p}'.format(p='Salut !'))
	# Un: Salut !, Deux: Salut !, Trois: Salut !
print ('Objet 1: {a}, Objet 2: {b}, Objet 3: {c}'.format(a=1,b='deux',c=12.3))
	# Objet 1: 1, Objet 2: deux, Objet 3: 12.3

# -------------------
