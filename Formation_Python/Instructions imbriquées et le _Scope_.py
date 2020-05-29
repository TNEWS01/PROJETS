# -------------------
# Les instructions imbriquées et le _Scope_
# # -------------------
# La règle LEGB.
#
# L: Local — Les noms assignés à l'intérieur d'une fonction (def or lambda), et qui ne sont pas déclarés global dans cette fonction.
#
# E: Enclosing function locals — Variables locales de la fonction appelante - Nom utilisés en local dans une des fonctions appelante (def or lambda), de l'intérieur vers l'extérieur.
#
# G: Global (module) — Noms assignés au niveau le plus au du module, ou déclarés comme global dans une des fonctions (def ou lambda) de ce module.
#
# B: Built-in (Python) — Noms préassignés dans les modules et fonctions intégrés de Python : open,range,SyntaxError,...
#
# -------------------
x = 25
def afficher():
    x = 50
    return x
print (x)
print (afficher())

print(10 * "*")

# -------------------
# Local
f = lambda x:x**2

print(10 * "*")

# -------------------
# Local de la fonction appelante
nom = 'Cette variable est globale'
def bienvenue():
	# Fonction appelante
	nom = 'Sammy'
	def bonjour():
		print('Bonjour ' + nom)
	bonjour()

bienvenue()

# -------------------
# Global
print (nom)

print(10 * "*")

# -------------------
# Variables locales
x = 50
def fonction(x):
	print ('x vaut', x)
	x = 2
	print ('La valeur locale de x a changé pour ', x)

fonction(x)
print( 'x est toujours ', x)

print(10 * "*")

# -------------------
x = 50
def fonction():
	global x
	print ('Cette fonction utilise maintenant la variable globale x !')
	print ('La valeur de cette variable x globale est : ', x)
	x = 2
	print ('La fonction est exécutée, la valeur de la variable globale x est maintenant ', x)

print ("Avant l'appel de fonction(), x vaut: ", x)
fonction()
print ('Valeur de x (hors de fonction()) : ', x)

print(10 * "*")

# -------------------
