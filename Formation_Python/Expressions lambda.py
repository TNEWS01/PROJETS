# -------------------
# Les expressions lambda
# -------------------
# Les expressions lambda nous permettent de créer des fonctions "anonymes".
# Cela veut dire que nous pouvons rapidement faire des fonctions ad-hoc sans avoir besoin de définir correctement une fonction en utilisant def.
# -------------------
# Fonction classique Façon N°1
def carre(num):
    résultat = num**2
    return résultat

print(carre(2))

# -------------------
# Fonction classique Façon N°2
def carre(num):
    return num**2

print(carre(2))

# -------------------
# Fonction classique Façon N°3
def carre(num): return num**2

print(carre(2))

# -------------------
# Fonction lambda
carre = lambda num: num**2

print(carre(2))

# -------------------
pair = lambda x: x%2==0

print(pair(6))
print(pair(3))

# -------------------
premier = lambda s: s[0]

caract1 = premier('bonjour')
print(caract1)

# -------------------
addition = lambda x,y : x+y

print(addition(2,3))

# -------------------
