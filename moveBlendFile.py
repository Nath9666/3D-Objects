import os
import json
import shutil

PATH = './_output/'

def exist_file(file):
    """
    Check if a file exists.

    Args:
        file (str): The path of the file to check.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.exists(file)

def exist_current_folder(file, curent_folder=os.getcwd()):
    """
    Check if the file exist in the current folder.

    Args:
        file (str): The path of the file to check.
        current_folder (str): The path of the current folder.

    Returns:
        bool: True if the file exists in the current folder, False otherwise.
    """
    if not exist_file(file):
        return False
    if file == curent_folder:
        return True
    if file.startswith(curent_folder):
        return True
    else:
        return False

def copier_fichiers(fichier_json):
    if not exist_file(fichier_json):
        print(f'Le fichier {fichier_json} n\'existe pas.')
        return
    with open(fichier_json, 'r') as f:
        fichiers = json.load(f)

    for fichier in fichiers:
        chemin = fichier['file_path']
        name = fichier['file_name']
        try:
            if not exist_current_folder(chemin):
                chemin = chemin.replace('//', '/').replace('//', '/')
                if exist_file(chemin):
                    nom_fichier = os.path.basename(chemin)
                    nom_base, extension = os.path.splitext(nom_fichier)
                    nouveau_chemin = os.path.join(os.getcwd(), nom_base + '2' + extension)
                    shutil.copy2(chemin, nouveau_chemin)
                else:
                    shutil.copy2(chemin, os.getcwd())
            else:
                print(f'Le fichier {name} existe déjà dans le dossier courant.')
        except Exception as e:
            print(f'Erreur lors de la copie du fichier {name} : {e}')

if __name__ == "__main__":
    fichier_json = PATH + 'output2C.json'
    copier_fichiers(fichier_json)