# Programme Test 1
##################

import os

# Class
class Personne:
	ctg = "Civil"
	
	def __init__(self,prenom,nom,age,sexe):
		self.prenom = prenom
		self.nom = nom
		self.age = age
		self.sexe = sexe
		
	def identite(self,carte_ident,permis):
		print("Prénom : {}".format(self.prenom))
		print("Nom : {}".format(self.nom))
		print("Age : {}".format(self.age))
		print("Sexe : {}".format(self.sexe))
		print("Carte Identité : {}".format(carte_ident))
		print("Permis : {}".format(permis))
		print("Catégorie : {}".format(Personne.ctg))
		
# Programme principal
if __name__ == "__main__":
	pers_1 = Personne("Jean","Durand",35,"masculin")

	# print("Prénom : {}".format(pers_1.prenom))
	# print("Nom : {}".format(pers_1.nom))
	# print("Age : {}".format(pers_1.age))
	# print("Sexe : {}".format(pers_1.sexe))

	print(pers_1.identite("oui","non"))
	
	