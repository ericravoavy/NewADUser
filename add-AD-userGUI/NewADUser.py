# -*- coding: latin-1 -*-

#importer Tkinter pour créer une interface graphique
from tkinter import *

# créer une fenêtre, racine de notre interface
window = Tk()
window.title('Add New User') #titre de notre fenêtre
window.geometry("500x500") #Dimension de la fen�tre
window.maxsize(500, 500) #taille maximum de la fen�tre

#creation un cadre qui contiendrons nos champs


#info = Frame(window, borderwidth=2, bg="black")
#info.pack(fill=BOTH)

#titre = Label(info, text="User Information")
#titre.pack(side="top")

#construction du premier champ de saisie
name_label = Label(window, text="first Name")
name_label.pack(side=LEFT, padx=10, pady=10)

#champ de texte
name_text = StringVar()
name_entry = Entry(window, textvariable=name_text, width=30)
#name_entry.focus_set()
name_entry.pack(side=LEFT, padx=10, pady=10)

firstname_label = Label(window, text="last Name")
firstname_label.pack(side=LEFT, padx=10, pady=10)

#champ de texte
firstname_text = StringVar()
firstname_entry = Entry(window, textvariable=firstname_text, width=30)
#firstname_entry.focus_set()
firstname_entry.pack(side=LEFT, padx=10, pady=10)

#name_label = Label(window, text="first Name")
#name_label.pack(side=LEFT, ipadx=10, padx=10, pady=10)

window.mainloop()
