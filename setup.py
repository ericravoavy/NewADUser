from cx_Freeze import setup, Executable
base = None

# Remplacer "monprogramme.py" par le nom du script qui lance votre programme
executables = [Executable("AddUserGUI.py", base=base)]

# Renseignez ici la liste complète des packages utilisés par votre application
packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

# Adaptez les valeurs des variables "name", "version", "description" à votre programme.
setup(
    name = "Interface ajout utilisateur",
    options = options,
    version = "1.0.1",
    description = 'Ajout utilisateur en interface graphique',
    executables = executables
)