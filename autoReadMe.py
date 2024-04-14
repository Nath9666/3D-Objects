import os

def find_specific_folders(start_path):
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
    for name in os.listdir(start_path):
        if os.path.isdir(os.path.join(start_path, name)):
            for folder in ['ref', 'render', 'assets']:
                os.makedirs(os.path.join(start_path, name, folder), exist_ok=True)

def delete_empty_folders(start_path):
    for root, dirs, files in os.walk(start_path, topdown=False):
        if not dirs and not files:
            os.rmdir(root)

def empty_folder(start_path)-> bool:
    for root, dirs, files in os.walk(start_path):
        if not dirs and not files:
            return True
    return False


def write_README(start_path):
    with open(os.path.join(start_path, 'README.md'), 'r') as f:
        content = f.read()

    start_point = content.index("## Les projets et leur avancement") + len("## Les projets et leur avancement")
    end_point = content.index("\n-- Fin des projets")

    new_content = content[:start_point]

    for name in os.listdir(start_path):
        if os.path.isdir(os.path.join(start_path, name)):
            new_content += f"\n ### {name} : \n"
            new_content += f"\n- [{name}](./{name}/Task.md) : \n"

            new_content += f"  - #### [Assets](./{name}/assets/)\n"

            new_content += f"  - #### [References](./{name}/ref/)\n"
            if os.path.join(start_path, name) in ref:
                print('Ref :', name)
                for img in os.listdir(os.path.join(start_path, name, 'ref')):
                    if img.endswith('.png') or img.endswith('.jpg') or img.endswith('.jpeg'):
                        new_content += f"    - ![image]({name}/ref/{img})\n"
                        
            new_content += f"  - #### [Rendu](./{name}/render/)\n"
            if os.path.join(start_path, name) in rendu:
                print('Rendu :', name)
                for img in os.listdir(os.path.join(start_path, name, 'render')):
                    if img.endswith('.png') or img.endswith('.jpg') or img.endswith('.jpeg'):
                        new_content += f"    - ![image]({name}/render/{img})\n"

                        

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

