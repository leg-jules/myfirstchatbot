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


def new_dscr(repertory):
    # lire le fichier
    for filename in os.listdir(repertory):
        with open(repertory+"/"+filename, "r", encoding="utf-8") as f, open("cleaned/"+filename, "w", encoding="utf-8") as cleaned_f:
            # traiter le texte
            for car in f.read():
                for k in ".:;,!/?'-":
                    car = car.lower().replace(k, " ")
                cleaned_f.write(car)


def term_frequency(text):
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
    idf_dict = {word: math.log10(total_docs / (count)) for word, count in doc_count.items()}

    return idf_dict


def tfidf_matrix(corpus_directory):
    # Liste pour stocker les vecteurs IDF pour chaque mot
    idf_vector = idf(corpus_directory)

    # Créer la matrice TF-IDF
    matrix = []
    words = []
    for filename in os.listdir(corpus_directory):
        dico = {}
        with open(os.path.join(corpus_directory, filename), 'r', encoding='utf-8') as file:
            document = file.read()
            # Calculer le vecteur TF pour chaque document
            tf_vector = term_frequency(document)
            # Multiplication par le vecteur IDF pour obtenir le vecteur TF-IDF
            matrix.append(filename)
            for word, tf in idf_vector.items():
                for cle, val in tf_vector.items():
                    if str(cle) == str(word):
                        dico[word]=round(tf * val,3)
                if word not in tf_vector.keys():
                        dico[word] = 0.0
        matrix.append(dico)
    return matrix

def additionDico(directory):
    dicoAdd = {}
    matrice = tfidf_matrix(directory)
    for i in range(1,16,2):
        for cle, val in matrice[i].items():
            if cle not in dicoAdd.keys():
                dicoAdd[cle] = val
            else:
                dicoAdd[cle] += val
    return dicoAdd

def mot_peu_important(directory):
    peu_important = []
    matrice = additionDico(directory)
    for mots, valeurs in matrice.items():
        if valeurs == 0.0:
            peu_important.append(mots)
    return peu_important

def highest_tfidf_words(directory):
    matrice = tfidf_matrix(directory)
    score = 0
    mot = ""
    for i in range(1,16,2):
        for cle, val in matrice[i].items():
            if score<val:
                score = val
                mot = cle
            elif score == val:
                mot = mot+cle
    return mot

def most_repeated_words_by_president(files:list):
    for element in files:
        text = open("cleaned/"+element,'r', encoding='utf-8').read()
        score = term_frequency(text)
        for cle, val in score.items():
            if cle not in score.keys():
                score[cle] = val
            else:
                score[cle] += val
        max_score = max(score, key=score.get)
    return max_score

def president_mentions_of_nation(directory,mot):
    dico = {}
    for filename in os.listdir(directory):
        cpt = 0
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
            document = file.read().lower().split()
            for i in range(len(document)):
                if str(document[i]) == str(mot.lower()):
                    cpt += 1
        if cpt != 0:
            dico[filename] = cpt
    return dico, max(dico, key=dico.get)

def first_president_to_mention_climate_ecology(directory,mot):
    dico = {}
    for filename in os.listdir(directory):

        i = 0
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
            document = file.read().lower().split()
            for i in range(len(document)):
                if str(document[i]) == str(mot.lower()):
                    dico[filename] = i
    if len(dico)!= 0:
        return min(dico, key=dico.get)
    else:
        return "Pas trouvé"


def common_words_among_presidents(tfidf_matrix, words):
    common_words_indices = [i for i in range(len(words)) if all(tfidf_matrix[:, i] > 0)]
    return [words[i] for i in common_words_indices]
