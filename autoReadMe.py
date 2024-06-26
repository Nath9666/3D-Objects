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
            template_path = './TaskTemplate.md'  # Remplacez par le chemin vers votre fichier 'TaskTemplate'
            
            if not os.path.exists(os.path.join(start_path, name, 'Task.md')):
                # Lire le contenu du fichier 'TaskTemplate'
                with open(template_path, 'r') as template_file:
                    template_content = template_file.read()
            
                # Remplacer la première ligne par le nom
                template_content = template_content.replace('ProjectName', f'{name}', 1)
            
                # Écrire le contenu modifié dans le nouveau fichier 'Task.md'
                with open(os.path.join(start_path, name, 'Task.md'), 'w') as task_file:
                    task_file.write(template_content)
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

def find_step_project(start_path)-> dict:
    """
    Find the step of each project in the given start_path directory.

    Args:
        start_path (str): The directory path to start the search from.

    Returns:
        dict: A dictionary containing the step of each project.
    """
    step_project = {}
    for root, dirs, files in os.walk(start_path):
        for file in files:
            if file == 'Task.md':
                with open(os.path.join(root, file), 'r') as f:
                    content = f.readlines()
                    step = content[2].strip()
                    if step.startswith('Etat :'):
                        step = step[len('Etat :'):].strip()
                        step_project[os.path.basename(root)] = step
    return step_project

def write_README(start_path: str, step_project: dict):
    """
    Updates the content of the README.md file located in the specified start_path directory.

    Args:
        start_path (str): The path to the directory containing the README.md file.

    Returns:
        None
    """
    extension_img = ['.png', '.jpg', '.jpeg', '.avif', '.webp', '.gif']

    with open(os.path.join(start_path, 'README.md'), 'r') as f:
        content = f.read()

    start_point = content.index("## Les projets et leur avancement") + len("## Les projets et leur avancement")
    end_point = content.index("\n-- Fin des projets")

    new_content = content[:start_point]

    for name in os.listdir(start_path):
        if os.path.isdir(os.path.join(start_path, name)):
            try:
                step_project[name]
            except KeyError:
                step_project[name] = 'Default'
            new_content += f"\n ### {name} : {step_project[name]}\n"
            new_content += f"\n- [{name}](./{name}/Task.md) : \n"

            new_content += f"  - [Assets](./{name}/assets/)\n"

            new_content += f"  - [References](./{name}/ref/)\n"
            if os.path.join(start_path, name) in ref:
                #? print('Ref :', name)
                for img in os.listdir(os.path.join(start_path, name, 'ref')):
                    for ext in extension_img:
                        if img.endswith(ext):
                            new_content += f"    - ![image]({name}/ref/{img})\n"
                            break
                        
            new_content += f"  - [Rendu](./{name}/render/)\n"
            image_rendu = []
            image_count = 0
            if os.path.join(start_path, name) in rendu:
                #? print('Rendu :', name)
                for img in os.listdir(os.path.join(start_path, name, 'render')):
                    if (img.endswith('.png') or img.endswith('.jpg') or img.endswith('.jpeg')) and image_count < 10:
                        new_content += f"    - ![image]({name}/render/{img})\n"
                        image_count += 1

                        

    new_content += content[end_point:]

    with open(os.path.join(start_path, 'README.md'), 'w') as f:
        f.write(new_content)

if __name__ == '__main__':
    rendu, ref, assets, nombre = find_specific_folders('./')
    print('Nombre de dossiers parcourus :', nombre)

    create_specific_folders('./')
    write_README('./', find_step_project('./'))
    #delete_empty_folders('./')