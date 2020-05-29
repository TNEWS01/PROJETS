# -------------------
# Les tuples
# -------------------
# Les tuples (que l'on peut trouver traduits en français par le terme n-uples) dans Python sont très similaires à des listes.
# Toutefois, contrairement aux listes ces objets sont immuables ce qui veut dire tout simplement qu'ils ne sont pas modifiables

# -------------------
# Il est possible de créer un Tuple avec différents types
t = (1,2,3)
print(t)

# -------------------
# On peut en obtenir la taille avec len comme pour les listes
print(len(t))

# -------------------
# Il est possible d'avoir des éléments de type différents
t = ('un',2,'trois')
print(t)

# -------------------
# On peut utiliser des index comme nous l'avons fait dans les listes
print(t[0])

# -------------------
# On peut aussi accéder à rebours comme avec les listes
print(t[-1])

# -------------------
# Les Méthodes de base des Tuples

# La methode .index permet d'ajouter une valeur de retourner le numéro d'index
i = t.index('un')
print(i)

# La méthode .count permet de compter le nombre de fois qu'une valeur est présente dans le Tuple
c = t.count('un')
print(c)

# -------------------
