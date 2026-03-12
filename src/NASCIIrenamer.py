#!/usr/bin/env python3

import os
import re
import sys

def remove_emojis(text):
    #Regular expression replacement
    #result = re.sub(pattern, replacement, input_text)
    return re.sub(r'[^\x00-\x7F]+', '', text)

'''
The regular expression r'[^\x00-\x7F]+' is used to match one or more characters that are not within the ASCII range (i.e., characters outside of the 128 most common characters in Western languages).
• r'...': The 'r' before the string denotes it as a raw string, meaning Python will not interpret backslashes as escape characters.
• [...]: This is a character class that matches any one of the enclosed characters or character ranges.
• ^: Inside a character class, ^ negates the match, so this part means "not" or "anything except".
• \x00-\x7F: This specifies a range of ASCII values from 0 (NUL) to 127. ASCII is a character encoding standard that includes characters used in most Western languages.
• +: Finally, the '+' quantifier says to match one or more occurrences of whatever precedes it.
So, [^\x00-\x7F] matches any single non-ASCII character. And [^\x00-\x7F]+ matches one or more consecutive non-ASCII characters.
'''

def normalize_text(text):
    # Normalizar mayúsculas a minúsculas
    text = text.lower()
    
    # Reemplazar espacios por guiones bajos
    text = text.replace(' ', '_')
    
    # Eliminar emojis y caracteres especiales no ASCII
    text = remove_emojis(text)
    
    return text

def rename_files_in_directory(directory):
    try:
        # Recorrer todos los archivos en la carpeta especificada
        for filename in os.listdir(directory):
            old_path = os.path.join(directory, filename)
            
            # Verificar si es un archivo (y no una carpeta)
            if os.path.isfile(old_path):
                # Normalizar el nombre del archivo
                new_filename = normalize_text(filename)
                
                # Crear la nueva ruta con el nuevo nombre de archivo
                new_path = os.path.join(directory, new_filename)
                
                # Renombrar el archivo
                os.rename(old_path, new_path)
                print(f'Renamed: {filename} -> {new_filename}')
    
    except Exception as e:
        print(f'Error: {e}')

def main():
    #Instrucciones en caso de que el usuario requiera guía
    if len(sys.argv) != 2:
        print("Uso: python3 NASCIIrenamer.py <ruta_a_carpeta>")
        sys.exit(1)
    
    directory_to_rename = sys.argv[1]

    # Asegurarse de que la carpeta existe
    if not os.path.exists(directory_to_rename):
        print(f"La carpeta {directory_to_rename} no existe.")
        sys.exit(1)

    rename_files_in_directory(directory_to_rename)

if __name__ == "__main__":
    main()
