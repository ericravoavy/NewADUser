# Outils d'automatisation de création d'utilisateurs dans l'Active Directory

Benefices du code :

- Avoir une interface graphique pour la saisie d'information Utilisateur
- Creation de plusieurs utilisateurs en une fois par saisie des informations de ces utilisateurs
- Creation d'utilisateur à partir d'un fichier csv
- Lecture des fiches utilisateurs en attente à partir d'un csv ou des saisies effectuées

Requirements :

Environnement WINDOWS

2 Programmes à utiliser
- AddUserGUI (Interface graphique de la saisie des information Utilisateur) :
nécéssite l'installation de Python 3

- AddUserAD (Programme de création des utilisateurs dans l'AD)
Nécessite l'utilisation de Powershell en mode unrestricted

Fonctionnement :

Ajouter des utilisateurs par saisie :

1 - Saisir les informations des utilisateurs dans les champs correspondants
2 - Cliquer sur le bouton "Ajouter" et saisir le deuxième utilisateur
3 - Lorsque tous les utilisateurs sont saisies - Cliquer sur le bouton "lire" pour voir les utilisateurs saisies
4 - Vérifier les informations
5 - Afin de les ajouter dans l'AD ==> cliquer sur le bouton Envoyer pour ajouter ces utilisateurs dans l'AD
6 - Le resultat (Réussite ou Ajout) de l'ajout des utilisateurs dans l'AD s'affichera sur la fenêtre de droite 

Ajouter des utilisateurs à partir d'un fichier csv

1 - Cliquer sur le bouton "joindre un fichier"
2 - Rechercher un fichier csv
3 - Les informations du fichier csv sera afficher sur la fenêtre de droite
4 - Cliquer sur le bouton "Envoyer" pour les ajouter dans l'AD
5 - Le resultat (réussite ou échec) de l'ajout des utilisateurs s'affichera sur la fenêtre de droite



