# -------------------
# La Programmation Orientée Objet (POO)

# -------------------
# Objets
# -------------------

# En Python, tout est Objet
print (type('lettre'))
	# <class 'str'>

print (type(1))
	# <class 'int'>

print (type([]))
	# <class 'list'>

print (type(()))
	# <class 'tuple'>

print (type({}))
	# <class 'dict'>


# -------------------
# class
# -------------------

# Par convention, nous donnons aux classes un nom qui commence par une majuscule
# Une instance est un objet spécifique créé à partir d'une classe particulière
# Un attribut est une caractéristique d'un objet.
# Une méthode est une opération que nous pouvons effectuer avec l'objet.


# Création d'un objet de base appelé Exemple
class Exemple(object):
	pass

# Instance de Exemple
x = Exemple()
print (type(x))
	# <class '__main__.Exemple'>

print(10 * "*")


# -------------------
# Attributs
# -------------------

# La syntaxe de création d'un attribut est :
# self.attribut = quelque_chose
#
# Il y a une méthode spéciale qui s'appelle :
# __init__()
#
# Cette méthode va être utilisée pour initialiser les attributs d'un objet
# La méthode spéciale init() est appelée automatiquement après que l'objet a été créé (instancié)
#

class Chien(object):
	def __init__(self, race):
		self.race = race

sam = Chien(race='Labrador')
print(sam.race)

frank = Chien(race='Huskie')
print(frank.race)

print(10 * "*")

# -------------------
class Chien(object):
	# Attributs de Classe
	espece = 'mammifère'

	def __init__(self, race, nom):
		self.race = race
		self.nom = nom

sam = Chien('Lab','Sam')
print(sam.nom)
print(sam.race)
print(sam.espece)

print(10 * "*")


# -------------------
# Méthodes
# -------------------

# Les méthodes sont des fonctions définies dans le corps d'une classe.
# Elles sont utilisées pour effectuer des opérations avec les attributs de nos objets
#
# Vous pouvez simplement imaginer les méthodes comme des fonctions agissant sur un objet
# qui prennent l'objet lui-même en compte par le paramètre self

# -------------------
class Cercle(object):
	pi = 3.14

	# Le Cercle est instancié avec une rayon (1 par défaut)
	def __init__(self, rayon=1):
		self.rayon = rayon

	# La méthode surface calcule la surface. Noter comment est utilisé self.
	def surface(self):
		return self.rayon * self.rayon * Cercle.pi

	# Méthode pour redéfinir le rayon
	def definirRayon(self, rayon):
		self.rayon = rayon

	# Méthode for obtenir le rayon (comme en appelant simplement .rayon)
	def obtenirRayon(self):
		return self.rayon

c = Cercle()
c.definirRayon(2)
print('Le rayon est : ',c.obtenirRayon())
print('La surface est : ',c.surface())

print(10 * "*")


# -------------------
# Héritage de Class
# -------------------
# L'héritage est un moyen de créer de nouvelles classes à l'aide de classes existantes.
# Les classes nouvellement formées sont appelées classes dérivées, les classes dont nous dérivons sont appelées classes de base.
# Les avantages de l'héritage sont la réutilisation du code et la réduction de la complexité d'un programme.
# Les classes dérivées (descendants) remplacent ou étendent la fonctionnalité des classes de base (ancêtres).

# -------------------
class Animal(object):
	def __init__(self):
		print("Animal créé")

	def quiSuisJe(self):
		print("Je suis un animal")

	def mange(self):
		print("En train de manger")

class Chien(Animal):
	def __init__(self):
		Animal.__init__(self)
		print("Chien créé")

	def quiSuisJe(self):
		print("Je suis un chien")

	def aboie(self):
		print("Ouah !")

d = Chien()
d.quiSuisJe()
d.mange()
d.aboie()
#
# Dans cet exemple, nous avons deux classes: Animal et Chien. L'animal est la classe de base, le chien est la classe dérivée.
# La classe dérivée hérite des fonctionnalités de la classe de base.
#     Comme la méthode mange().
# La classe dérivée modifie le comportement existant de la classe de base.
#     Comme la méthode quiSuisJe().
# Enfin, la classe dérivée étend la fonctionnalité de la classe de base, en définissant une nouvelle méthode aboie().

print(10 * "*")


# -------------------
# Méthodes spéciales
# -------------------
# Ces méthodes ne sont pas réellement appelées directement mais par une syntaxe spécifique Python

class Livre(object):
	def __init__(self, titre, auteur, pages):
		print ("Un livre est créé")
		self.titre = titre
		self.auteur = auteur
		self.pages = pages

	def __str__(self):
		return "Titre : %s , auteur : %s, pages : %s " %(self.titre, self.auteur, self.pages)

	def __len__(self):
		return self.pages

	def __del__(self):
		print ("Un livre a été détruit")


liv = Livre("Python Rocks!", "Jose Portilla", 159)

print(liv.auteur)
print(liv.titre)
print(liv.pages)

print(liv.__str__())
print(liv.__len__())

liv.__del__()

# Les méthodes __init__(), __str__(), __len__() and the __del__() .
# Ces méthodes spéciales sont facilement identifiées par l'utilisation de caractères de soulignement
# dans leurs noms. Elles nous permettent d'appliquer des fonctions spécifiques de Python sur des objets créés avec nos classes.
# -------------------

