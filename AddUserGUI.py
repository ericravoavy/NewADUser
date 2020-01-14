import tkinter as tk
import os
from tkinter import filedialog
import csv


class Interface(tk.Tk):
    def __init__(self):
        """La class Fenetre permet de créer une interface graphique des saisie des informations.

         ses attributs sont composés de champs suivants :
        - Nom :
        - Prénom :
         - Fonction :
        - Email Adresse :
        - Password
        - Telephone number
        - Mobile Number
        - Member of :

        """
        super().__init__()  # Initialisation de la fenêtre racine
        self.val_label = ""
        self.val_entry = ""
        self.title('Creation Compte AD')
        self.cmd = 'powershell -file '  # definition de la commande à executer dans l'OS
        self.ps_file = 'AddUserAD.ps1 '  # fichier du script powershell
        self.csvfile = 'import.csv'  # fichier csv à mettre en paramêtre du script powershell
        self.writer = ""  # Constructeur de l'ecriture du fichier csv
        self.param = '-ExecutionPolicy Unrestricted'  # Force l'execution du script Powershell
        self.argument = ''  # Constructeur de l'argument pour le script powershell
        self.current_dir = os.getcwd()  # connnaitre le repertoire actuel
        self.command = self.cmd + self.ps_file + self.argument + self.param
        self.row = 0  # Constructeur du variable pour parcourir le fichier csv
        self.csv_read = ''  # Constructor du variable lecture csv
        self.csv_header = ''  # Constructeur pour l'ecriture en tête fichier csv
        self.csv_writer = ''  # Constructeur pour l'ecriture de fichier
        self.read = ''
        self.read_label = tk.Label(self, text='')
        self.position = ""
        self.val_command = ""
        self.val_button = ""

        # newuser - Instantiation de la classe Utilisateur
        self.newuser = Utilisateur()

        # methode pour ecrire l'entête du fichier csv
        self.csv_init()

        # ------Definition du formulaire-------- #
        # définition des widgets Label et champs de saisie avec positionnement
        self.form2("lastname", "lastname_entry", "Nom", '0')

        self.form2("givenname", "givenname_entry", "Prénom", '1')

        self.form2("telnum", "telnum_entry", "Téléphone", '2')

        self.form2("mobilephone", "mobilephone_entry", "Mobile", '3')

        self.form2("email", "email_entry", "email", '4')

        """self.form("lastname", "Nom", '0')

        self.form("givenname", "Prénom", '1')

        self.form("telnum", "Téléphone", '2')

        self.form("mobilephone", "Mobile", '3')

        self.form("email", "email", '4')
        """
        # ------------------- Button section--------------------------- #
        self.button("btn_create", "Créer les comptes", self.envoyer, 1)

        self.button("btn_join", "Joindre un fichier", self.joinfile, 2)

        self.button("btn_add", "ajouter utilisateur", self.ecrirefichier, 3)

        self.button("btn_read", "Afficher", self.lire, 4)

        """self.btn_send = tk.Button(self, text='Créer les comptes', pady='2',
                                  command=self.envoyer)  # Définition du bouton afficher
        # qui va avoir comme fonction d'afficher ceux qui ont été saisies en appélant la methode modify
        self.btn_send.grid(column=1, row=11, sticky='sw', pady=20)

        self.btn_join = tk.Button(self, text='joindre fichier csv', pady='2', command=self.joinfile)
        self.btn_join.grid(column=2, row=11, sticky='sw', pady=20)

        # Définition du bouton afficher :
        self.btn_add = tk.Button(self, text='Ajouter utilisateur', pady='2', command=self.ecrirefichier)
        # qui va avoir comme fonction d'ajouter ceux qui ont été saisies en appélant la methode modify
        self.btn_add.grid(column=3, row=11, sticky='sw', pady=20)

        self.btn_read = tk.Button(self, text='Afficher', pady='2', command=self.lire)
        self.btn_read.grid(column=4, row=11, sticky='sw', pady=20, padx=10)"""

        self.lire()

    def form2(self, label, entry, text, position):
        """Methode pour créer le formulaire de saisie"""
        self.val_label = label + "label"
        self.val_entry = entry
        # self.position = str(position)

        self.val_label = tk.Label(self, text=text)
        self.val_label.grid(column=0, sticky='w', row=position)

        self.val_entry = tk.StringVar()
        self.val_entry = tk.Entry(self, textvariable=self.val_entry)
        self.val_entry.grid(column=1, row=position, columnspan=2, pady=position)

    """def form(self, label, text, position):
        Methode pour créer le formulaire de saisie
        self.val_label = label + "label"
        self.val_entry = label
        # self.position = str(position)

        self.val_label = tk.Label(self, text=text)
        self.val_label.grid(column=0, sticky='w', row=position)

        self.val_entry = tk.StringVar()
        self.val_entry = tk.Entry(self, textvariable=self.val_entry)
        self.val_entry.grid(column=1, row=position, columnspan=2, pady=position)"""

    def button(self, button, text, function, position):
        # self.val_command = "self." + function
        self.val_button = button

        self.val_button = tk.Button(self, text=text, pady='2', command=function)
        self.val_button.grid(column=position, row='11', sticky='sw', pady=20)


    def csv_init(self):
        """ Methode pour initialiser le fichier csv avec les entête de colonne """
        self.csv_header = ''
        with open(self.csvfile, 'w', newline='') as csvfile:
            self.csv_header = ['firstname', 'lastname', 'login', 'job_title', 'samaccountname',
                               'tel_number', 'mobile_number', 'departement', 'email']
            self.csv_writer = csv.writer(csvfile, delimiter=';')
            self.csv_writer.writerow(self.csv_header)

    def csvreset(self):
        """ permet de réinitialise la variable csvfile qui sera le fichier csv par défaut """
        self.csvfile = 'import.csv'

    def ecrirefichier(self):
        """ Cette methode permet d'ajouter les utilisateurs saisient dans le formulaire dans un fichier
        csv import.csv
        """
        print("nous sommes dans le repertoire pour ecrire dans le fichier", os.getcwd())
        with open(self.csvfile, 'a') as userdatas:
            self.newuser.set_nom(self.
            self.newuser.set_prenom(self.givenname.get())
            self.newuser.set_tel_number(self.val_entry.get())
            self.newuser.set_mobile_number(self.val_entry.get())
            self.newuser.set_email_address(self.val_entry.get())
            self.newuser.set_email_address(self.val_entry.get())
            userdatas.write(
                self.newuser.prenom + ";" + self.newuser.nom + ";" +
                self.newuser.prenom + '.' + self.newuser.nom + ";" + 'VP' + ";" + self.newuser.prenom + '.' +
                self.newuser.nom + ";" + self.newuser.tel_number + ";"
                + self.newuser.mobile_number + ";" + "IT" + ";" + self.newuser.email_address + '\n')
            self.val_entry.delete(0, tk.END)
            self.val_entry.delete(0, tk.END)
            self.val_entry.delete(0, tk.END)
            self.val_entry.delete(0, tk.END)
            self.val_entry.delete(0, tk.END)
            self.row = 0
            Interface.update(self)

    def joinfile(self):
        """ Cette methode permet de recupérer les informations user
         à partir d'un fichier csv et d'ajouter les dans l'AD """
        self.argument = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
        self.csvfile = self.argument
        self.lire()

    def lire(self):
        """ Cette methode permet d'afficher les utilisateurs en file d'attente à partir d'un fichier csv """
        self.read_label.destroy()
        print("nous sommes dans le repertoire", os.getcwd(), "pour lire le contenu du fichier", self.csvfile)
        with open(self.csvfile, newline='') as csv_file:
            print(csv_file)
            self.csv_read = csv.reader(csv_file)
            for row in self.csv_read:
                self.read_label = tk.Label(self, text=row)
                self.read_label.grid(column=5, row=self.row, sticky='w')
                self.row += 1

    def envoyer(self):
        """ Cette fonction permet d'exécuter la fonction de creation user
         à partir du fichier csv """

        os.chdir(self.current_dir)
        self.argument = self.csvfile
        self.command = self.cmd + self.ps_file + self.argument
        type_execute = os.popen(self.command)
        type_output = type_execute.read()
        self.row = 0
        print("resultat de la creation : \n")
        self.read_label = tk.Label(self, text=type_output)
        self.read_label.grid(column=5, row=self.row, sticky='w')


class Utilisateur:
    """Classe utilisateur qui aura en paramètre d'entrée deux variables name et firstname :

    - attribut nom
    - attribut firstname
    """

    # Définition de la classe
    def __init__(self):
        self.nom = ""  # attributs name
        self.prenom = ""  # attributs prenom
        self.login = ""
        self.fonction = ""
        self.tel_number = ""
        self.mobile_number = ""
        self.password = "Welcome.2020"
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

    def set_mobile_number(self, mobile_number):
        self.mobile_number = mobile_number

    def set_email_address(self, email_address):
        self.email_address = email_address


if __name__ == "__main__":
    window = Interface()
    window.mainloop()
