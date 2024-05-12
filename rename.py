import os

def count_blend_files(start_path):
    blend_counts = {}
    for root, dirs, files in os.walk(start_path):
        blend_count = sum(file.endswith('.blend') for file in files)
        if blend_count > 0:
            blend_counts[root] = blend_count
    return blend_counts

# Utilisez le chemin d'accès spécifié dans votre fichier
blend_counts = count_blend_files("./")
for folder, count in blend_counts.items():
    if count > 1:
        print(f"Dossier : {folder}, Nombre de fichiers .blend : {count}")
    else:
        print(f"Dossier : {folder}, Nombre de fichier .blend : {count}")
        # rename the file to a folder name
        for file in os.listdir(folder):
            if file.endswith('.blend'):
                new_name = os.path.join(folder, os.path.basename(folder) + '.blend')
                os.rename(os.path.join(folder, file), new_name)