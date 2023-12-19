# Authors: Legalais Jules et Steed Dalphrase
from functions import *

if __name__ == "__main__":
    while True:
        print("Menu:")
        print("1. Afficher les mots les moins importants")
        print("2. Afficher le(s) mot(s) ayant le score TF-IDF le plus élevé")
        print("3. Indiquer le(s) mot(s) le(s) plus répété(s) par le président Chirac")
        print("4. Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois")
        print("5. Indiquer le premier président à parler du climat et/ou de l’écologie")
        print("6. Hormis les mots dits « non importants », quel(s) est(sont) le(s) mot(s) que tous les présidents ont évoqués")
        print("7. Afficher la matrice TF-IDF")
        print("0. Quitter")
        print("9. Secret")
        choice = input("Sélectionnez une option (0-6): ")

        if choice == "1":
            directory = str(input("Enter a directory"))
            print("Mots les moins importants:", mot_peu_important(directory))

        elif choice == "2":
            directory = str(input("Enter a directory"))
            print(f"Mot(s) avec le score TF-IDF le plus élevé: ",highest_tfidf_words(directory))

        elif choice == "3":
            print("Mot(s) le(s) plus répété(s) par le président Chirac:", most_repeated_words_by_president(["Nomination_Chirac1.txt","Nomination_Chirac2.txt"]))

        elif choice == "4":
            directory = str(input("Enter a directory"))
            mot = str(input("Enter a word"))
            print("Président(s) ayant parlé de la « Nation » et celui qui l’a répété le plus de fois:", president_mentions_of_nation(directory, mot))

        elif choice == "5":
            directory = str(input("Enter a directory"))
            mot = str(input("Enter a word"))
            print("Premier président à parler du climat et/ou de l’écologie:", first_president_to_mention_climate_ecology(directory, mot))

        elif choice == "7":
            directory = str(input("Enter a directory"))
            print(tfidf_matrix(directory))

        elif choice == "0":
            print("Programme terminé.")
            break

        else:
            print("Option invalide. Veuillez choisir un nombre entre 0 et 6.")
