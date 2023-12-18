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
    # Créer un dictionnaire pour stocker le nombre de documents dans lesquels chaque mot apparaît
    doc_count = {}

    # Parcourir tous les documents du corpus
    for filename in os.listdir(corpus_directory):
        with open(os.path.join(corpus_directory, filename), 'r', encoding='utf-8') as file:
            words = file.read().split()

            # Mettre à jour le dictionnaire `doc_count` avec le nombre de documents pour chaque mot
            for word in words:
                if word not in doc_count:
                    doc_count[word] = 0
                doc_count[word] += 1

    # Calculer l'IDF pour chaque mot
    idf_dict = {word: math.log(len(os.listdir(corpus_directory)) / count) for word, count in doc_count.items()}

    return idf_dict

def tfidf_matrix(corpus_directory, tf, idf):
    # Create a dictionary to store IDF values for each word
    idf_dict = {}
    for document in os.listdir(corpus_directory):
        document_words = document.split()
        # Calculate IDF for each word in the corpus
        for word in set(document_words):
            idf_dict[word] = idf(document_words)

    # Create a TF-IDF matrix
    tfidf_matrix = []
    word_list = []
    for filename in os.listdir(corpus_directory):
        with open(os.path.join(corpus_directory, filename), 'r', encoding='utf-8') as file:
            document = file.read().split()

            # Calculate TF vector for each document
            tf_vector = tf(document)

            # Calculate TF-IDF vector by multiplying TF with IDF values
            tfidf_vector = {
                word: tf * idf_dict[word]
                for word, tf in tf_vector.items()
            }
            tfidf_matrix.append(list(tfidf_vector.values()))

            # Append unique words to the word list
            word_list.extend(tfidf_vector.keys())

    return tfidf_matrix, word_list


def mot_peu_important(tfidf_matrix, words):
    peu_important = [word for word in words if all(tfidf_matrix[words.index(word)]) == 0]
    return peu_important               # retourne les mots les moins importants

def highest_tfidf_words(tfidf_matrix, words, n=1):
    # Extract the highest TF-IDF scores
    max_tfidf = tfidf_matrix.max(axis=1)

    # Find the indices of the highest TF-IDF scores
    highest_tfidf_indices = max_tfidf.argsort()[-n:][::-1]

    # Return the corresponding words
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


def load_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def get_tfidf_for_word(word, tfidf_matrix, words, directory):
    word_index = words.index(word)
    idf = calculate_idf(word, directory)

    tfidf_values = [row[word_index] * idf for row in tfidf_matrix]
    return tfidf_values


def calculate_idf(word, directory):
    document_count = len(list_of_files(directory, "txt"))
    documents_with_word = sum(
        1 for filename in list_of_files(directory, "txt") if word_in_document(word, os.path.join(directory, filename)))

    return math.log(document_count / (1 + documents_with_word))


def word_in_document(word, document_path):
    with open(document_path, 'r', encoding="utf-8") as file:
        document = file.read()
    return word in document


def list_least_important_words(tfidf_matrix, words, directory):
    least_important_words = []

    for word in words:
        tfidf_values = get_tfidf_for_word(word, tfidf_matrix, words, directory)
        if all(value == 0 for value in tfidf_values):
            least_important_words.append(word)

    return least_important_words


def list_most_important_words(tfidf_matrix, words):
    max_tfidf_values = [max(row) for row in tfidf_matrix]
    max_tfidf_index = max_tfidf_values.index(max(max_tfidf_values))

    most_important_words = [words[i] for i, value in enumerate(tfidf_matrix[max_tfidf_index]) if
                            value == max_tfidf_values[max_tfidf_index]]

    return most_important_words


def most_repeated_words_by_president(president, words, tfidf_matrix, directory):
    president_files = [filename for filename in list_of_files(directory, "txt") if
                       president.lower() in filename.lower()]
    if not president_files:
        return None

    president_text = " ".join([load_text_from_file(os.path.join(directory, filename)) for filename in president_files])
    cleaned_president_text = re.sub(r"[^\w\s]", "", lower(president_text))

    president_words = cleaned_president_text.split()
    tfidf_values = {word: get_tfidf_for_word(word, tfidf_matrix, words, directory) for word in president_words}

    most_repeated_words = [word for word, values in tfidf_values.items() if
                           sum(values) == max(sum(v) for v in tfidf_values.values())]

    return most_repeated_words
