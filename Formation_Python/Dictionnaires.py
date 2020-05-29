# -------------------
# Les dictionnaires
# -------------------
# Création d'un dictionnaire avec {} et : pour spécifier la clef et sa valeur
mon_dict = {'clef1':'valeur1','clef2':'valeur2'}
print(mon_dict)
	# {'clef1': 'valeur1', 'clef2': 'valeur2'}

# Retrouver une valeur avec sa clef
print(mon_dict['clef2'])
	# valeur2

# -------------------
mon_dict = {'clef1':123,'clef2':[12,23,33],'clef3':['item0','item1','item2']}
print(mon_dict['clef3'])
	# ['item0', 'item1', 'item2']
print(mon_dict['clef3'][0])
	# item0
print(mon_dict['clef3'][0].upper())
	# ITEM0
# Soustraire 123 de la valeur
# mon_dict['clef1'] = mon_dict['clef1'] - 123
mon_dict['clef1'] -= 123
print(mon_dict['clef1'])
	# 0

# -------------------
# Crée un nouveau dictionnaire vide
d = {}
# Crée une nouvelle clef par assignation
d['animal'] = 'Chien'
# On peut faire cela avec n'importe quel objet
d['réponse'] = 42
print(d)
	# {'animal': 'Chien', 'réponse': 42}

# -------------------
# Dictionnaires imbriqués
# Dictionnaire imbriqué dans un dictinnaire imbriqué dans un dictinnaire
d = {'clef1':{'sousclef':{'sousousclef':'valeur'}}}

# Il faut mettre les clef dans le bon ordre
print(d['clef1']['sousclef']['sousousclef'])
	# valeur

# -------------------
# Créer un dictionnaire
d = {'clef1':1,'clef2':2,'clef3':3}

# Méthode qui renvoie la liste des clefs
print(d.keys())
	# dict_keys(['clef1', 'clef2', 'clef3'])

# Méthode qui extrait toutes les valeurs
print(d.values())
	# dict_values([1, 2, 3])

# Méthode qui renvoie un Tuple pour chaque item (Nous verrons les Tuples très prochainement)
print(d.items())
	# dict_items([('clef1', 1), ('clef2', 2), ('clef3', 3)])

# -------------------
