"""
Jeu du pendu en python comprenant plusieurs fonctions :
- Récupération du nom du fichier
- Sélection aléatoire d'un mot et mise en équivalent sans accent
- Jeu du pendu avec plusieurs vies, stockage des lettres utilisées, stockage des lettres trouvées,
indice à la dernière chance, état du mot mystère à chaque boucle et proposition de rejouer à la fin d'une partie.
"""

from random import choice
import os


# Fonction de récupération du fichier de mots
def recup_fichier():
    # Récupération du nom du fichier et du nom du dossier en récursif (tant que le nom n'est pas correct)
    nom_fichier = str(input('Quel est le nom du fichier contenant les mots ? '))
    nom_dossier = str(input('Entrez le chemin complet du dossier dans lequel se trouve le fichier : '))

    # Vérification de l'existence du fichier et s'il s'agit bien d'un fichier .txt
    if (not os.path.isfile(os.path.join(nom_dossier, nom_fichier))
            or not os.path.exists(os.path.join(nom_dossier, nom_fichier))
            or str(os.path.join(nom_dossier, nom_fichier))[-4:] != '.txt'):
        choix_fichier = int(input('Fichier introuvable ou n est pas un fichier .txt, souhaitez-vous 1 : Réessayer '
                                  'ou 2 : Choisir le fichier de mots par défaut ? Répondez par 1 ou 2 : '))
        if choix_fichier == 1:
            recup_fichier()  # Tant que le fichier n'est pas trouvé, on réessaye
        elif choix_fichier == 2:
            chemin_fichier = 'C:/Users/augus/PycharmProjects/jeu_du_pendu/mots_pendu.txt'
            print('Vous avez choisi le fichier de mots par défaut, son chemin est : ', chemin_fichier)
            return chemin_fichier
        else:
            print('Entrée erronée, retour à la sélection de fichier.')
            recup_fichier()
    # Lorsque le fichier est trouvé, son chemin est retourné
    else:
        print('Fichier trouvé, son chemin est : ' + str(os.path.join(nom_dossier, nom_fichier)))
        chemin_fichier = str(os.path.join(nom_dossier, nom_fichier))
        return chemin_fichier


# Fonction de remplacement d'accents par sans accent
def equivalent_accent(mot):
    # Définition des listes avec et sans accent
    liste_accents = ['à', 'â', 'é', 'è', 'ë', 'ê', 'ù', 'û', 'ï', 'î', 'ô', 'ö', 'ç']
    liste_lettres = ['a', 'a', 'e', 'e', 'e', 'e', 'u', 'u', 'i', 'i', 'o', 'o', 'c']
    # Création du nouveau mot sans accent (même si le mot original n'en contient pas)
    nouveau_mot = ''
    # Parcours du mot
    for i in range(len(mot)):
        # Si un accent est trouvé alors on le remplace par l'indice correspondant dans la liste sans accent
        if mot[i] in liste_accents:
            nouveau_mot += liste_lettres[liste_accents.index(mot[i])]
        else:   # Sinon, on garde le caractère du mot
            nouveau_mot += mot[i]
    return nouveau_mot


# Fonction de choix d'un mot aléatoire
def choix_mot(chemin_fichier):
    with open(chemin_fichier, 'r') as fio:
        mots = fio.read().splitlines()
    mot = choice(mots)
    vrai_mot = equivalent_accent(mot)
    return vrai_mot


