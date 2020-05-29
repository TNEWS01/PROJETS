# -------------------
# Les chaines de caractères
# -------------------
print("Le double guilemet évite les problème d'apostrophe")
print('Le double guilemet évite les problème d\'apostrophe')
# -------------------
print('Ceci \n permet de sauter une ligne')
print('\n')
print('Vous voyez ce que je veux dire ?')
# -------------------
# longueur d'une chaine
print(len('Bonjour le monde'))
	# 16

# -------------------
# Indexation et découpage de chaines de caractères
s = 'Bonjour le monde'
print(s[0])
	# B
print(s[1:])
	# onjour le monde
print(s[:3])
	# Bon
print(s[:])
	# Bonjour le monde
print(s[-1])
	# e
print(s[:-1])
	# Bonjour le mond
print(s[::1])
	# Bonjour le monde
print(s[::2])
	# Bnorl od
print(s[::-1])
	# ednom el ruojnoB

# -------------------
s = 'Bonjour le monde'

# Concaténer des chaines de caractères!
print(s + ' ajoute moi !')
	# Bonjour le monde ajoute moi !

s = s + ' ajoute moi !'
print(s)
	# Bonjour le monde ajoute moi !

# -------------------
lettre = 'z'
print(lettre*10)
	# zzzzzzzzzz

# -------------------
# Mettre une chaine en majuscules
print(s.upper())
	# BONJOUR LE MONDE AJOUTE MOI !
# -------------------
print(s.lower())
	# bonjour le monde ajoute moi !
# -------------------
# Couper une chaine par les caractères espace (le défaut)
print(s.split())
	# ['Bonjour', 'le', 'monde', 'ajoute', 'moi', '!']

# Couper une chaine sur un caractère spécifique (l'élément qui sert au découpage n'est pas inclus)
print(s.split('l'))
	# ['Bonjour ', 'e monde ajoute moi !']
# -------------------
print('Insérer une chaine avec des acolades : {}'.format('la chaine insérée'))
	# Insérer une chaine avec des acolades : la chaine insérée

# -------------------
