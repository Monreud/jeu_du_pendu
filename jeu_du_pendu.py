import unicodedata
from unicodedata import normalize
from random import choice
import os


# Fonction de récupération du fichier de mots
def recup_fichier():
    # Récupération du nom du fichier et du nom du dossier en récursif (tant que le nom n'est pas correct)
    nom_fichier = str(input('Quel est le nom du fichier contenant les mots ? '))
    nom_dossier = str(input('Entrez le chemin complet du dossier dans lequel se trouve le fichier : '))

    # Vérification de l'existence du fichier et s'il s'agit bien d'un fichier .txt
    if (not os.path.isfile(os.path.join(nom_dossier,nom_fichier))
            or not os.path.exists(os.path.join(nom_dossier,nom_fichier))
            or str(os.path.join(nom_dossier,nom_fichier))[-4:] != '.txt'):
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
        print('Fichier trouvé, son chemin est : ' + str(os.path.join(nom_dossier,nom_fichier)))
        chemin_fichier = str(os.path.join(nom_dossier,nom_fichier))
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


def choix_mot(chemin_fichier):
    with open(chemin_fichier, 'r') as fio:
        mots = fio.read().splitlines()
    mot = choice(mots)
    vrai_mot = equivalent_accent(mot)
    return vrai_mot


def jeu(mot_para):
    mot = equivalent_accent(mot_para)
    #   print(mot)

    chances = 6
    print('Mot à trouver : ' + len(mot) * '_')

    lettres_mot = len(mot) * ['_']
    lettres_trouvees = len(mot) * []
    lettres_utilisees = []
    cpt = 0

    while chances > 0:
        essai = str(input('Quelle lettre pensez-vous faire partie du mot ?'))
        if essai in mot and essai not in lettres_trouvees:
            for i in range(len(mot)):
                if essai == mot[i]:
                    cpt += 1
                    del lettres_mot[i]
                    lettres_mot.insert(i, essai)
            lettres_trouvees.append(essai)
            lettres_utilisees.append(essai)
            print('Bravo ! Voici le mot désormais : ' + ''.join(lettres_mot) + ' et les lettres utilisées '
                                                                               'pour l instant sont ' + str(lettres_utilisees))
            if cpt == len(mot):
                choix = 0
                while choix != 1 or choix != 2:
                    choix = int(input('Vous avez gagné ! Voulez-vous refaire une partie ? 1 pour oui et 2 pour non'))
                    if choix == 1:
                        fichier = recup_fichier()
                        mot = choix_mot(fichier)
                        jeu(mot)
                    elif choix == 2:
                        print('Merci d avoir joué ! A bientôt ! ')
                        return 0
        elif essai in mot and essai in lettres_trouvees:
            print('Vous avez déjà trouvé cette lettre, tentez autre chose ! ')
        else:
            chances -= 1
            lettres_utilisees.append(essai)
            print('Oh non ! Mauvaise pioche ! Plus que ' + str(chances) + ' vies ! ')
            print('Les lettres utilisees pour l instant sont : ' + str(lettres_utilisees))
            if chances == 1:
                print('Vous semblez en difficulté... Voici un indice : ')
    choix = 0
    while choix != 1 or choix != 2:
        choix = int(input('Vous avez perdu ! Voulez-vous refaire une partie ? 1 pour oui et 2 pour non'))
        if choix == 1:
            fichier = recup_fichier()
            mot = choix_mot(fichier)
            jeu(mot)
        elif choix == 2:
            print('Merci d avoir joué ! A bientôt ! ')
            return 0


def premiere_partie():
    fichier = recup_fichier()
    mot = choix_mot(fichier)
    jeu(mot)


premiere_partie()



