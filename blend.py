import os
import json
from datetime import datetime

# Define the directory to search (excluding the current directory)
search_directory = 'C://'
exeption = './'

print('Searching for .blend files in the directory:', search_directory)

# List to store file details
file_details = []

# Traverse the directory tree
for root, dirs, files in os.walk(search_directory):
    # Exclude the current directory
    if root != search_directory:
        for file in files:
            if file.endswith('.blend') and root != exeption:
                file_path = os.path.join(root, file)
                creation_date = datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
                modification_date = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
                print('Found:', len(file_details))
                file_details.append({
                    'file_name': file,
                    'file_path': file_path,
                    'creation_date': creation_date,
                    'modification_date': modification_date
                })

print("Ecriture des details des fichiers dans un fichier JSON...")

# Save file details to a JSON file
json_file = './output.json'
with open(json_file, 'w') as f:
    json.dump(file_details, f, indent=4)