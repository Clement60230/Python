# Intitulé : Exercice 16 - Distance entre deux mots (Hamming)
# Auteur : FIOT Clément
# Formation : M2i - L3
# Date butoir : 30/10/2019

# Initialisation de la Fonction distance_hamming
def distance_hamming(mot1, mot2):

    # Initialisation de la distance à 0 (C'est elle qui comptera au final le nombre d'endroits ou les lettres sont différentes)
    distance = 0

    # Declaration des deux variables m1 et m2 qui correspondent aux deux mots
    m1 = mot1
    m2 = mot2

    # Bloc qui va permettre de calculer le nombre d'endroits ou les lettres sont différentes, entre deux mots de même longueur
    # Si la longueur des deux mots est identique alors
    if len(m1) == len(m2):
        # Pour la valeur i dans la range du premier mot (par exemple Japon = 5 lettres, donc la range est de 0 à 5)
        for i in range(len(m1)):
            #On ajoute 1 à la distance si à chaque endroit parcouru (en fonction de la range), les caractères sont différents
            if m1[i] != m2[i]:
                distance = distance + 1
        # On renvoie la distance finale qui correspond au nombre d'endroits ou les lettres sont différentes entre les deux mots
        return distance
    else:
        # Affichage de ce message si la longueur des deux mots est différente
        print("Attention, les mots doivent être de meme longueur")

# Resultat qui fera appel à la fonction distance_hamming
resultat=distance_hamming('Japon','Savon')

# Affichage du resultat
print("La distance de Hamming entre les deux mots est :",resultat)