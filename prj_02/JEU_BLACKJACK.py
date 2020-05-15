# -*-coding:utf-8 -*

#=================
# Jeu du BlackJack
#=================

# Import des modules
#===================
import random

# Initialisation des Variables, des Tuples et des Dictionnaires
#==============================================================
types = ('Coeur', 'Carreau', 'Pique', 'Trefle')
rangs = ('Deux', 'Trois', 'Quatre', 'Cinq', 'Six', 'Sept', 'Huit', 'Neuf', 'Dix', 'Vallet', 'Dames', 'Roi', 'As')
valeurs = {'Deux':2, 'Trois':3, 'Quatre':4, 'Cinq':5, 'Six':6, 'Sept':7, 'Huit':8, 'Neuf':9, 'Dix':10, 'Vallet':10, 'Dames':10, 'Roi':10, 'As':11}
jeu_encours = True

# Définition des Classes
#=======================
class Carte:
	def __init__(self,type,rang):
		self.type = type
		self.rang = rang

	def __str__(self):
		return self.rang + ' de ' + self.type

class Deck:
	def __init__(self):
		self.deck = []  		# Initialisation avec une liste vide
		for type in types:
			for rang in rangs:
				self.deck.append(Carte(type,rang))

	def __str__(self):
		deck_comp = ''  		# Initialisation de la composition du deck avec une chaine vide
		for carte in self.deck:
			deck_comp += '\n '+carte.__str__()		# Ajout de la chaine d'impression de chaque objet "Carte"
		return 'Le deck est composé de :' + deck_comp

	def melange(self):
		random.shuffle(self.deck)

	def distrib_carte(self):
		carte_unique = self.deck.pop()
		return carte_unique

class Main:
	def __init__(self):
		self.cartes = []		# Initialisation avec une liste vide comme dans la class Deck
		self.valeur = 0			# Initialisation de la main à 0
		self.aces = 0				# Initilaisation d'une variable pour suivre les as

	def ajout_carte(self,carte):
		self.cartes.append(carte)
		self.valeur += valeurs[carte.rang]
		if carte.rang == 'As':
			self.aces += 1

	def ajust_as(self):
		while self.valeur > 21 and self.aces:
			self.valeur -= 10
			self.aces -= 1

class Jetons:
	"""
		Class Jetons :
		- Définition des jetons du joueur en début de partie
		- Calcul des jetons du joueur si le pari est gagné
		- Calcul des jetons du joueur si le pari est perdu
	"""
	def __init__(self):
		self.total = 100
		self.pari = 0

	def gagne_pari(self):
		self.total += self.pari

	def perd_pari(self):
		self.total -= self.pari

# Définition des Fonctions
#=========================
def prendre_pari(jetons):
	while True:
		try:
			jetons.pari = int(input("\nCombien de jetons voulez-vous parier ? : "))
		except ValueError:
			print("\nDésolé, votre pari doit être un nombre entier !")
		else:
			if jetons.pari > jetons.total:
				print("\nDésolé, votre pari ne peut pas dépasser : ",jetons.total)
			elif jetons.pari == 0:
				print("\nDésolé, votre pari ne peut être nul : ", jetons.pari)
			else:
				break

def pioche(deck,main):
	main.ajout_carte(deck.distrib_carte())
	main.ajust_as()

def continuer_ou_stopper(deck,main):
	global jeu_encours

	while True:
		x = input("\nVoulez-vous continuer ou stopper votre demande de cartes ? Entrer 'c' ou 's' : ")

		if x[0].lower() == 'c':
			pioche(deck,main)
		elif x[0].lower() == 's':
			print("\nVous stoppé. Donc le croupier va jouer...")
			jeu_encours = False
		else:
			print("Desolé, essayer une nouvelle fois.")
			continue
		break

def affiche_partiel(joueur,croupier):
	print(20 * "*")
	print("Main du croupier :")
	print(" <carte cachée>")
	print('',croupier.cartes[1])
	print(20 * "*")
	print("Main du joueur :", *joueur.cartes, sep='\n ')
	print(20 * "*")
