import os

def count_blend_files(start_path :str) -> dict:
    """
    Count the number of .blend files in a directory (not its subdirectories).

    Args:
        start_path (str): The path to the directory to start counting from.

    Returns:
        dict: A dictionary where the keys are the directories containing .blend files,
              and the values are the counts of .blend files in each directory.
    """
    blend_counts = {}
    for name in os.listdir(start_path):
        if os.path.isdir(os.path.join(start_path, name)):
            blend_count = sum(file.endswith('.blend') for file in os.listdir(os.path.join(start_path, name)))
            if blend_count > 0:
                blend_counts[name] = blend_count
    return blend_counts


def count_assets_ref_render(start_path: str) -> int:
    """
    Count the number of directories containing 'assets', 'ref', and 'render' subdirectories with files.

    Args:
        start_path (str): The path to the directory to start counting from.

    Returns:
        int: A dictionary where the keys are the directories containing 'assets', 'ref', and 'render' subdirectories,
              and the values are the counts of directories containing all three subdirectories with files.
    """
    arr = ['assets', 'ref', 'render']
    count = 0
    for root, dirs, files in os.walk(start_path):
        for d in dirs:
            if d in arr and os.listdir(os.path.join(root, d)):
                count += 1
    return count


path = './'
NbDirBlender = 0
NbAssets = 0

NbDir = len(os.listdir(path))

# Utilisez le chemin d'accès spécifié dans votre fichier
blend_counts = count_blend_files(path)

# Affichez les dossiers contenant plus d'un fichier .blend
for folder, count in blend_counts.items():
    NbDirBlender += 1
    if count > 1:
        print(f"Dossier : {folder}, Nombre de fichiers .blend : {count}")
    else:
        # Renome le fichier .blend unique dans le dossier en fonction du nom du dossier parent
        for file in os.listdir(folder):
            if file.endswith('.blend'):
                new_name = os.path.join(folder, os.path.basename(folder) + '.blend')
                os.rename(os.path.join(folder, file), new_name)
        NbAssets += count_assets_ref_render(folder)
        print(folder, ":", count_assets_ref_render(folder))


print("Note finale : ", NbAssets, "/", NbDirBlender*3)
print("Note finale : ", round(NbAssets/(NbDirBlender*3)*100, 2), "%")

print("Dossier sans fichier .blend : ", NbDir - NbDirBlender)