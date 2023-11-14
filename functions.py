import string


def dscr_prcsd(dscr):
    #supprime la ponctuation
    dscr = dscr.translate(str.maketrans('', '', string.punctuation))
    # Mettre en minuscules
    dscr = dscr.lower()
    return dscr

def new_dscr(disc_process):
    #lire le fichier
    with open(disc_process, "w") as f :
        dscr = f.read()

   #traiter le texte
    cleaned_dscr = dscr_prcsd(dscr)

    with open(disc_process, "w") as cleaned_f:
        cleaned_f.write(cleaned_dscr)






