import os
import psutil
import json
import time

def afficher_disques():
    disques = psutil.disk_partitions()
    for disque in disques:
        print(disque.device)

def trouver_fichiers_blend(repertoire, exeption=None):
    fichiers_blend = []
    for dossier, sous_dossiers, fichiers in os.walk(repertoire):
        for fichier in fichiers:
            if fichier.endswith(".blend"):
                chemin_fichier = os.path.join(dossier, fichier).replace("\\", "/")
                date_creation = time.ctime(os.path.getctime(chemin_fichier))
                date_modification = time.ctime(os.path.getmtime(chemin_fichier))
                fichiers_blend.append({"nom": fichier, "chemin": chemin_fichier, "date_creation": date_creation, "date_modification": date_modification})
    return fichiers_blend

if __name__ == "__main__":
    afficher_disques()
    print("Choisissez un disque : ")
    rep = input()
    print("Recherche des fichiers blend... dans le disque", rep)
    fichiers_blend = trouver_fichiers_blend(rep)

    print("Ecriture des fichiers blend dans un fichier JSON...")

    # ecrit dans un fichier JSON la liste des fichiers blend
    with open("fichiers_blend.json", "w") as f:
        for fichier_blend in fichiers_blend:
                print(fichier_blend)
                json.dump(fichier_blend, f)
                f.write("\n")