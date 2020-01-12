# Outil d'automatisation de création d'utilisateurs dans l'Active Directory
### Pourquoi ce programme
La croissance de nouveaux arrivants et la création de plusieurs comptes manuellement dans l'Active Directory génèrent parfois des erreurs et  surtout consomment beaucoup de temps à cause de la répétition des tâches.
Nous avons donc eu l'idée de créer un petit programme, avec une interface graphique, de :
- rentrer les informations des utilisateurs
- d'enregistrer ces informations dans un fichier csv
- d'importer des fichiers csv de listes d'utilisateurs
- de créer les comptes Utilisateurs à partir des informations provénants des fichiers csv

## Benefices du code :

- Avoir une interface graphique pour la saisie d'informations Utilisateur
- Creation de plusieurs utilisateurs en une fois par saisie des informations de compte
- Creation de compte dans l'Active Directory à partir d'un fichier csv
- Lecture des fiches utilisateurs du fichier csv ou des saisies effectuées

## Requirements :

### Environnement WINDOWS

Restriction du programme à l'environnement WINDOWS dans un premier temps :

#### Serveur :

- Windows Server 2012 R2 ou plus récent
- Domain Controleur + Active Directory

#### Workstation WINDOWS 10 :

- RSAT: Active Directory Domain Services and Lightweight Directory Tools ==> "installé"
- Mode d'exécution du script "unrestricted" : Set-ExecutionPolicy -Scope "CurrentUser" -ExecutionPolicy "Unrestricted"

Fichiers :

- AddUserGUI.zip qui contient les fichiers nécéssaires à la bonne exécution du programme.

Les deux fichiers suivant doivent être dans un même dossier pour fonctionner :
- AddUserGUI.exe
- AddUserAD.ps1

## Fonctionnement :

- Télécharger le fichier ZIP AddUserGUI.zip
- Décompresser le fichier
- localiser le fichier AddUserGUI.exe

Exécuter le fichier AddUSerGUI.exe inclut dans le dossier

### Ajouter des utilisateurs par saisie :
La fenêtre interface graphique s'ouvre avec les informations à saisir :

- Saisir les informations des utilisateurs dans les champs correspondants aux champs
- Cliquer sur le bouton "Ajouter utilisateur" pour ajouter l'utilisateur dans une file d'attente
- Lorsque tous les utilisateurs sont saisies - Cliquer sur le bouton "Afficher" pour voir les utilisateurs dans la file d'attente
- Vérifier les informations saisies
- Afin de lancer l'ajout des comptes qui sont en file d'attente dans l'AD ==> cliquer sur le bouton "Créer les comptes" pour ajouter ces utilisateurs dans l'AD
- Le resultat (Réussite ou Echec) de l'ajout des utilisateurs dans l'AD s'affichera sur la fenêtre de droite

### Ajouter des utilisateurs à partir d'un fichier csv
Le programme permet aussi de rajouter plusieurs utilsateurs en mode "bulk" en une fois à partir d'un fichier csv 

- Cliquer sur le bouton "joindre un fichier"
- Rechercher un fichier csv avec la structure de modele csv présent dans le dossier 
- Les informations du fichier csv seront affichés sur la fenêtre de droite
- Cliquer sur le bouton "Créer les comptes" pour les ajouter dans l'AD
- Le resultat (réussite ou échec) de l'ajout des utilisateurs s'affichera sur la fenêtre de droite



