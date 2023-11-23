import os
from functions import *
if __name__ == "__main__":
    input_file = input("Saisir un texte à convertir:")
    process_file = input_file
    print(input_file)


# Call of the function
directory = "./speeches"
files_names = list_of_files(directory, "txt")
print(list(files_names))

new_dscr("speeches","cleaned")
