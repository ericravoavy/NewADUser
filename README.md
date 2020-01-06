# Outil d'automatisation de création d'utilisateurs dans l'Active Directory

## Benefices du code :

- Avoir une interface graphique pour la saisie d'informations Utilisateur
- Creation de plusieurs utilisateurs en une fois par saisie des informations de ces utilisateurs
- Creation d'utilisateur à partir d'un fichier csv
- Lecture des fiches utilisateurs en attente à partir d'un csv ou des saisies effectuées

## Requirements :

### Environnement WINDOWS

2 Programmes à utiliser
- AddUserGUI (Interface graphique de la saisie des informations Utilisateur) :
nécéssite l'installation de Python 3

- AddUserAD (Programme de création des utilisateurs dans l'AD)
Nécessite l'utilisation de Powershell en mode unrestricted

## Fonctionnement :

### Ajouter des utilisateurs par saisie :

- Saisir les informations des utilisateurs dans les champs correspondants
- Cliquer sur le bouton "Ajouter" et saisir le deuxième utilisateur
- Lorsque tous les utilisateurs sont saisies - Cliquer sur le bouton "lire" pour voir les utilisateurs saisies
- Vérifier les informations
- Afin de les ajouter dans l'AD ==> cliquer sur le bouton Envoyer pour ajouter ces utilisateurs dans l'AD
- Le resultat (Réussite ou Ajout) de l'ajout des utilisateurs dans l'AD s'affichera sur la fenêtre de droite 

### Ajouter des utilisateurs à partir d'un fichier csv

- Cliquer sur le bouton "joindre un fichier"
- Rechercher un fichier csv
- Les informations du fichier csv seront affichés sur la fenêtre de droite
- Cliquer sur le bouton "Envoyer" pour les ajouter dans l'AD
- Le resultat (réussite ou échec) de l'ajout des utilisateurs s'affichera sur la fenêtre de droite



