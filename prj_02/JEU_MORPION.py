# -*-coding:utf-8 -*

#=================
# Jeu du Morpion
#=================

# Import des modules
#===================
import random
from IPython.display import clear_output

# Définition des Fonctions
#=========================
def affiche_tableau(tableau):
	clear_output()
	print('   |   |')
	print(' ' + tableau[7] + ' | ' + tableau[8] + ' | ' + tableau[9])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + tableau[4] + ' | ' + tableau[5] + ' | ' + tableau[6])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + tableau[1] + ' | ' + tableau[2] + ' | ' + tableau[3])
	print('   |   |')

def pion_joueur():    
	marque = ''
	while not (marque == 'X' or marque == 'O'):
		marque = input('Joueur 1: Est-ce que vous voulez jouer X ou O ?').upper()

	if marque == 'X':
		return ('X', 'O')
	else:
		return ('O', 'X')

def place_marque(tableau, marque, position):
	tableau[position] = marque
	
def verif_gagnant(tableau, marque):
	return ((tableau[7] == marque and tableau[8] == marque and tableau[9] == marque) or	# ligne du haut
	(tableau[4] == marque and tableau[5] == marque and tableau[6] == marque) or			# ligne du milieu
	(tableau[1] == marque and tableau[2] == marque and tableau[3] == marque) or			# ligne du bas
	(tableau[7] == marque and tableau[4] == marque and tableau[1] == marque) or			# colonne de gauche
	(tableau[8] == marque and tableau[5] == marque and tableau[2] == marque) or			# colonne du milieu
	(tableau[9] == marque and tableau[6] == marque and tableau[3] == marque) or			# colonne de droite
	(tableau[7] == marque and tableau[5] == marque and tableau[3] == marque) or			# diagonale
	(tableau[9] == marque and tableau[5] == marque and tableau[1] == marque))			# diagonale

def choix_premier():
	if random.randint(0, 1) == 0:
		return 'Joueur 2'
	else:
		return 'Joueur 1'

def verif_position(tableau, position):
	return tableau[position] == ' '

def verif_tableau_complet(tableau):
	for i in range(1,10):
		if verif_position(tableau, i):
			return False
	return True

def choix_du_joueur(tableau):
	# On a lu une chaine
	position = ' '
	while position not in '1 2 3 4 5 6 7 8 9'.split() or not verif_position(tableau, int(position)):
		position = input('Choisissez la position où vous voulez jouer : (1-9) ')
	return int(position)

def rejouer():
	return input('Est-ce que vous voulez jouer à nouveau ? Répondez par Oui ou par Non : ').lower().startswith('o')
	
# Script Principal
#=================
print('Bienvenue dans le jeu du Morpion !')

while True:
	# Préparer le tableau
	leTableau = [' '] * 10
	marque_joueur1, marque_joueur2 = pion_joueur()
	tour = choix_premier()
	print(tour + ' va commencer.')
	jeu_en_cours = True

	while jeu_en_cours:
		if tour == 'Joueur 1':
			# Tour du joueur 1
			affiche_tableau(leTableau)
			position = choix_du_joueur(leTableau)
			place_marque(leTableau, marque_joueur1, position)

			if verif_gagnant(leTableau, marque_joueur1):
				affiche_tableau(leTableau)
				print('Bravo ! Vous avez gagné !')
				jeu_en_cours = False
			else:
				if verif_tableau_complet(leTableau):
					affiche_tableau(leTableau)
					print('Match nul !')
					break
				else:
					tour = 'Joueur 2'
		else:
			# Tour du joueur 2
			affiche_tableau(leTableau)
			position = choix_du_joueur(leTableau)
			place_marque(leTableau, marque_joueur2, position)

		if verif_gagnant(leTableau, marque_joueur2):
			affiche_tableau(leTableau)
			print('Le joueur 2 a gagné !')
			jeu_en_cours = False
		else:
			if verif_tableau_complet(leTableau):
				affiche_tableau(leTableau)
				print('Vous êtes à égalité !')
				break
			else:
				tour = 'Joueur 1'

	if not rejouer():
		break