# Procédure principale du jeu
def jeu(mot_para):
    mot = equivalent_accent(mot_para)  # Transformée du mot potentiellement avec accent en sans accent
    #   print(mot) # Retirer le commentaire pour pouvoir vérifier le mot en début de partie

    chances = 6  # Déclaration des chances initiales
    print('Mot à trouver : ' + len(mot) * '_')  # Annonce du nombre de lettres à trouver

    # Déclaration des variables du mot en cours, des lettres trouvées et des lettres utilisées
    lettres_mot = len(mot) * ['_']
    lettres_trouvees = len(mot) * []
    lettres_utilisees = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # Utilisé pour l'indice à 1 chance
    cpt = 0  # Déclaration du compteur de bonne réponse

    while chances > 0:  # On boucle tant que le joueur a une chance
        essai = str(input('Quelle lettre pensez-vous faire partie du mot ?'))
        # Lors d'une tentative, on vérifie que la lettre soit présente dans le mot
        # mais pas dans les lettres trouvées ni dans les lettres utilisées (nouvelle bonne lettre)
        if essai in mot and essai not in lettres_trouvees and essai not in lettres_utilisees:
            for i in range(len(mot)):  # On cherche alors dans tous les caractères du mot les cohérences
                if essai == mot[i]:
                    cpt += 1  # A chaque occurence, le joueur obtient une bonne réponse
                    del lettres_mot[i]
                    lettres_mot.insert(i, essai)  # On remplace alors le tiret par la lettre trouvée
            lettres_trouvees.append(essai)
            lettres_utilisees.append(essai)  # On ajoute la lettre trouvée et utilisée dans les listes

            print('Bravo ! Voici le mot désormais : '  # Mise à jour du mot
                  + ''.join(lettres_mot) + ' et les lettres utilisées pour l instant sont ' + str(lettres_utilisees))
            if cpt == len(mot):  # Lors de la réussite, on vérifie si le joueur a trouvé toutes les lettres
                choix = 0
                while choix != 1 or choix != 2:  # Choix de relancer une partie
                    choix = int(input('Vous avez gagné ! Voulez-vous refaire une partie ? 1 pour oui et 2 pour non'))
                    if choix == 1:
                        fichier = recup_fichier()
                        mot = choix_mot(fichier)
                        jeu(mot)
                    elif choix == 2:
                        print('Merci d avoir joué ! A bientôt ! ')
                        return 0

        # Si la lettre est dans le mot mais est aussi déjà dans les lettres trouvées alors il peut réessayer
        # et les lettres utilisées sont affichées
        elif essai in mot and essai in lettres_trouvees:
            print('Vous avez déjà trouvé cette lettre, tentez autre chose ! ' + ''.join(lettres_mot))
            print('Les lettres utilisees pour l instant sont : ' + str(lettres_utilisees))

        # Si la lettre est dans le mot mais est aussi déjà dans les lettres déjà utilisées alors il peut réessayer
        # et les lettres utilisées sont affichées
        elif essai in mot and essai in lettres_utilisees:
            print('Vous avez déjà utilisé cette lettre, tentez autre chose ! ' + ''.join(lettres_mot))
            print('Les lettres utilisees pour l instant sont : ' + str(lettres_utilisees))

        # Si la lettre n'est pas dans le mot mais déjà dans les lettres utilisées alors il peut réessayer
        # et les lettres utilisées sont affichées
        elif essai not in mot and essai in lettres_utilisees:
            print('Vous avez déjà utilisé cette lettre, tentez autre chose ! ' + ''.join(lettres_mot))
            print('Les lettres utilisees pour l instant sont : ' + str(lettres_utilisees))

        # Sinon, le joueur perd une vie
        else:
            chances -= 1
            lettres_utilisees.append(essai)  # La lettre est ajoutée à la liste des lettres utilisées
            # et elles sont affichées
            print('Oh non ! Mauvaise pioche ! Plus que ' + str(chances) + ' vies ! ' + ''.join(lettres_mot))
            print('Les lettres utilisees pour l instant sont : ' + str(lettres_utilisees))

            # Quand le joueur arrive à une chance, il a droit à un indice sur une lettre qui n'est pas dans le mot
            if chances == 1:
                lettres_mot_entier = set(mot)  # On fais un ensemble de lettres du mot à trouver
                # On prend les lettres de l'alphabet SAUF les lettres présentes dans le mot à trouver
                lettres_restantes_alphabet = [lettre for lettre in alphabet if lettre not in lettres_mot_entier]
                # On choisit au hasard une lettre de cet ensemble et on lui affiche
                lettre_random_indice = choice(lettres_restantes_alphabet)
                print('Vous semblez en difficulté... Voici un indice : il n y a pas de ' + lettre_random_indice)
    choix = 0  # Lorsque le joueur n'a plus de chance, on lui propose de rejouer ou de quitter
    while choix != 1 or choix != 2:
        choix = int(input('Vous avez perdu ! Le mot était : ' + mot +
                          '\n Voulez-vous refaire une partie ? 1 pour oui et 2 pour non'))
        if choix == 1:
            fichier = recup_fichier()
            mot = choix_mot(fichier)
            jeu(mot)
        elif choix == 2:
            print('Merci d avoir joué ! A bientôt ! ')
            return 0


# Procédure de lancement de la première partie
def premiere_partie():
    fichier = recup_fichier()
    mot = choix_mot(fichier)
    jeu(mot)


# Appel de la procédure de jeu
premiere_partie()
