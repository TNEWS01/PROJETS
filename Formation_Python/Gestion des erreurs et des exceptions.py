# -------------------
# Gestion des erreurs et des exceptions
# -------------------

# Type d'erreur
# print ('Bonjour)
	# File "<ipython-input-1-cce31fab3614>", line 1
	#     print ('Bonjour)
	#                     ^
	# SyntaxError: EOL while scanning string literal
	#

# Remarquez pourquoi nous obtenons une Erreur de Syntaxe (SyntaxError), avec l'expliquation supplémentaire
# qu'il s'agit en fait d'un EOL (End of Line Error) lors de la lecture de la chaîne de caractères.
# Ceci est assez précis pour comprendre que nous avons oublié une apostrophe à la fin de la chaine
# Ce type d'erreur et de description est connu sous le nom d'Exception

# Tous les Types d'exceptions
# https://docs.python.org/3.7/library/exceptions.html

# -------------------
# try et except
# -------------------
# Le code qui peut provoquer une exception est placé dans le bloc try et le traitement de l'exception est implémenté dans le bloc de code except. La syntaxe est la suivante :
#
# try:
#    Vos opérations sont ici...
#    ...
# except ExceptionI:
#    Si une ExceptionI ce produit, ce bloc sera exécuté.
# except ExceptionII:
#    Si une ExceptionII ce produit, ce bloc sera exécuté.
#    ...
# else:
#    S'il ne se produit pas d'exception, ce bloc sera exécuté.

# -------------------
# Exemple lors de l'écriture dans un fichier texte
try:
	f = open('fichiertest','w')
	f.write('On écrit une ligne')
except IOError:
	# Ceci va tester si une exception IOError se produit et afficher un message d'erreur
	print("Erreur: Fichier non trouvé ou données non lisibles")
else:
	print("Contenu écrit avec succès")
	f.close()

print(10 * "*")

# -------------------
# Exemple lors de l'écriture dans un fichier texte mais uniquement avec les droits de lectures
try:
	f = open('fichiertest','r')
	f.write('On écrit une ligne')
except IOError:
	# Ceci va tester si une exception IOError se produit et afficher un message d'erreur
	print("Erreur: Fichier non trouvé ou données non lisibles")
else:
	print("Contenu écrit avec succès")
	f.close()

print(10 * "*")

# -------------------
# Exemple lors de l'écriture dans un fichier texte mais uniquement avec les droits de lectures
try:
	f = open('fichiertest','r')
	f.write('On écrit une ligne')
except Exception as e:
	# Ceci va afficher le message d'erreur
	print("Erreur: {}".format(e))
else:
	print("Contenu écrit avec succès")
	f.close()

print(10 * "*")

# -------------------
# finally
# -------------------
# Le bloc de code finally: sera toujours exécuté, qu'il se produise ou non une exception dans le code du bloc try. Voici la syntaxe :
#
# try:
#    Le code du bloc ici...
#    ...
#    À cause d'une exception, ce code pourrait ne jamais être exécuté.
# finally:
#   Ce code sera toujours exécuté.

# -------------------
try:
	f = open('fichiertest','w')
	f.write('On écrit une ligne')
finally:
	print("Exécute toujours cette portion de code au final")

print(10 * "*")

# -------------------
def demandeInt():
	try:
		val = int(input("Merci de taper un entier : "))
	except:
		print("Il semble que vous n'avez pas tapé un entier !")
	finally:
		print("Je suis exécuté au final !")
	print(val)

demandeInt()

print(10 * "*")

# -------------------
# Demande à l'utilisateur et nous assurer que le type d'entrée est bien un entier !
def demandeInt():
	try:
		val = int(input("Merci de taper un entier : "))
	except:
		print ("Il semble que vous n'avez pas tapé un entier !")
		val = int(input("Essayez de nouveau - Merci de taper un entier : "))
	finally:
		print ("Je suis exécuté au final !")
	print (val)

demandeInt()


print(10 * "*")

# -------------------
# Boucle pour obtenir absolument un entier !
def demandeInt():
	while True:
		try:
			val = int(input("Merci de taper un entier : "))
		except:
			print ("Il semble que vous n'avez pas tapé un entier !")
			continue
		else:
			print("Merci, c'est bien un entier !")
			break
		finally:
			print ("Je suis exécuté au final !")
		print (val)

demandeInt()

# -------------------

# -------------------

# -------------------

# -------------------

# -------------------

# -------------------

# -------------------
