# -------------------
# Boucles while
# -------------------
# Le format général de la boucle while est :
#
# while test:
#     lignes de code
# else:
#     lignes de codes de cloture

# -------------------
x = 0
while x < 10:
    print('x vaut : ',x)
    print(' x est toujours inférieur à 10, on ajoute 1 à x')
    x+=1

print(10 * "*")

# -------------------
x = 0
while x < 10:
	print('x vaut : ', x)
	print(' x est toujours inférieur à 10, on ajoute 1 à x')
	x += 1
else:
	print('Terminé !')


print(10 * "*")

# -------------------
# break, continue, pass
#
# Il est possible d'utiliser les instructions break, continue et pass dans les boucles pour avoir plus de fonctionnalités dans certains cas. Ces trois instructions sont définies par :
#
# break: Casse et sort de la boucle en cours.
# continue: Va directement au début de la boucle en cours.
# pass: Ne fait rien.
#
# Pour ce qui concerne les instructions break et continue, le format général de la boucle while ressemble à ceci :
#
# while test:
#     lignes de code
#     if test:
#         break
#     if test:
#         continue
# else:
# -------------------
x = 0
while x < 10:
    print('x vaut : ',x)
    print(' x est toujours inférieur à 10, on ajoute 1 à x')
    x+=1
    if x ==3:
        print('x==3')
    else:
        print('on contine...')
        continue

print(10 * "*")

# -------------------
x = 0
while x < 10:
    print ('x vaut : ',x)
    print (' x est toujours inférieur à 10, on ajoute 1 à x')
    x+=1
    if x ==3:
        print ('On arrête parce que x==3')
        break
    else:
        print ('on contine...')
        continue

print(10 * "*")

# -------------------
#
# # Surtout ne PAS exécuter ce CODE!!!!
# while True:
#     print ('Désastre, une boucle infinie !')
#
# -------------------
