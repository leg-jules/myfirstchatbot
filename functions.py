import os
import re
import math



def extract_president_name(filename):
    # Extrait le nom du président du nom du fichier
    parts = filename.split('_')
    if len(parts) >= 2:
        return parts[1]   # détache le nom en plusieurs parties et garde le nom
    else:
        return None

def associate_president_firstname(president_name):
    # Associe un prénom à chaque nom de président
    first_names = {"Chirac": "Jacques",
                   "dEstaing": "Valéry Giscard",
                   "Mitterrand": "François",
                   "Macron": "Emmanuel",
                   "Sarkozy": "Nicolas",
                   "Hollande": "François", }

    return first_names.get(president_name, "Prénom inconnu")

def display_president_names(president_names):
    # Affiche la liste des noms de présidents
    print("Liste des noms de présidents :")
    for president in president_names:

        return(president)

def list_of_files(speeches, extension):
    files_names = []
    for filename in os.listdir(speeches):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def lower(text):  # Convertit le texte en minuscules
    text2 = text.lower()
    return text2

def new_dscr(disc_process, output_file):
    # lire le fichier
    for filename in os.listdir(disc_process):
        with open(disc_process + "/" + filename, "r", encoding="utf-8") as f:
            dscr = f.read()
        # traiter le texte
        cleaned_dscr = re.sub(r"[^\w\s]", "", lower(dscr))

        with open(output_file + "/" + filename, "w", encoding="utf-8") as cleaned_f:
            cleaned_f.write(cleaned_dscr)
#enregisrte dans le bon fichier

def tfglobal(tf_fichiers,tf_global):
    for tf_fichier in tf_fichiers:
            for key in tf_fichier.keys():
                if key in tf_global:
                    tf_global[key] += tf_fichier[key]
                else:
                    tf_global[key] = tf_fichier[key]
    print(tf_global)
    return()

def calcul_tf(chaine):
    tf={}
    for mot in chaine:
        if mot not in tf:
            tf[mot]=1
        else:
            tf[mot]+=1


    tf_list=chaine.split()
    for mot in tf_list:
        if  "\n"in mot:
            mot = mot.replace("\n", "")
        if "é" in mot:
            mot = mot.replace("é", "e")
        if "è" in mot:
            mot = mot.replace("è", "e")
        if "à" in mot:
            mot = mot.replace("à", "a")
        if "'" in mot:
            mot= mot.replace("'", "  ")
        if "ù" in mot:
            mot = mot.replace("ù", "u")
        if mot not in tf:
            tf[mot] = 1
        else:
            tf[mot] += 1
    return(tf)


idf_fichier=[]
tf_global={}
def idf(tf_fichier,idf_fichier):
    for texte in tf_fichier:                         #parcourir tt les fichiers
        idffichier={}
        for key in tf_global.keys():
            if key in texte.keys():
                idffichier[key] = math.log(texte[key]/tf_global[key])
            else:
                idffichier[key] = 0
        idf_fichier.append(idffichier)

    return idf_fichier

documents = []


def tfidf_matrix(corpus_directory, idf_fichier):
    # créer une liste de documents

    for filename in os.listdir(corpus_directory):
        with open(os.path.join(corpus_directory, filename), 'r', encoding='utf-8') as file:
            document = file.read()
            words = document.split()
            documents.append(words)

    # créer un ensemble de mots uniques dans le corpus
    words = set()
    for document in documents:
        words.update(document)

    # créer une matrice TF-IDF
    tfidf_matrix = []
    for document in documents:
        tf_vector = calcul_tf(document)
        tfidf_vector = {word: tf * idf_fichier.get(word, 0) for word, tf in tf_vector.items()}
        tfidf_matrix.append(list(tfidf_vector.values()))

    return tfidf_matrix













# def tfidf_matrix(corpus_directory, idf):
#         # Create a list of documents
#         documents = []
#         for filename in os.listdir(corpus_directory):
#             with open(os.path.join(corpus_directory, filename), 'r', encoding='utf-8') as file:
#                 document = file.read()
#                 words = document.split()
#                 documents.append(words)
#
#         # Create a set of unique words in the corpus
#         words = set()
#         for document in documents:
#             words.update(document)
#
#         # Create a TF-IDF matrix
#         tfidf_matrix = []
#         for document in documents:
#             print("toto")
#             print(document)
#             tf_vector = calcul_tf(document)                   #####################
#             tfidf_vector = {word: tf * idf(words).get(word, 0) for word, tf in tf_vector.items()}
#             tfidf_matrix.append(list(tfidf_vector.values()))
#
#         return tfidf_matrix


        ###FONCTION DE LA IIème PARTIE

def first_president_to_mention_climate_ecology(tf_fichiers, words):
    for fichier in tf_fichiers:
        if "nature" or "climat" or "ecologie" in dict:
            print(os.listdir("cleaned"))
        else:
            print("Aucun président n'a prononcé le mot nature")
    return


# universal_word=["nature", "climat", "ecologie"]
# def universal_word():
#     for i in range (len(tfidf_matrix)):
#         if tfidf_matrix[i] in tfidf_matrix(i+1):
#             print(tfidf_matrix[i])
#         else:
#             print("Aucun mot commun à tous les présidents")
#     return universal_word