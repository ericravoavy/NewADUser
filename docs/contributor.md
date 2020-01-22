# Contibution pour AdduserADGUI

Dans un premier temps merci d'avance pour votre temps afin de contribuer à l'amélioration de ce projet

Les instructions suivantes seront une ligne de conduite pour maintenir ce projet lisible et propre.

Si vous voulez contribuer à l'amélioration de ce document, vous pouvez adresser un pull Request si nécéssaire.

Sachant que c'est l'ecriture de mon premier code, je serai ouvert à toutes les propositions d'amélioration du projet de manière globale.

## Par ou commencer ?

Ce projet s'inclut dans le cadre de ma formation Administrateur Intrastructure Cloud. 

Dans le cadre de ce parcours, un des projets consiste à identifier une tâche complexe, manuelle et recurente afin de pouvoir l'automatiser.

Pour ma part, la tâche récurrente que j'ai identifié est l'ajout de plusieurs comptes dans l'Active Directory.

En effet, cette tâche s'effectue la plupart du temps à se connecter à l'Active Directory par le biais d'un remote desktop,
et créer les comptes un par un sur le serveur.

Ou effectuer pour chaque compte la commande Powershell de création de compte sur un poste de l'adminitrateur system afin de créer
les comptes un par un.

ce qui nécessite à chaque fois de réecrire le code pour chaque paramêtre utilisateur.

L'objectif de ce projet est donc d'avoir une interface graphique ecrite en python 3.x.x qui permet de saisir les informations des utilisateurs.

Puis de passer ces paramètres à un script powershell afin de créer le compte de l'utilisateur dans l'Active Directory.

## Pré-requis

- Nécessite Windows 10 1803 ou supérieur
- Nécessite l'installation de python 3.XXX ou supérieur
- Nécessite l'execution de script powershell sous windows 10 en mode "Unrestricted"
- Nécessite des droits domain Admin sur le poste administrateur
- Nécessite le module RSAT: Active Directory Domain Services and Lightweight Directory Tools

## Code de conduite pour le contribution :
Pour contribuer au projet voici une liste de bonnes pratiques qu'il seraient judicieux de respecter.

- faire un pull du projet
- Créer la branche "develop" à partir de "Master"
- créer une branche "feature-GUI" pour developper l'interface graphique en python
- créer une branche "feature-CreateUserAD" pour developper le script de création de compte dans l'AD
- Essayer d'utiliser des noms de fichier explicite

faire un merge des branches finalisées dans la branche "develop" afin de fusionner les fonctionnalités.

Faire une push request afin de proposer la developpement du programme

### L'interface graphique en python

le fichier AddUserGUI.py est le fichier python qui sera l'interface graphique des saisies et le contrôle des informations utilisateurs.

Ecriture du code :

- Respecter les bonnes pratiques PEP 8 que vous pouvez retrouver sur le site https://www.python.org/dev/peps/pep-0008/ 
- Effectuer des commentaires adéquates des codes

### Création de compte sur l'Active Directory

- Effectuer les commentaires adéquates des codes
- respecter les conventions de nommage des fonctions et classes

les variables : tous en miniscules. Le caractère "_" souligné peut-être utilisé pour la bonne lecture des variables.
