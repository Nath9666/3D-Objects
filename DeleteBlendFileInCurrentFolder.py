import os
import json

exception = os.getcwd()
print('Excluding files in the directory:', exception)

file = './_output/output2C.json'

# Read the JSON file
with open(file, 'r') as f:
    data = json.load(f)

# Filter out objects where file_path matches the exception
data = [item for item in data if not item['file_path'].startswith(exception)]

# Write the filtered data back to the JSON file
with open(file, 'w') as f:
    json.dump(data, f, indent=4)