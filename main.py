import os
if __name__ == "__main__":
    input_file = input("Saisir un texte à convertir:")
    process_file = input_file
    print(input_file)


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

# Call of the function
directory = "./speeches"
files_names = list_of_files(directory, "txt")
print(list(files_names))



