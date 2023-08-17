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

print(obfuscate_names('mark is the dad'))
