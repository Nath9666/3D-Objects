import os
import json
from datetime import datetime

# Define the directory to search (excluding the current directory)
search_directory = 'C://'
exception = "C://Users//Nathan//3D-Objects"

print('Searching for .blend files in the directory:', search_directory)

# List to store file details
file_details = []

# Traverse the directory tree
for root, dirs, files in os.walk(search_directory):
    if root.startswith(exception):
        continue
    else:
        for file in files:
            file_path = os.path.join(root, file)
            # Check if the file is not in the exception directory
            if file.endswith('.blend'):
                creation_date = datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
                modification_date = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
                print(len(file_details)+1)
                file_path = file_path.replace("\\","//")
                file_details.append({
                    'file_name': file,
                    'file_path': file_path,
                    'creation_date': creation_date,
                    'modification_date': modification_date
                })

print("Ecriture des details des "+ str(len(file_details)) + " fichiers dans un fichier JSON...")

# Save file details to a JSON file
json_file = './_output/output2'+search_directory.replace("://","")+'.json'
with open(json_file, 'w') as f:
    json.dump(file_details, f, indent=4)

import DeleteBlendFileInCurrentFolder