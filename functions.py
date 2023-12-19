import os
from collections import Counter
import string
import math

def extract_president_name(filename):
    # Extrait le nom du président du nom du fichier
    parts = filename.split('_')
    if len(parts) >= 2:
        return parts[1]  # détache le nom en plusieurs parties et garde le nom
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
        with open(repertory + "/" + filename, "r", encoding="utf-8") as f, open("cleaned/" + filename, "w",
                                                                                encoding="utf-8") as cleaned_f:
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
        tf_dict[word] = tf_dict.get(word, 0) + 1  # crée un compteur à valeur de 1 si le mot n'existe pas

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
    idf_dict = {word: math.log10(total_docs / count) for word, count in doc_count.items()}

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
                        scoreidf = val
                        tfidf_vector = {word: round(tf * scoreidf, 3)}

                        matrix.append(list(tfidf_vector.items()))
                        words.extend(tfidf_vector.keys())
    return matrix
def mot_peu_important(tfidf_matrix):
    peu_important = []
    for word in tfidf_matrix:
        if tfidf_matrix == 0:
            peu_important.append(word)
    return peu_important


def highest_tfidf_words(tfidf_matrix, n=1):
    max_tfidf = []
    for row in tfidf_matrix:
        max_tfidf.append(max(row))

    highest_tfidf_indices = sorted(range(len(max_tfidf)), key=lambda k: max_tfidf[k], reverse=True)[:n]
    highest_tfidf_words = []
    for index in highest_tfidf_indices:
        if max_tfidf[index] >= 0:
            highest_tfidf_words.append(list(tfidf_matrix)[index])

    return highest_tfidf_words


def most_repeated_words_by_president(tfidf_matrix, president_name):
    president_indices = []
    for index, word in enumerate(tfidf_matrix):
        if president_name.lower() in word.lower():
            president_indices.append(index)

    president_tfidf_sum = []
    for idx in president_indices:
        tfidf_sum = sum(tfidf_matrix[:, idx])
        president_tfidf_sum.append(tfidf_sum)

    most_repeated_index = president_indices[president_tfidf_sum.index(max(president_tfidf_sum))]
    most_repeated_word = list(tfidf_matrix)[most_repeated_index]

    return most_repeated_word


def president_mentions_of_nation(tfidf_matrix):
    nation_indices = []
    for index, word in enumerate(tfidf_matrix):
        if 'nation' in word.lower():
            nation_indices.append(index)

    president_nation_counts = []
    for idx in nation_indices:
        nation_counts = sum(tfidf_matrix[:, idx] > 0)
        president_nation_counts.append(nation_counts)

    most_mentions_index = nation_indices[president_nation_counts.index(max(president_nation_counts))]
    most_mentions_word = list(tfidf_matrix)[most_mentions_index]

    return most_mentions_word


def first_president_to_mention_climate_ecology(tfidf_matrix):
    climate_ecology_indices = []
    for word in tfidf_matrix:
        if isinstance(word, str):
            if 'climate' in word.lower() or 'ecology' in word.lower():
                climate_ecology_indices.append(word)

    first_mention_index = min(
        (i for i, doc in enumerate(tfidf_matrix) if doc in climate_ecology_indices))
    first_mention_president = list(tfidf_matrix)[first_mention_index]

    return first_mention_president


def common_words_among_presidents(tfidf_matrix):
    common_words_indices = []
    for index in range(len(tfidf_matrix)):
        if all(tfidf_matrix[:, index] > 0):
            common_words_indices.append(index)

    common_words = []
    for index in common_words_indices:
        common_words.append(list(tfidf_matrix)[index])

    return common_words
def tokenize_question(question):
    words = question.split()
    # Supprimer les ponctuations
    for i, word in enumerate(words):
        if word in string.punctuation:
            words.pop(i)
    # Supprimer les majuscules
    words = [word.lower() for word in words]
    return words

def find_terms_in_corpus(terms):
    return [word for word in terms if word in terms]

terms = []

print(find_terms_in_corpus(terms))

def compute_tf_idf(terms): # pour les termes de la question
    # Calculer le TF
    tf = {}
    for word in terms:
        if word not in tf:
            tf[word] = 0
        tf[word] += 1

    # Calculer le IDF
    idf = {}
    for word in terms:
        if word not in idf:
            idf[word] = 0
        idf[word] = math.log10(len(terms) / (idf[word] + 1))

    # Calculer le TF-IDF
    tf_idf = {}
    for word in terms:
        tf_idf[word] = tf[word] * idf[word]
    return tf_idf

terms = []

print(compute_tf_idf(terms))



def find_terms_in_corpus(terms):
    return [word for word in terms if word in terms]

df={}
term_frequency1 = {}
idf1 = {}
def compute_tf_idf(terms):
    # Create a dictionary to store the TF and IDF values for each word
    tf_idf = {}

    # Calculate the TF for each word
    for word in terms:
        if word not in term_frequency1(terms):
            term_frequency1[word] = 0
        term_frequency1[word] += 1

    # Calculate the IDF for each word
    for word in terms:
        if word not in idf1:
            idf[word] = 0
        idf[word] = math.log10(len(terms) / (df[word] + 1))

    # Calculate the TF-IDF for each word
    for word in terms:
        tf_idf[word] = term_frequency1[word] * idf1[word]

    return tf_idf

def find_most_relevant_document(question, tf_idf_matrix, filenames):
    similarities = []
    for i, document in enumerate(tf_idf_matrix):
        similarity = 0
        for word, tf_idf in question.items():
            if word in document:
                similarity += tf_idf * document[word]
        similarities.append((similarity, filenames[i]))
    return max(similarities)[1]

def generate_response(question, tf_idf_matrix, filenames):
    document = find_most_relevant_document(question, tf_idf_matrix, filenames)
    with open(document, 'r') as f:
        content = f.read()
    words = tokenize_question(question)
    response = ""
    for word in words:
        if word in content:
            start = content.find(word)
            end = start + len(word)
            response += content[start:end] + " "
    return response

def generate_response_with_question_starter(question, tf_idf_matrix, filenames):
    response = generate_response(question, tf_idf_matrix, filenames)
    if question_starters.get(question[0]):
        response = question_starters[question[0]] + response
    return response

question_starters = {
    "qui": "Il est intéressant de noter que...",
    "quand": "Selon le corpus, le président a mentionné ce sujet...",
    "pourquoi": "Il semblerait que le président ait attaché une importance particulière à..."
}
filenames =["cleaned/Chirac.txt", "cleaned/Giscard.txt", "cleaned/Hollande.txt", "cleaned/Macron.txt", "cleaned/Mitterrand.txt", "cleaned/Pompidou.txt", "cleaned/Sarkozy.txt"]
def chatbot_mode():
    while True:
        question = input("Question: ")
        response = generate_response_with_question_starter(question, tfidf_matrix, filenames)
        response_list = list(response)
        print("Réponse: " + response_list[0])
        if response_list[0] == "Je ne sais pas":
            break
