# -------------------
# Les listes
# -------------------
# Créer une liste et lui assigner le nom de variable ma_liste
ma_liste = [1,2,3]
print(ma_liste)

# -------------------
ma_liste = ['Une chaine',23,100.232,'o']
print(ma_liste)

# -------------------
# Nombre d'éléments dans la liste
ma_liste = ['un','deux','trois',4,5]
print(ma_liste)
print(len(ma_liste))

# -------------------
# Afficher l'élément à l'index 0
print(ma_liste[0])

# -------------------
# Afficher l'élément à l'index 1 et les suivants
print(ma_liste[1:])

# -------------------
# Tout afficher jusqu'à l'index 3
print(ma_liste[:3])

# -------------------
newlist = ma_liste + ['nouvel élément']
print(newlist)

# -------------------
# Dupliquer les entrées de la liste
dblist = ma_liste * 2
print(dblist)

# -------------------
# Créer une nouvelle liste
list1 = [1,3,2,5,4]

# Append
list1.append('ajoute moi !')
print(list1)

# Assigner l'élément extrait, rappelez-vus que l'index de l'élément extrait par défaut est -1
objsupprim = list1.pop()
print(objsupprim)
print(list1)

# Inversion - Ceci est permanent
list1.reverse()
print(list1)

# Utiliser sort pour trier la liste (dans ce cas par ordre alphabétique, pour des nombres en ordre ascendant)
# Ceci est permanent
list1.sort()
print(list1)

# -------------------
# Listes imbriquées

# Création de trois listes
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Faire une liste de listes va créer une matrice
matrice = [lst_1,lst_2,lst_3]

print(matrice)
	# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Afficher le premier élément de l'objet matrice
print(matrice[0])

# Afficher le premier élément du premier élément de l'objet matrice
print(matrice[0][0])

# -------------------
# Listes en compréhension
# Construire une liste en compréhension en déconstruisant une boucle for à l'intérieur de []
col_un = [ligne[0] for ligne in matrice]
print(col_un)
	# [1, 4, 7]



# -------------------

# -------------------

# -------------------

# -------------------

# -------------------

# -------------------
