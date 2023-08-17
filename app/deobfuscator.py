import json
import os
import re

def deobfuscate_text(text, mapping):
    """
    De-obfuscate the text based on the provided mapping.
    
    :param text: Obfuscated text
    :param mapping: Mapping used for obfuscation
    :return: De-obfuscated text
    """
    for original, obfuscated in mapping.items():
        # Replace only full word matches
        text = re.sub(r'\b' + re.escape(obfuscated) + r'\b', original, text)
    return text

# Get the absolute path of this script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path of the mapping.json file
mapping_file_path = os.path.join(script_dir, '..', 'output_files', 'mapping.json')

# Load the saved mapping
with open(mapping_file_path, 'r') as file:
    saved_mapping = json.load(file)

# Print the loaded mapping to debug
print("Loaded Mapping:", saved_mapping)

# Construct the absolute path of the obfuscated_response.txt file
response_file_path = os.path.join(script_dir, '..', 'responses', 'obfuscated_response.txt')

# Read the obfuscated response text from the file
with open(response_file_path, 'r') as file:
    response_text = file.read()

# Print the original obfuscated text to debug
print("Original Obfuscated Text:", response_text)

# De-obfuscate the response text
readable_response = deobfuscate_text(response_text, saved_mapping)

# Print the de-obfuscated text to debug
print("De-obfuscated Text:", readable_response)

# Construct the absolute path of the response_clean.txt file
clean_response_file_path = os.path.join(script_dir, '..', 'responses', 'response_clean.txt')

# Write the de-obfuscated, readable response to a new file
with open(clean_response_file_path, 'w') as file:
    file.write(readable_response)
