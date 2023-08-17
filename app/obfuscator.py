import os
import re
import random
import string
import json

def obfuscate_names(names):
    """
    Generate a unique obfuscated name for each name provided.
    
    :param names: A list of names to be obfuscated
    :return: A dictionary mapping original names to obfuscated names
    """
    mapping = {}
    for name in names:
        if name not in mapping:
            obfuscated = ''.join(random.choice(string.ascii_letters) for _ in range(len(name)))
            mapping[name] = obfuscated
    return mapping

def obfuscate_sql(sql, mapping):
    """
    Replace the original names in the SQL query with obfuscated names based on the given mapping.
    
    :param sql: The SQL query text to be obfuscated
    :param mapping: A dictionary mapping original names to obfuscated names
    :return: The obfuscated SQL query text
    """
    for original, obfuscated in mapping.items():
        sql = re.sub(r'\b{}\b'.format(original), obfuscated, sql)
    return sql

def is_sql_keyword(word):
    """
    Check if a word is an SQL keyword.
    
    :param word: A string to be checked
    :return: True if the word is an SQL keyword, False otherwise
    """
    keywords = ['SELECT', 'FROM', 'WHERE', 'JOIN', 'ON', 'IN', 'AND', 'OR', 'NOT', 'NULL', 'GROUP', 'BY', 'HAVING', 'ORDER', 'INNER', 'LEFT', 'RIGHT', 'FULL', 'OUTER', 'AS']
    return word.upper() in keywords

def main():
    # Get the absolute path of the directory where this script is located
    script_directory = os.path.dirname(os.path.realpath(__file__))
    # Get the parent directory of the script directory
    base_directory = os.path.dirname(script_directory)

    # Construct the absolute paths of the input and output files
    input_file_path = os.path.join(base_directory, 'input_files', 'example_query.sql')
    prompt_input_path = os.path.join(base_directory, 'input_files', 'prompt.txt')
    output_file_path = os.path.join(base_directory, 'output_files', 'example_query_obfuscated.sql')
    prompt_output_path = os.path.join(base_directory, 'output_files', 'prompt_output.txt')
    mapping_path = os.path.join(base_directory, 'output_files', 'mapping.json')

    # Create the output_files directory if it doesn't exist
    if not os.path.exists(os.path.join(base_directory, 'output_files')):
        os.makedirs(os.path.join(base_directory, 'output_files'))

    # Read the SQL query from the input file
    with open(input_file_path, 'r') as file:
        sql = file.read()

    # Identify names in the SQL that are not SQL keywords
    names = set(word for word in re.findall(r'\b\w+\b', sql) if not is_sql_keyword(word))
    
    # Generate a mapping of original names to obfuscated names
    mapping = obfuscate_names(names)
    
    # Obfuscate the SQL query
    obfuscated_sql = obfuscate_sql(sql, mapping)

    # Write the obfuscated SQL query to the output file
    with open(output_file_path, 'w') as file:
        file.write(obfuscated_sql)

    # Read the prompt text from the input file
    with open(prompt_input_path, 'r') as file:
        prompt = file.read()

    # Obfuscate the prompt text using the same mapping
    obfuscated_prompt = obfuscate_sql(prompt, mapping)

    # Write the obfuscated prompt text to the output file
    with open(prompt_output_path, 'w') as file:
        file.write(obfuscated_prompt)
    
    # Save the mapping to a JSON file
    with open(mapping_path, 'w') as file:
        json.dump(mapping, file)

    # Print a completion message
    print("Obfuscation completed. Check the output_files directory.")

# This allows the script to be run from the command line
if __name__ == "__main__":
    main()
