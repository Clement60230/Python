# Intitulé : Exercice 17 - Palindrome
# Auteur : FIOT Clément
# Formation : M2i - L3
# Date butoir : 06/11/2019

# Initialisation de la Fonction Palindrome
def Palindrome(mot):

    # Declaration de la variable m et de la variable inverse qui correspond au mot inversé du mot
    m = mot
    inverse = m[::-1]

    # Bloc qui va permettre de définir si le mot est un palindrome ou non
    # Si le mot est identique au mot inversé de ce mot alors
    if m == inverse:
        # On affiche le mot inversé
        print(inverse)
        # On retourne le message 'Le mot est un Palindrome'
        return('Le mot est un Palindrome')
    else:
        print(inverse)
        # Sinon on retourne le message 'Le mot n'est pas un palindrome'
        return('Le mot n est pas un palindrome')

# Resultat qui fera appel à la fonction Palindrome avec input qui permettra de rentrer notre mot
resultat=Palindrome(input())

# Affichage du resultat
print(resultat)