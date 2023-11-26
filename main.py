from functions import *
import os
if __name__ == "__main__":
    input_file = input("Saisir un texte à convertir:")
    process_file = input_file
    print(input_file)

# Call of the function
directory = "./speeches"
files_names = list_of_files(directory, "txt")
print(list(files_names))
new_dscr("speeches", "cleaned")

if __name__ == "__main__":
    # Chargement des données
    speeches_directory = "cleaned"
    files_names = list_of_files(speeches_directory, "txt")
    with open(os.path.join(speeches_directory, files_names[0]), 'r', encoding="utf-8") as file:
        text = file.read()
    words = text.split()

    while True:
        print("\nMenu:")
        print("1. Afficher les mots les moins importants")
        print("2. Afficher le(s) mot(s) ayant le score TF-IDF le plus élevé")
        print("3. Indiquer le(s) mot(s) le(s) plus répété(s) par le président Chirac")
        print("4. Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois")
        print("5. Indiquer le premier président à parler du climat et/ou de l’écologie")
        print("6. Hormis les mots dits « non importants », quel(s) est(sont) le(s) mot(s) que tous les présidents ont évoqués")
        print("0. Quitter")

        choice = input("Sélectionnez une option (0-6): ")

        if choice == "1":
            print("Mots les moins importants:", mot_peu_important(tfidf_matrix, words))
        elif choice == "2":
            n = int(input("Nombre de mots à afficher: "))
            print(f"Mot(s) avec le score TF-IDF le plus élevé: {highest_tfidf_words(tfidf_matrix, words, n)}")
        elif choice == "3":
            print("Mot(s) le(s) plus répété(s) par le président Chirac:", most_repeated_words_by_president(tfidf_matrix, words, "Chirac"))
        elif choice == "4":
            print("Président(s) ayant parlé de la « Nation » et celui qui l’a répété le plus de fois:", president_mentions_of_nation(tfidf_matrix, words))
        elif choice == "5":
            print("Premier président à parler du climat et/ou de l’écologie:", first_president_to_mention_climate_ecology(tfidf_matrix, words))
        elif choice == "6":
            print("Mot(s) évoqué(s) par tous les présidents hormis les mots dits « non importants »:", common_words_among_presidents(tfidf_matrix, words))
        elif choice == "0":
            print("Programme terminé.")
            break
        else:
            print("Option invalide. Veuillez choisir un nombre entre 0 et 6.")


