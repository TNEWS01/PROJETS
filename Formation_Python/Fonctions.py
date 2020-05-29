# -------------------
# Fonctions
# -------------------
# Les fonctions sont une des façons les plus simples de réutilisation de code en Python,
# et elles vont nous permettre de commencer à penser à la conception de programmes
# -------------------
# L' instruction def
#
# def nom_de_fonction(parm1, parm2):
# 	'''
# 	C'est l'endroit où placer la description de la fonction (doc-string)
# 	'''
# 	# Ici, on fait des chose
# 	# Et on retourne le résultat
#
# # Ce n'est plus la fonction

# -------------------
def bienvenue(nom):
    print('Bonjour %s' %nom)

bienvenue('Marc')

# -------------------
def ajoute_nombre(nombre1,nombre2):
	return nombre1+nombre2

result = ajoute_nombre(4,5)
print(result)

# -------------------
def est_premier(num):
	'''
    Méthode simple de vérification de nombre premiers
    '''
	for n in range(2,num):
		if num % n == 0:
			print('non premier')
			break
	else: 	# si on a parcouru la boucle sans jamais avoir de reste à 0, le nombre est premier
		print('premier')

est_premier(14)

# -------------------
import math

def est_premier(num):
	'''
	Méthode plus évoluée de vérifier les nombres premiers
	'''
	if num % 2 == 0 and num > 2:
		return False
	for i in range(3, int(math.sqrt(num)) + 1, 2):
		if num % i == 0:
			return False
	return True

result = est_premier(14)
print(result)

# -------------------
