from tkinter import *
import tkinter.messagebox
import tkinter


# Fonction de réinitialisation 
def reset():
    FirstNameField.delete(0,END)
    LastNameField.delete(0,END)
    TelField.delete(0,END)
    EmailField.delete(0,END)
    Login.delete(0,END)
    DeptField.delete(0,END)
    DescriptField.delete(0,END)
    Enable.deselect()
    #C2.deselect()
    #C3.deselect()
    #C4.deselect()
    #C5.deselect()
    #C6.deselect()
    #homme.deselect()
    #femme.deselect()
 
 
     
#DEfinition de notre fenetre racine
fenetre= Tk()
print("Hello World")
#fichier= open('User.txt',"w")

#Definir le champ first name
FirstNameLabel = Label(fenetre, text = 'First Name :')# Titre du champs First name
FirstNameLabel.grid(column=0, row=0, sticky='w')#Positionnement du label
FirstName= StringVar() #Récupérer une chaîne de caractère
FirstNameField = Entry(fenetre, textvariable= FirstName, width=31)#Champ de saisie du texte
FirstNameField.focus_set() #Focus sur le champs de saisie. curseur
#Positionnement du champs de saisie
FirstNameField.grid(column=1, row=0, sticky='e', columnspan=2, padx=10)
print(FirstName)
 
 
#Definir le champ first name
LastName = Label(fenetre, text = 'Last Name : ',)
LastName.grid(column=0, row=1,sticky='w',pady=2)
Last_Name= StringVar()
LastNameField = Entry(fenetre, textvariable= Last_Name, width=31)
LastNameField.focus_set()
LastNameField.grid(column=1, row=1,columnspan=2)
 
 
#Definir le champ Téléphone
Phone = Label(fenetre, text = 'Phone : ')
Phone.grid(column=0, row=2, sticky='w',pady=2)
Phone= StringVar()
TelField = Entry(fenetre, textvariable= Phone,width=31)
TelField.focus_set()
TelField.grid(column=1, row=2,columnspan=2)
 
#Definir le champ
Email = Label(fenetre, text = 'Email address : ')
Email.grid(column=0, row=3,sticky='w',pady=2)
Adresse= StringVar()
EmailField = Entry(fenetre, textvariable= Adresse,width=31)
EmailField.focus_set()
EmailField.grid(column=1, row=3,columnspan=2)
 
#Definir le champ
Login = Label(fenetre, text = 'Login : ')
Login.grid(column=0, row=4,sticky='w', pady=2)
MDP= StringVar()
Login = Entry(fenetre, textvariable= MDP,width=31)
Login.focus_set()
Login.grid(column=1, row=4,columnspan=2)
 
#Definir le champ 
Dept = Label(fenetre, text = 'Departement : ')
Dept.grid(column=0, row=5, sticky='w',pady=2)
Departement= StringVar()
DeptField = Entry(fenetre, textvariable= Departement,width=31)
DeptField.focus_set()
DeptField.grid(column=1, row=5,columnspan=2)
 
#Definir le champ 
Description = Label(fenetre, text = 'Description : ')
Description.grid(column=0,row=6, sticky='w',pady=2)
Descript= StringVar()
DescriptField= Entry(fenetre, textvariable= Descript,width=31)
DescriptField.focus_set()
DescriptField.grid(column=1, row=6, ipady=25,columnspan=2)

EnableAccount= IntVar()

Enable= Checkbutton (text="Enable Account", variable=EnableAccount, onvalue=1, offvalue=0)
Enable.grid (column=1, row=8,sticky='sw')

 
bouton1= Button (fenetre, text="envoyer", pady=2)
bouton1.grid (column=1, row=11,sticky='sw', pady=20)
bouton2= Button (fenetre, text="réeinitialiser", command=reset, pady=2)
bouton2.grid (column=2, row=11,sticky='sw',pady=20)
 
 
            
fenetre.mainloop()
