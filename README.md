Le dépôt contient 3 fichiers : 
- le script du jeu
- un fichier "liste_mots.txt" avec des mots personnalisés
- un fichier "mots_pendus.txt" avec les mots proposés sur Moodle
- Ce fichier README.MD

*** UTILISATION DU CODE ***
Lors de la compilation, la première chose à faire est de choisir le fichier de mots. D'abord, le code vous demande d'entrer le nom du fichier (exemple : liste_mots.txt) puis de copier coller le chemin de ce fichier.
Le choix par défaut est accessible uniquement si vous modifiez le chemin en dur dans le code (car il est en local). Il est donc préférable d'utiliser la première option. 

Le jeu commence directement après la sélection. Plusieurs tirets "_" sont affichés selon la longueur du mot à trouver, et à chaque tentative de lettre, plusieurs variables peuvent être mises à jour :
- Le mot mystère remplit de "_" est mis à jour si la tentative est réussie, et la lettre utilisée est affichée dans une liste qui stocke les essais à chaque boucle;
- Si la tentative est ratée, vous perdez une vie, l'état actuel du mot mystère est affiché et la lettre utilisée est aussi stockée dans la liste;
- Même si uniquement la liste de lettres utilisées est affichée, il y a aussi une liste de lettres trouvées afin de vérifier si la nouvelle tentative n'avait pas déjà été trouvée.

Si le joueur arrive à trouver toutes les lettres, il remporte la partie et on lui propose de rejouer (avec nouvelle sélection de fichier) ou de quitter.
Si le joueur arrive à 1 vie, on lui propose un indice (lettre aléatoire non présente dans le mot)parmis les lettres de l'alphabet NON PRÉSENTES dans les lettres du mot et 
NON PRÉSENTES dans les lettres déjà utilisées.
Si le joueur arrive à 0 vie, il perd la partie et on lui propose de rejouer (avec nouvelle sélection de fichier) ou de quitter.

*** CONTENU DU CODE *** 
Le script contient plusieurs fonctions :
- recup_fichier : renvoit le chemin du fichier de mots
- equivalent_accent : renvoi le mot aléatoire sans accent
- choix_mot : renvoi un mot choisi aléatoirement dans le fichier
  Et procédures :
- jeu : contient le code qui fait tourner la partie et qui permet de relancer ou de quitter
- premiere_partie : contient les fonctions pour lancer la première partie

