# -------------------
# Les fichiers
# -------------------
# Écrire dans un fichier
# Par défaut, la fonction open() ne nous permettra que la lecture du fichier,
# il faut utiliser un argument 'w' pour pouvoir écrire

# Ajout d'un deuxième argument à la fonction.
# 'w' pour écrire ('write' en anglais)
# 'w+' pour écrire et lire
mon_fichier = open('test.txt','w+')

# -------------------
# Écrire dans le fichier
mon_fichier.write('Ligne1:Ceci est un petit fichier de test')
mon_fichier.write('Ligne2:Ceci est un petit fichier de test')

# Lire le fichier
mon_fichier.read()

# Fermer le fichier
mon_fichier.closed

# -------------------
# Ouvrir le fichier text.txt que nous venons de créer
mon_fichier = open('test.txt')

# Afficher chaque ligne d'un fichier
for ligne in mon_fichier:
	print(ligne)

# -------------------
# Pointer le début du fichier(index 0)
mon_fichier.seek(0)

# -------------------
# Lire une seule ligne
print(mon_fichier.readline())

# -------------------
# Readlines renvoie la liste des lignes du fichier
mon_fichier.seek(0)
print(mon_fichier.readlines())

# -------------------
