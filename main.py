#                         ____ _              __           __            __   __            __
#    ____ ___   __  __   / __/(_)_____ _____ / /_   _____ / /_   ____ _ / /_ / /_   ____   / /_
#   / __ `__ \ / / / /  / /_ / // ___// ___// __/  / ___// __ \ / __ `// __// __ \ / __ \ / __/
#  / / / / / // /_/ /  / __// // /   (__  )/ /_   / /__ / / / // /_/ // /_ / /_/ // /_/ // /_
# /_/ /_/ /_/ \__, /  /_/  /_//_/   /____/ \__/   \___//_/ /_/ \__,_/ \__//_.___/ \____/ \__/
#            /____/



# Authors: Legalais Jules et Steed Dalphase
from functions import *
import os

# Call of the function
directory = "./speeches"
files_names = list_of_files(directory, "txt")
print(list(files_names))
new_dscr("speeches")
print(tfidf_matrix("cleaned"))

if __name__ == "__main__":
    # Chargement des données
    speeches_directory = "cleaned"
    files_names = list_of_files(speeches_directory, "txt")
    print(list(files_names))


    while True:
        print("\nMenu:")
        print("1. Afficher les mots les moins importants")
        print("2. Afficher le(s) mot(s) ayant le score TF-IDF le plus élevé")
        print("3. Indiquer le(s) mot(s) le(s) plus répété(s) par le président Chirac")
        print("4. Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois")
        print("5. Indiquer le premier président à parler du climat et/ou de l’écologie")
        print("6. Hormis les mots dits « non importants », quel(s) est(sont) le(s) mot(s) que tous les présidents ont évoqués")
        print("0. Quitter")
        print("9. Secret")
        choice = input("Sélectionnez une option (0-6): ")



        if choice == "1":
            print(mot_peu_important(tfidf_matrix)
        elif choice == "2":
            n = int(input("Nombre de mots à afficher: "))
            print(highest_tfidf_words(tfidf_matrix, words, n=n))
        elif choice == "3":
            print(most_repeated_words_by_president(tfidf_matrix, words, "Chirac"))
        elif choice == "4":
            print(president_mentions_of_nation(tfidf_matrix, words))
        elif choice == "5":
            print(first_president_to_mention_climate_ecology(tf_fichiers, words))
        elif choice == "6":
            print(common_words_among_presidents(tfidf_matrix, words))
        elif choice == "0":
            print("Programme terminé.")
            break
        else:
            print("Option invalide. Veuillez choisir un nombre entre 0 et 6.")


