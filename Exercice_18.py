# Intitulé : Exercice 18 - Le Crime
# Auteur : FIOT Clément
# Formation : M2i - L3
# Date butoir : 13/11/2019

# Initialisation de la Fonction Position
def Position(code,sequence):

# Bloc qui permet de définir la position du code dans la sequence lorsqu'il concorde avec celle-ci
    for i in range(len(sequence)-len(code)):
        # Si la chaîne code est identique a une partie de la chaine sequence (caractère de départ + nombre de caractères correspondant au code)
        if code == sequence[i:i+len(code)]:
            # On retourne la valeur de i --> Position dans la chaîne
            return i
    # Sinon on retourne que le code n'est pas présent dans la chaîne séquence et que donc la personne ne peut pas être coupable
    return print("Un des deux codes ne correspond pas ! Cette personne ne peut pas être coupable !")


# Initialisation de la Fonction Enquete
def Enquete():

    # Declaration des variables
    moutarde =  "CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGC"
    rose =      "CTCCTGATGCTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGG"
    pervenche = "AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGTACTCCGCGCGCCGGGACAGAATGCC"
    leblanc =   "CTGCAGGAACTTCTTCTGGAAGTACTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG"

    code1 = "CATA"
    code2 = "ATGC"

    # Bloc qui permet de lire chaque séquence grace au "for -- in" et de faire appel à la fonction Position qui va -
    # -déterminer la concordance entre les codes et les séquences et définir la position de départ ou les caractères concordent
    for personnage in [moutarde,rose,pervenche,leblanc]:
        print("Code1 :",code1,"| Sequence du suspect :",personnage,"| Position du code :",Position(code1,personnage))
        print("Code2 :",code2,"| Sequence du suspect :",personnage,"| Position du code :",Position(code2,personnage),"\n")
    return

# Appel de la fonction Enquete
Enquete()

# Affichage d'un message afin de déterminer le suspect
print("****Si les deux codes sont présents dans la sequence du suspect, alors il est le criminel !****")