def affiche_tout(joueur,croupier):
	print(20 * "*")
	print("Main du croupier :", *croupier.cartes, sep='\n ')
	print("Valeur de la main du croupier= ",croupier.valeur)
	print(20 * "*")
	print("Main du joueur :", *joueur.cartes, sep='\n ')
	print("Valeur de la main du joueur = ",joueur.valeur)
	print(20 * "*")
def joueur_perd(joueur,croupier,jetons):
	print("\nVous avez perdu car vous avez dépassé 21 !")
	jetons.perd_pari()

def joueur_gagne(joueur,croupier,jetons):
	print("\nVous avez gagné car vous êtes au dessus du croupier !!!")
	jetons.gagne_pari()

def croupier_perd(joueur,croupier,jetons):
	print("\nVous avez gagné car le croupier a dépassé 21 !")
	jetons.gagne_pari()

def croupier_gagne(joueur,croupier,jetons):
	print("\nVous avez perdu car vous êtes en dessous du croupier !")
	jetons.perd_pari()

def egalite(joueur,croupier):
	print("\nVous êtes à égalité avec le croupier ! Aucun gain.")


# Script Principal
#=================

print("""
******************************************************************************
Bienvenu au BlackJack ! Rapprochez-vous le plus possible de 21 sans dépasser !
Le croupier pioche jusqu'à ce que sa main atteigne au moins 17.
Les as comptent pour 1 ou 11.
******************************************************************************""")

# Initialise la mise du joueur
jetons_joueur = Jetons()  # Rappel de la Valeur par defaut définie dans la Class Jetons : 100 Jetons

print("\nBonne nouvelle ! le casino vous offre {} jetons !".format(jetons_joueur.total))

while True :
	print("""
*********************
Nouvelle partie ...
*********************""")
	print("\nVous possédez {} jetons".format(jetons_joueur.total))

	# Création et mélange du deck, distibution de 2 cartes
	deck = Deck()
	deck.melange()

	main_joueur = Main()
	main_joueur.ajout_carte(deck.distrib_carte())
	main_joueur.ajout_carte(deck.distrib_carte())

	main_croupier = Main()
	main_croupier.ajout_carte(deck.distrib_carte())
	main_croupier.ajout_carte(deck.distrib_carte())

	# Invite le joueur à parier
	prendre_pari(jetons_joueur)

	# Affichage des cartes :
	affiche_partiel(main_joueur,main_croupier)

	while jeu_encours:  	# Cette variable est valorisée dans la fonction continuer_ou_stopper

		# Demande au joueur s'il continue à demander des cartes ou s'il stoppe
		continuer_ou_stopper(deck,main_joueur)
		affiche_partiel(main_joueur,main_croupier)

		if main_joueur.valeur > 21:
			joueur_perd(main_joueur,main_croupier,jetons_joueur)
			break

	# Si le joueur n'a pas dépasser 21, c'est alors au croupier de jouer      
	if main_joueur.valeur <= 21:

		while main_croupier.valeur < 17:
			pioche(deck,main_croupier)

		# Affichage des cartes du joueur et du croupier
		affiche_tout(main_joueur,main_croupier)

		# Test des différents scénarii du jeu
		if main_croupier.valeur > 21:
			croupier_perd(main_joueur,main_croupier,jetons_joueur)
		elif main_croupier.valeur > main_joueur.valeur:
			croupier_gagne(main_joueur,main_croupier,jetons_joueur)
		elif main_croupier.valeur < main_joueur.valeur:
			joueur_gagne(main_joueur,main_croupier,jetons_joueur)
		else:
			egalite(main_joueur,main_croupier)

	# Infomation sur le total des jetons du joueur   
	print("\nVous possédez au total {} jetons".format(jetons_joueur.total))

	# Rejouer une partie
	new_game = input("\nVoulez-vous jouer une nouvelle fois ? Entrer 'o' ou 'n' ")
	if new_game[0].lower()=='o':
		jeu_encours=True
		continue
	else:
		print("\nMerci d'avoir joué ! \nVous repartez du casino avec {} !".format(jetons_joueur.total))
		break
