# -------------------
# Boucles for
# -------------------
# Voici le format générique d'une boucle for avec Python :
# for élément in objet:
#     instruction pour réaliser quelque chose

# -------------------
# Nous verrons comment automatiser ce type de liste dans la prochaine leçon
l = [1,2,3,4,5,6,7,8,9,10]
print(l)

print(10*"*")

# -------------------
for num in l:
    print('Voici un nombre : %i' % num)

print(10*"*")

# -------------------
for num in l:
    if num % 2 == 0:
        print('Ce nombre %i est pair.' % num)

print(10*"*")

# -------------------
for num in l:
    if num % 2 == 0:
        print('Ce nombre %i est pair.' % num)
    else:
        print('Ce nombre %i est impair.' % num)

print(10*"*")

# ------------------
# La somme commence à zéro
somme_liste = 0
for num in l:
    somme_liste = somme_liste + num
print(somme_liste)

print(10*"*")

# -------------------
# La somme commence à zéro
somme_liste = 0
for num in l:
    somme_liste += num
print(somme_liste)

print(10*"*")

# -------------------

for lettre in 'Ceci est une chaine.':
    print(lettre)

print(10 * "*")

# -------------------
tup = (1,2,3,4,5)

for t in tup:
    print(t)

print(10 * "*")

# -------------------
l = [(2,4),(6,8),(10,12)]
print(l)
for tup in l:
    print(tup)

print(10 * "*")

# -------------------
for (t1,t2) in l:
    print(t1)

print(10 * "*")

# -------------------
d = {'clef1':1,'clef2':2,'clef3':3}

for x in d:
    print (x)

print(10 * "*")

# -------------------
for clef,valeur in d.items():
    print(clef)
    print(valeur)

print(10 * "*")

# -------------------
