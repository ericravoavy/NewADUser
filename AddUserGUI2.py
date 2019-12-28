import tkinter as tk
import os


class Fenetre(tk.Tk):
    def __init__(self):
        """La class Fenetre permet de créer une interface graphique des saisie des informations.
         ses attributs sont composés de champs suivants :

        - Nom : champs de saisie
        - Prénom : champs de saisie
        """
        super().__init__()  # Initialisation de la fenêtre racine

        self.cmd = 'powershell -file '  # definition de la commande à executer dans l'OS
        self.file = 'AddUserAD.ps1 '  # valeur du fichier que va recevoir la commande
        self.param = '-ExecutionPolicy Unrestricted'
        self.argument = ''
        self.ch_dir = "C:/P6-OC-Project/NewADUser"
        self.commande = self.cmd + self.file + self.argument + self.param

        # newuser - Instantiation de la classe Utilisateur
        self.newuser = Utilisateur()

        # ------Definition du champs "Nom"-------- #
        # définition du widget Label avec affichage "nom" et le positionnement
        self.lastnamelabel = tk.Label(self, text='Nom')
        self.lastnamelabel.grid(column=0, row=0, sticky='w')

        # Definition du champs de saisie "Nom"
        self.lastnamefield = tk.StringVar()  # Définir le type de ce variable comme étant une chaîne de caractère
        self.lastname = tk.Entry(self, textvariable=self.lastnamefield)  # Définition du champs de saisie
        self.lastname.grid(column=1, row=0, sticky='e', columnspan=2, padx=10)  # Mise en place du champs de saisie

        # Prénom
        self.givennamelabel = tk.Label(self, text="Prénom")  # Définition du widget Label avec comme affichage "prénom"
        self.givennamelabel.grid(column=0, row=1, sticky='w', pady='2')  # Positionnement du widget dans la fenêtre

        self.givennamefield = tk.StringVar()  # Définir le type de ce variable comme étant une chaîne de caractère
        self.givenname = tk.Entry(self, textvariable=self.givennamefield)  # Définition du champs de saisie du "prénom"
        self.givenname.grid(column=1, row=1, columnspan=2)  # Positionnement du widget dans la fenêtre racine

        # Login
        self.loginlabel = tk.Label(self, text="login")  # Définition du widget Label avec comme affichage "prénom"
        self.loginlabel.grid(column=0, row=2, sticky='w', pady='2')  # Positionnement du widget dans la fenêtre

        self.loginfield = tk.StringVar()  # Définir le type de ce variable comme étant une chaîne de caractère
        self.loginname = tk.Entry(self, textvariable=self.loginfield)  # Définition du champs de saisie du "prénom"
        self.loginname.grid(column=1, row=2, columnspan=2)  # Positionnement du widget dans la fenêtre racine

        # Tel number
        self.telnumlabel = tk.Label(self, text="Téléphone")  # Définition du widget Label avec comme affichage "prénom"
        self.telnumlabel.grid(column=0, row=3, sticky='w', pady='2')  # Positionnement du widget dans la fenêtre

        self.telnumfield = tk.IntVar()  # Définir le type de ce variable comme étant une chaîne de caractère
        self.telnum = tk.Entry(self, textvariable=self.telnumfield)  # Définition du champs de saisie du "prénom"
        self.telnum.grid(column=1, row=3, columnspan=2)  # Positionnement du widget dans la fenêtre racine#Prénom

        # mail address
        self.email_label = tk.Label(self, text="Email")  # Définition du widget Label avec comme affichage "prénom"
        self.email_label.grid(column=0, row=4, sticky='w', pady='2')  # Positionnement du widget dans la fenêtre

        self.email_field = tk.StringVar()  # Définir le type de ce variable comme étant une chaîne de caractère
        self.email = tk.Entry(self, textvariable=self.email_field)  # Définition du champs de saisie du "prénom"
        self.email.grid(column=1, row=4, columnspan=2)  # Positionnement du widget dans la fenêtre racine

        self.btn = tk.Button(self, text='Envoyer', pady='2', command=self.envoyer)  # Définition du bouton afficher
        # qui va avoir comme fonction d'afficher ceux qui ont été saisies en appélant la methode modify
        self.btn.grid(column=1, row=11, sticky='sw', pady=20)

        # Définition du bouton afficher :
        # self.btn_ecrire = tk.Button(self, text='Ecrire', pady='2', command=self.ecrirefichier)
        # qui va avoir comme fonction d'afficher ceux qui ont été saisies en appélant la methode modify
        # self.btn_ecrire.grid(column=3, row=11, sticky='sw', pady=20)
        # self.btn_cmd = tk.Button(self, text='lire fichier', pady='2', command=self.lirefichier)
        # self.btn_cmd.grid(column=2, row=11, sticky='sw', pady=20)
        print("Class is defined")

    def ecrirefichier(self):
        print("nous sommes dans le repertoire pour ecrire dans le fichier", os.getcwd())
        with open(self.file, self.write) as fichier:
            nom = self.newuser.nom
            prenom = self.newuser.prenom
            fichier.write(nom)
            fichier.write("\n")
            fichier.write(prenom)

    def lirefichier(self):
        os.chdir(self.change_dir)
        self.commande = self.cmd
        type_execute = os.popen(self.commande)
        type_output = type_execute.read()
        print("le fichier contient : \n", type_output)

    def envoyer(self):
        """Cette fonction permet d'afficher les informations entré dans le formulaire"""
        os.chdir(self.ch_dir)
        self.newuser.set_nom(self.lastname.get())
        self.newuser.set_prenom(self.givenname.get())
        self.newuser.set_login(self.loginname.get())
        self.newuser.set_tel_number(self.telnum.get())
        self.newuser.set_email_address(self.email.get())
        self.argument = '-name ' + '"' + self.newuser.prenom + ' ' + self.newuser.nom + '" ' \
                        + '-given_name ' + '"' + self.newuser.prenom + '" ' \
                        + '-last_name ' + '"' + self.newuser.nom + '" ' \
                        + '-samaccountname ' + '"' + self.newuser.login + '" ' \
                        +'-login ' + '"' + self.newuser.login + "@silver-holdings.lan" +  '" ' \
                        + '-Tel_Number ' + '"' + self.newuser.tel_number +'" ' \
                        + '-mail_address ' + '"' + self.newuser.email_address + '" '
        print("nous sommes dans le repertoire pour ecrire dans le fichier", os.getcwd())
        self.commande = self.cmd + self.file + self.argument + self.param
        type_execute = os.popen(self.commande)
        type_output = type_execute.read()
        print("le fichier contient : \n", type_output)
        # print(self.newuser.nom, self.newuser.prenom)


class Utilisateur:
    """Classe utilisateur qui aura en paramètre d'entrée deux variables name et firstname :

    - attribut nom
    - attribut firstname
    """

    def __init__(self):
        self.nom = ""  # attributs name
        self.prenom = ""  # attributs prenom
        self.login = ""
        self.tel_number = ""
        self.email_address = ""

    def get_nom(self):
        print(self.nom)

    def get_prenom(self):
        print(self.prenom)

    def set_nom(self, nom):
        self.nom = nom

    def set_prenom(self, prenom):
        self.prenom = prenom

    def set_login(self, login):
        self.login = login

    def set_tel_number(self, tel_number):
        self.tel_number = tel_number

    def set_email_address(self, email_address):
        self.email_address = email_address
