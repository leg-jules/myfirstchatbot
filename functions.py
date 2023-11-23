import os
def extract_president_name(filename):
    # Extrait le nom du président du nom du fichier
    parts = filename.split('_')
    if len(parts) >= 2:
        return parts[1]
    else:
        return None

def associate_president_firstname(president_name):
    # Associe un prénom à chaque nom de président
    first_names = {"Chirac": "Jacques",
        "dEstaing": "Valéry Giscard",
        "Mitterrand": "François",
        "Macron": "Emmanuel",
        "Sarkozy": "Nicolas",
        "Hollande": "François",}

        # Ajouter d'autres présidents pour 1 et 2
    return first_names.get(president_name, "Prénom inconnu")

def display_president_names(president_names):
    # Affiche la liste des noms de présidents
    print("Liste des noms de présidents :")
    for president in president_names:
        print(president)

def list_of_files(speeches,extension):
    files_names = []
    for filename in os.listdir(speeches):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names





def lower(text):     # Convertit le texte en minuscules
    text2 = text.lower()
    return(text2)
def new_dscr(disc_process,output_file):
    # lire le fichier
    for filename in os.listdir(disc_process):
        with open(disc_process +"/"+ filename, "r") as f:
            dscr = f.read()
        # traiter le texte
        cleaned_dscr = lower(dscr)

        with open(output_file+"/"+ filename, "w") as cleaned_f:
            cleaned_f.write(cleaned_dscr)






