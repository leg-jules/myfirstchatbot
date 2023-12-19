#                     _____ .__                  __            .__              __  ___.             __
#   _____  ___.__. _/ ____\|__|_______  _______/  |_    ____  |  |__  _____  _/  |_\_ |__    ____ _/  |_
#  /     \<   |  | \   __\ |  |\_  __ \/  ___/\   __\ _/ ___\ |  |  \ \__  \ \   __\| __ \  /  _ \\   __\
# |  Y Y  \\___  |  |  |   |  | |  | \/\___ \  |  |   \  \___ |   Y  \ / __ \_|  |  | \_\ \(  <_> )|  |
# |__|_|  // ____|  |__|   |__| |__|  /____  > |__|    \___  >|___|  /(____  /|__|  |___  / \____/ |__|
#       \/ \/                              \/              \/      \/      \/           \/
#
#
#
# # Authors: Legalais Jules et Steed Dalphrase

from functions import *

if __name__ == "__main__":
    # Import des bibliothèques
    import random

    # Chargement des données
    speeches_directory = "cleaned"
    files_names = list_of_files(speeches_directory, "txt")

    n = random.randint(0, 100)
    vies = 10
    appreciation = "?"

    # Menu principal
    while True:
        print("\nMenu:")
        print("1. Afficher les mots les moins importants")
        print("2. Afficher le(s) mot(s) ayant le score TF-IDF le plus élevé")
        print("3. Indiquer le(s) mot(s) le(s) plus répété(s) par le président Chirac")
        print(
            "4. Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois")
        print("5. Indiquer le premier président à parler du climat et/ou de l’écologie")
        print(
            "6. Hormis les mots dits « non importants », quel(s) est(sont) le(s) mot(s) que tous les présidents ont évoqués")
        print("0. Quitter")
        print("9. Devinette de nombre")
        choice = input("Sélectionnez une option (0-9): ")

        if choice == "1":
            print(mot_peu_important(tfidf_matrix))
        elif choice == "2":
            n = int(input("Nombre de mots à afficher: "))
            print(highest_tfidf_words(tfidf_matrix, n=1))
        elif choice == "3":
            print(most_repeated_words_by_president(tfidf_matrix, "Chirac"))
        elif choice == "4":
            print(president_mentions_of_nation(tfidf_matrix))
        elif choice == "5":
            print(first_president_to_mention_climate_ecology(tfidf_matrix))
        elif choice == "6":
            print(common_words_among_presidents(tfidf_matrix))
        elif choice == "0":
            print("Programme terminé.")
            break
        elif choice == "9":
            # Lancement du mini-jeu
            while vies > 0:
                var = input("Entrez un nombre: ")
                var = int(var)

                if var < n:
                    appreciation = "trop bas"
                    print(vies, var, appreciation)
                elif var > n:
                    appreciation = "trop haut"
                    print(("vôtre nombre de vies est ", vies, var, appreciation))
                else:
                    appreciation = "bravo!"
                    print(vies, var, appreciation)
                    break

                vies -= 1
        else:
            print("Option invalide. Veuillez choisir un nombre entre 0 et 9.")
