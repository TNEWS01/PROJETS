# Programme Test

import os

# Class
class Personne:                 # Définition de notre classe Personne
    """Classe définissant une personne caractérisée par :
    - son nom
    - son prénom"""
    def __init__(self):         # Notre méthode constructeur
        self.nom = "Dupont"
        self.prenom = "Thierry"

# Fonctions
def aff(x):
    print("-" * 50)
    print(x)
    print("-" * 50)

# Début du programme
Dic1={
    "P":{"Nom":"F","Prenom":"T"},
    "M":{"Nom":"B","Prenom":"V"}
}

Label1 = Dic1["P"]["Nom"] + " & " + Dic1["M"]["Nom"]
aff(Label1)

Pers = Personne()
Label2 = Pers.nom + " " + Pers.prenom
aff(Label2)

# os.system("pause")
