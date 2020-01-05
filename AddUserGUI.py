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

        # newuser - Instantiation de la classe Utilisateur
        self.newuser = Utilisateur()

        # methode pour ecrire l'entête du fichier csv
        self.csv_init()

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
        # self.loginlabel = tk.Label(self, text="login")  # Définition du widget Label avec comme affichage "prénom"
        # self.loginlabel.grid(column=0, row=2, sticky='w', pady='2')  # Positionnement du widget dans la fenêtre

        # self.loginfield = tk.StringVar()  # Définir le type de ce variable comme étant une chaîne de caractère
        # self.loginname = tk.Entry(self, textvariable=self.loginfield)  # Définition du champs de saisie du "prénom"
        # self.loginname.grid(column=1, row=2, columnspan=2)  # Positionnement du widget dans la fenêtre racine

        # Tel number
        self.telnumlabel = tk.Label(self, text="Téléphone")  # Définition du widget Label avec comme affichage "prénom"
        self.telnumlabel.grid(column=0, row=3, sticky='w', pady='2')  # Positionnement du widget dans la fenêtre

        self.telnumfield = tk.IntVar()  # Définir le type de ce variable comme étant une chaîne de caractère
        self.telnum = tk.Entry(self, textvariable=self.telnumfield)  # Définition du champs de saisie du "prénom"
        self.telnum.grid(column=1, row=3, columnspan=2)  # Positionnement du widget dans la fenêtre racine#Prénom
        self.telnum.delete(0, tk.END)

        # mobile
        self.mobilephone_label = tk.Label(self,
                                          text="Mobile")  # Définition du widget Label avec comme affichage "prénom"
        self.mobilephone_label.grid(column=0, row=4, sticky='w', pady='2')  # Positionnement du widget dans la fenêtre

        self.mobilephone_field = tk.IntVar()  # Définir le type de ce variable comme étant une chaîne de caractère
        self.mobile = tk.Entry(self, textvariable=self.mobilephone_field)  # Définition du champs de saisie du "prénom"
        self.mobile.grid(column=1, row=4, columnspan=2)  # Positionnement du widget dans la fenêtre racine
        self.mobile.delete(0, tk.END)
        # mail address
        self.email_label = tk.Label(self, text="Email")  # Définition du widget Label avec comme affichage "prénom"
        self.email_label.grid(column=0, row=5, sticky='w', pady='2')  # Positionnement du widget dans la fenêtre

        self.email_field = tk.StringVar()  # Définir le type de ce variable comme étant une chaîne de caractère
        self.email = tk.Entry(self, textvariable=self.email_field)  # Définition du champs de saisie du "prénom"
        self.email.grid(column=1, row=5, columnspan=2)  # Positionnement du widget dans la fenêtre racine

        # ------------------- Button section--------------------------- #
        self.btn_send = tk.Button(self, text='Envoyer', pady='2',
                                  command=self.envoyer)  # Définition du bouton afficher
        # qui va avoir comme fonction d'afficher ceux qui ont été saisies en appélant la methode modify
        self.btn_send.grid(column=1, row=11, sticky='sw', pady=20)

        self.btn_join = tk.Button(self, text='joindre fichier', pady='2', command=self.joinfile)
        self.btn_join.grid(column=2, row=11, sticky='sw', pady=20)

        # Définition du bouton afficher :
        self.btn_add = tk.Button(self, text='Ajouter', pady='2', command=self.ecrirefichier)
        # qui va avoir comme fonction d'ajouter ceux qui ont été saisies en appélant la methode modify
        self.btn_add.grid(column=3, row=11, sticky='sw', pady=20)

        self.btn_read = tk.Button(self, text='Lire', pady='2', command=self.lire)
        self.btn_read.grid(column=4, row=11, sticky='sw', pady=20, padx=10)
        print("Class is defined")

    def csvread(self):
        with open(self.csvfile, newline='') as csvfile:
            self.read = csv.reader(csvfile)
            for row in self.read:
                print(row)

    def csvreset(self):
        self.csvfile = 'import.csv'

    def ecrirefichier(self):
        print("nous sommes dans le repertoire pour ecrire dans le fichier", os.getcwd())
        with open(self.csvfile, 'a') as userdatas:
            self.newuser.set_nom(self.lastname.get())
            self.newuser.set_prenom(self.givenname.get())
            self.newuser.set_tel_number(self.telnum.get())
            self.newuser.set_mobile_number(self.mobile.get())
            self.newuser.set_email_address(self.email.get())
            self.newuser.set_email_address(self.email.get())
            # self.csv_writerow = csvwriterow self.csv_writerow.writelines({'firstname': self.newuser.prenom,
            # 'lastname': self.newuser.nom, 'office':'', 'password':self.password})
            userdatas.write(
                self.newuser.prenom + ";" + self.newuser.nom + ";" +
                self.newuser.prenom + '.' + self.newuser.nom + ";" + 'VP' + ";" + self.newuser.prenom + '.' +
                self.newuser.nom + ";" + self.newuser.tel_number + ";"
                + self.newuser.mobile_number + ";" + "IT" + ";" + self.newuser.email_address + '\n')
            # userdatas.close()
            self.lastname.delete(0, tk.END)
            self.givenname.delete(0, tk.END)
            self.telnum.delete(0, tk.END)
            self.mobile.delete(0, tk.END)
            self.email.delete(0, tk.END)
            Interface.update(self)

    def joinfile(self):
        self.argument = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
        self.csvfile = self.argument
        # self.read_label.config(text="")
        self.lire()
        self.csvreset()
        # print("le fichier contient : \n", type_output)

    def lire(self):
        self.read_label.destroy()
        print("nous sommes dans le repertoire", os.getcwd(), "pour lire le contenu du fichier", self.csvfile)
        self.row = 0
        # self.read_label.grid(column=5, row=self.row, sticky='w')
        with open(self.csvfile, newline='') as csv_file:
            print(csv_file)
            # self.lecture = file.read()
            # print(self.lecture)
            # for self.line in file.readlines():
            # self.read_label.configure(text=self.line)
            # self.read_label["text"] = self.line
            self.csv_read = csv.reader(csv_file)
            for row in self.csv_read:
                self.read_label = tk.Label(self, text=row)
                self.read_label.grid(column=5, row=self.row, sticky='w')
                # self.read_label.config(text=self.line)
                self.row += 1
        # Interface.update(self)

    def envoyer(self):
        """ Cette fonction permet d'exécuter la fonction de creation user
         à partir du fichier par defaut """

        os.chdir(self.current_dir)
        self.argument = self.csvfile
        self.command = self.cmd + self.ps_file + self.argument
        type_execute = os.popen(self.command)
        type_output = type_execute.read()
        self.row = 0
        # self.output = StringVar()
        print("resultat de la creation : \n")
        self.read_label = tk.Label(self, text=type_output)
        self.read_label.grid(column=5, row=self.row, sticky='w')
        # print("resultat de la creation : \n", type_output)

    def csv_init(self):
        self.csv_header = ''
        with open(self.csvfile, 'w', newline='') as csvfile:
            self.csv_header = ['firstname', 'lastname', 'login', 'job_title', 'samaccountname',
                               'tel_number', 'mobile_number', 'departement', 'email']
            self.csv_writer = csv.writer(csvfile, delimiter=';')
            self.csv_writer.writerow(self.csv_header)


class Utilisateur:
    """Classe utilisateur qui aura en paramètre d'entrée deux variables name et firstname :

    - attribut nom
    - attribut firstname
    """

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
