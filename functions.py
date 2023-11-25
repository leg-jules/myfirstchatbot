import os
import re
import math
from collections import Counter

def extract_president_name(filename):
    # Extrait le nom du président du nom du fichier
    parts = filename.split('_')
    if len(parts) >= 2:
        return parts[1]   #détache le nom en plusieurs parties et garde le nom
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
        print(president)


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

def tf(text):
    words = text.split()
    tf_dict = {}

    for word in words:
        tf_dict[word] = tf_dict.get(word, 0) + 1  #crée un compteur à valeur de 1 si le mot n'existe pas

    return tf_dict

def idf(corpus_directory):
    # Dictionnaire pour stocker le nombre de documents dans lesquels chaque mot apparaît
    doc_count = Counter()

    # Compter le nombre de documents dans lesquels chaque mot apparaît
    for filename in os.listdir(corpus_directory):
        with open(os.path.join(corpus_directory, filename), 'r', encoding='utf-8') as file:
            words = file.read().split()
            # Utiliser un ensemble pour s'assurer que chaque document contribue une seule fois par mot
            unique_words = set(words)
            doc_count.update(unique_words)

    # Nombre total de documents dans le corpus
    total_docs = len(os.listdir(corpus_directory))

    # Calcul de l'IDF pour chaque mot
    idf_dict = {word: math.log(total_docs / (count + 1)) for word, count in doc_count.items()}

    return idf_dict

def tfidf_matrix(corpus_directory, tf, idf):
    # Liste pour stocker les vecteurs IDF pour chaque mot
    idf_vector = idf([document.split() for document in os.listdir(corpus_directory)])

    # Créer la matrice TF-IDF
    matrix = []
    words = []
    for filename in os.listdir(corpus_directory):
        with open(os.path.join(corpus_directory, filename), 'r', encoding='utf-8') as file:
            document = file.read().split()
            # Calculer le vecteur TF pour chaque document
            tf_vector = tf(document)
            # Multiplication par le vecteur IDF pour obtenir le vecteur TF-IDF
            tfidf_vector = {word: tf * idf_vector[word] for word, tf in tf_vector.items()}
            matrix.append(list(tfidf_vector.values()))
            words.extend(tfidf_vector.keys())

def mot_peu_important(tfidf_matrix, words):
    peu_important = [word for word in words if all(tfidf_matrix[words.index(word)]) == 0]
    return peu_important

