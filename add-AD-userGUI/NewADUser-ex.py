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
fichier= open('User.txt',"w")

#Definir le champ first name
FirstName = Label(fenetre, text = 'First Name :')# Titre du champs First name
FirstName.grid(column=0, row=0, sticky='w')#Positionnement du label
Name= StringVar() #Récupérer une chaîne de caractère
FirstNameField = Entry(fenetre, textvariable= Name, width=31)#Champ de saisie du texte
FirstNameField.focus_set() #Focus sur le champs de saisie. curseur
#Positionnement du champs de saisie
FirstNameField.grid(column=1, row=0, sticky='e', columnspan=2, padx=10)

 
 
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

#Enable = Label(fenetre, text = 'Enable :')
#Enable.grid(column=0,row=7, sticky='w',pady=2)
#sexe=StringVar()
#homme= Radiobutton (fenetre, text="homme", variable=sexe, value=1)
#homme.focus_set()
#homme.grid(column=1, row=7,sticky='sw')
#femme= Radiobutton (fenetre, text="femme", variable=sexe, value=2)
#femme.focus_set()
#femme.grid(column=2, row=7,sticky='sw')
 
 
 
#Label9 = Label(fenetre, text = 'Hobbies : ')
#Label9.grid(column=0,row=9, sticky='w',pady=2)
 
 
#VP= IntVar()
#CheckVar2= IntVar()
#CheckVar3= IntVar()
#CheckVar4= IntVar()
#CheckVar5= IntVar()
#CheckVar6= IntVar()
 
#C1= Checkbutton (text="Cinema", variable=CheckVar1, onvalue=1, offvalue=0)
#C1.grid (column=1, row=8,sticky='sw')
 
#C2= Checkbutton (text="Equitation", variable=CheckVar2, onvalue=1, offvalue=0)
#C2.grid (column=1, row=9, sticky='sw')
 
#C3= Checkbutton (text="Planche à voile", variable=CheckVar3, onvalue=1, offvalue=0)
#C3.grid (column=1, row=10, sticky='sw')
 
#C4= Checkbutton (text="Musique", variable=CheckVar4, onvalue=1, offvalue=0)
#C4.grid (column=2, row=8,sticky='sw')
 
#C5= Checkbutton (text="Theatre", variable=CheckVar5, onvalue=1, offvalue=0)
#C5.grid (column=2, row=9, sticky='sw')
 
#C6= Checkbutton (text="Rien", variable=CheckVar6, onvalue=1, offvalue=0)
#C6.grid (column=2, row=10, sticky='sw')
 
 
 
bouton1= Button (fenetre, text="envoyer", pady=2)
bouton1.grid (column=1, row=11,sticky='sw', pady=20)
bouton2= Button (fenetre, text="réeinitialiser", command=reset, pady=2)
bouton2.grid (column=2, row=11,sticky='sw',pady=20)
 
 
fichier.close()             
fenetre.mainloop()
