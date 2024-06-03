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

def copier_fichiers(fichier_json):
    if not exist_file(fichier_json):
        print(f'Le fichier {fichier_json} n\'existe pas.')
        return
    with open(fichier_json, 'r') as f:
        fichiers = json.load(f)

    for fichier in fichiers:
        chemin = fichier['file_path']
        chemin = chemin.replace('\\', '/').replace('//', '/')
        if exist_file(chemin):
            nom_fichier = os.path.basename(chemin)
            nom_base, extension = os.path.splitext(nom_fichier)
            nouveau_chemin = os.path.join(os.getcwd(), nom_base + '2' + extension)
            shutil.copy2(chemin, nouveau_chemin)
        else:
            shutil.copy2(chemin, os.getcwd())

if __name__ == "__main__":
    copier_fichiers(PATH + 'outputC.json')