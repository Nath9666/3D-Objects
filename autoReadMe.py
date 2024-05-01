import os

def find_specific_folders(start_path)-> tuple:
    """
    Find specific folders in the given start_path directory.

    Args:
        start_path (str): The directory path to start the search from.

    Returns:
        tuple: A tuple containing the lists of found folders and the total number of files in the start_path directory.
            The tuple contains the following elements:
            - rendu (list): A list of paths to folders named 'render' that are not empty.
            - ref (list): A list of paths to folders named 'ref' that are not empty.
            - assets (list): A list of paths to folders named 'assets' that are not empty.
            - nombre (int): The total number of files in the start_path directory.
    """
    rendu = []
    ref = []
    assets = []
    nombre = 0
    for root, dirs, files in os.walk(start_path):
        if 'ref' in dirs and not empty_folder(os.path.join(start_path, root, 'ref')):
            ref.append(root)
        if 'render' in dirs and not empty_folder(os.path.join(start_path, root, 'render')):
            rendu.append(root)
        if 'assets' in dirs and not empty_folder(os.path.join(start_path, root, 'assets')):
            assets.append(root)

    for name in os.listdir(start_path):
        nombre += 1
    return rendu, ref, assets, nombre

def create_specific_folders(start_path):
    """
    Create specific folders and a Task.md file in each subdirectory of the given start_path.

    Args:
        start_path (str): The path of the directory where the subdirectories are located.

    Returns:
        None
    """
    for name in os.listdir(start_path):
        if os.path.isdir(os.path.join(start_path, name)):
            for folder in ['ref', 'render', 'assets']:
                os.makedirs(os.path.join(start_path, name, folder), exist_ok=True)
            # create a Task.md file without overwriting its contents
            if not os.path.exists(os.path.join(start_path, name, 'Task.md')):
                with open(os.path.join(start_path, name, 'Task.md'), 'w') as f:
                    f.write(f"# {name} \n\n## Description\n\n## Objectifs\n\n ## Taches")
            else:
                with open(os.path.join(start_path, name, 'Task.md'), 'a') as f:
                    pass

def delete_empty_folders(start_path):
    """
    Deletes empty folders recursively starting from the given start_path.

    Args:
        start_path (str): The path of the directory to start deleting empty folders from.

    Returns:
        None
    """
    for root, dirs, files in os.walk(start_path, topdown=False):
        if not dirs and not files:
            os.rmdir(root)

def empty_folder(start_path) -> bool:
    """
    Check if a folder is empty.

    Args:
        start_path (str): The path of the folder to check.

    Returns:
        bool: True if the folder is empty, False otherwise.
    """
    for root, dirs, files in os.walk(start_path):
        if not dirs and not files:
            return True
    return False


def write_README(start_path):
    """
    Updates the content of the README.md file located in the specified start_path directory.

    Args:
        start_path (str): The path to the directory containing the README.md file.

    Returns:
        None
    """
    with open(os.path.join(start_path, 'README.md'), 'r') as f:
        content = f.read()

    start_point = content.index("## Les projets et leur avancement") + len("## Les projets et leur avancement")
    end_point = content.index("\n-- Fin des projets")

    new_content = content[:start_point]

    for name in os.listdir(start_path):
        if os.path.isdir(os.path.join(start_path, name)):
            new_content += f"\n ### {name} : \n"
            new_content += f"\n- [{name}](./{name}/Task.md) : \n"

            new_content += f"  - [Assets](./{name}/assets/)\n"

            new_content += f"  - [References](./{name}/ref/)\n"
            if os.path.join(start_path, name) in ref:
                print('Ref :', name)
                for img in os.listdir(os.path.join(start_path, name, 'ref')):
                    if img.endswith('.png') or img.endswith('.jpg') or img.endswith('.jpeg'):
                        new_content += f"    - ![image]({name}/ref/{img})\n"
                        
            new_content += f"  - [Rendu](./{name}/render/)\n"
            image_rendu = []
            image_count = 0
            if os.path.join(start_path, name) in rendu:
                print('Rendu :', name)
                for img in os.listdir(os.path.join(start_path, name, 'render')):
                    if (img.endswith('.png') or img.endswith('.jpg') or img.endswith('.jpeg')) and image_count < 10:
                        new_content += f"    - ![image]({name}/render/{img})\n"
                        image_count += 1

                        

    new_content += content[end_point:]

    with open(os.path.join(start_path, 'README.md'), 'w') as f:
        f.write(new_content)

rendu, ref, assets, nombre = find_specific_folders('./')
print('Nombre de dossiers parcourus :', nombre)
for i in rendu:
    print('Dossier rendu :', i)
for i in ref:
    print('Dossier ref :', i)
for i in assets:
    print('Dossier assets :', i)

create_specific_folders('./')
write_README('./')
#delete_empty_folders('./')

