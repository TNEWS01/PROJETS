# -------------------
# Les Sets et les Booléens
# -------------------

# -------------------
# Set
# -------------------
x = set()

# Nous pouvons ajouter des éléments avec la méthode add
x.add(1)
print(x)

# Ajouter un élement différent
x.add(2)

# Essaye d'ajouter un élément déjà présent
x.add(1)
print(x)

# -------------------
# Création d'un set avec les éléments uniques d'une liste avec des éléments dupliqués
l1 = [1,1,2,2,3,4,5,6,1,1]
print(l1)

# Redéfinie en set pour isoler les éléments uniques
s1 = set(l1)
print(s1)

# -------------------

# -------------------
# Booléens
# -------------------
# Définir un objet avec le type Booléen
a = True
print('a =', a)

# -------------------
# La sortie produite est un booléen
r1 = 1 > 2
print('r1 = %s' %(r1))

# -------------------
# Réserver l'espace avec None
b = None
print('b = {}'.format(b))

# -------------------

