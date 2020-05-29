# -------------------
# Opérateurs logiques
# -------------------
# Ces opérateurs vont nous permettre de comparer des variables
# et de produire un Bouléen Vrai (True) ou Faux (False) en fonction du résultat.

# -------------------
#  Tableau de comparison des opérateurs
#  Opérateur		Description		Exemple
#  == 		Si les valeurs des deux opérandes sont égales, alors la condition est vraie. 								(a == b) n'est pas vrai.
#  != 		Si les valeurs des deux opérandes ne sont pas égales, alors la condition est vraie. 						(a != b) est vrai
#  > 		Si la valeur de l'opérande gauche est supérieure à celle de droite, alors la condition est vraie. 			(a > b) n'est pas vrai.
#  < 		Si la valeur de l'opérande gauche est inférieure à celle de droite, alors la condition est vraie. 			(a < b) est vrai.
#  >= 		Si la valeur de l'opérande gauche est supérieure ou égale à celle de droite, alors la condition est vraie. 	(a >= b) n'est pas vrai.
#  <= 		Si la valeur de l'opérande gauche est inférieure ou égale à celle de droite, alors la condition est vraie.. (a <= b) est vrai.

# -------------------
# chainer les tests logiques avec deux opérateurs indispensables "et" and et "ou" or

x = int(2)
if 1 < x < 3:
	print('Vrai')
else:
	print('Faux')

print(10 * "*")

# -------------------
x = int(5)
if 1 < x > 2:
	print('Vrai')
else:
	print('Faux')

print(10 * "*")

# -------------------

x = int(2)
if x>1 and x<3:
	print('Vrai')
else:
	print('Faux')

print(10 * "*")

# -------------------
x = int(2)
if 1==x or x<3:
	print('Vrai')
else:
	print('Faux')

print(10 * "*")

# -------------------
x = int(1)
if 1==x or 100==x:
	print('Vrai')
else:
	print('Faux')

print(10 * "*")
# -------------------
