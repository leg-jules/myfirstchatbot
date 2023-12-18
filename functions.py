import os
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
new_dscr("speeches")

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
        with open(os.path.join(corpus_directory, filename), 'r', encoding='utf-8') as file:
            document = file.read()
            # Calculer le vecteur TF pour chaque document
            tf_vector = term_frequency(document)
            # Multiplication par le vecteur IDF pour obtenir le vecteur TF-IDF
            matrix.append(filename)
            for word, tf in tf_vector.items():
                for cle, val in idf_vector.items():
                    if str(cle) == str(word):
                        scoreIDF = val
                        tfidf_vector = {word: round(tf * scoreIDF,3) }

                        matrix.append(list(tfidf_vector.items()))
                        words.extend(tfidf_vector.keys())
    return matrix


print(tfidf_matrix("cleaned"))

def mot_peu_important(tfidf_matrix, words):
    peu_important = [word for word in words if all(tfidf_matrix[words.index(word)]) == 0]
    return peu_important

def highest_tfidf_words(tfidf_matrix, words, n=1):
    max_tfidf = [max(row) for row in tfidf_matrix]
    highest_tfidf_indices = sorted(range(len(max_tfidf)), key=lambda k: max_tfidf[k], reverse=True)[:n]
    return [words[i] for i in highest_tfidf_indices]

def most_repeated_words_by_president(tfidf_matrix, words, president_name):
    president_indices = [i for i, word in enumerate(words) if president_name.lower() in word.lower()]
    president_tfidf_sum = [sum(tfidf_matrix[:, idx]) for idx in president_indices]
    most_repeated_index = president_indices[president_tfidf_sum.index(max(president_tfidf_sum))]
    return words[most_repeated_index]

def president_mentions_of_nation(tfidf_matrix, words):
    nation_indices = [i for i, word in enumerate(words) if 'nation' in word.lower()]
    president_nation_counts = [sum(tfidf_matrix[:, idx] > 0) for idx in nation_indices]
    most_mentions_index = nation_indices[president_nation_counts.index(max(president_nation_counts))]
    return words[most_mentions_index]

def first_president_to_mention_climate_ecology(tfidf_matrix, words):
    climate_ecology_indices = [i for i, word in enumerate(words) if 'climate' in word.lower() or 'ecology' in word.lower()]
    first_president_index = min([next(i for i, value in enumerate(tfidf_matrix[:, idx] > 0) if value) for idx in climate_ecology_indices])
    return words[first_president_index]

def common_words_among_presidents(tfidf_matrix, words):
    common_words_indices = [i for i in range(len(words)) if all(tfidf_matrix[:, i] > 0)]
    return [words[i] for i in common_words_indices]