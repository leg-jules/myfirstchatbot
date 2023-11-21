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
    first_names = {
        "Chirac": "Jacques",
        "dEstaing": "Valéry Giscard",
        "Mitterrand": "François",
        "Macron": "Emmanuel",
        "Sarkozy": "Nicolas",
        "Hollande": "François",

        # Ajouter d'autres présidents pour 1 et 2
    }
    return first_names.get(president_name, "Prénom inconnu")

def display_president_names(president_names):
    # Affiche la liste des noms de présidents
    print("Liste des noms de présidents :")
    for president in president_names:
        print(president)


def convert_to_lowercase_and_save(input_path, output_path):
    # Convertit le texte en minuscules et enregistre le contenu dans un nouveau fichier
    with open(input_path, 'r', encoding='utf-8') as file:
        text = file.read()

    text_lower = text.lower()

    output_filename = os.path.join(output_path, os.path.basename(input_path))

    with open(output_filename, 'w', encoding='utf-8') as output_file:
        output_file.write(text_lower)


# Exemple d'utilisation pour un fichier "Nomination_Hollande.txt"
filename = "Nomination_Hollande.txt"

president_name = extract_president_name(filename)
if president_name:
    first_name = associate_president_firstname(president_name)
    print(f"Nom du président: {first_name} {president_name}")

# Affichage de la liste des noms de présidents (à ajuster selon vos besoins)
all_president_names = ["Chirac", "dEstaing", "Mitterrand", "Macron", "Sarkozy", "Hollande"]
display_president_names(all_president_names)

# Conversion en minuscules et sauvegarde dans le dossier "cleaned"
input_path = os.path.join("speeches", filename)
output_directory = "cleaned"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

output_path = os.path.join(output_directory, filename)
convert_to_lowercase_and_save(input_path, output_path)








