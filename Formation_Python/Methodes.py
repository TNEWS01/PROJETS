# -------------------
# Les méthodes
# -------------------
# Les méthodes sont de la forme :
# objet.méthode(parm1,parm2,etc...)

# -------------------
# Création d'une liste simple
l = [1,2,3,4,5]
print(l)

# Les méthodes pour une liste sont les suivantes :
#
#     append
#     count
#     extend
#     insert
#     pop
#     remove
#     reverse
#     sort

# -------------------
l.append(6)
print(l)

# -------------------
# Vérifie combien de fois 2 apparait dans la liste
nc = l.count(2)
print(nc)

# -------------------
print('Affichage de l\'aide de la méthode')
help(l.count)

# -------------------
