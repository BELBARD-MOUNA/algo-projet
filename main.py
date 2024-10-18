# Initialisation des compteurs
longueur_phrase = 0
nombre_mots = 0
nombre_voyelles = 0

# Définir les voyelles
voyelles = "aeiouAEIOU"

# Lecture de la phrase caractère par caractère
phrase = input("Entrez une phrase se terminant par un point: ")

# Boucle pour parcourir chaque caractère de la phrase
mot_en_cours = False  # Indicateur pour détecter un mot

for char in phrase:
    # Si le caractère est un point, on arrête la boucle
    if char == '.':
        longueur_phrase += 1
        if mot_en_cours:  # Pour compter le dernier mot avant le point
            nombre_mots += 1
        break

    # Incrémenter la longueur totale
    longueur_phrase += 1

    # Vérifier si le caractère est une voyelle
    if char in voyelles:
        nombre_voyelles += 1

    # Vérifier les espaces pour compter les mots
    if char == ' ':
        if mot_en_cours:  # Si un mot est terminé
            nombre_mots += 1
            mot_en_cours = False
    else:
        mot_en_cours = True

# Affichage des résultats
print("Longueur de la phrase (y compris le point):", longueur_phrase)
print("Nombre de mots:", nombre_mots)
print("Nombre de voyelles:", nombre_voyelles)
