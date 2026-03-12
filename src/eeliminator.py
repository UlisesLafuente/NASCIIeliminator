#!/usr/bin/env python3

import os
import sys
import unicodedata
import re

def es_emoji(caracter):
    codigo = ord(caracter)
    
    rangos_emoji = [
        (0x1F300, 0x1F5FF),  # Símbolos y pictogramas
        (0x1F600, 0x1F64F),  # Emoticonos
        (0x1F680, 0x1F6FF),  # Transporte y mapas
        (0x1F700, 0x1F77F),  # Símbolos alquímicos
        (0x1F780, 0x1F7FF),  # Formas geométricas extendidas
        (0x1F800, 0x1F8FF),  # Flechas suplementarias
        (0x1F900, 0x1F9FF),  # Símbolos suplementarios
        (0x1FA00, 0x1FA6F),  # Símbolos de ajedrez
        (0x1FA70, 0x1FAFF),  # Símbolos adicionales
        (0x2600, 0x26FF),    # Símbolos misceláneos
        (0x2700, 0x27BF),    # Dingbats
        (0xFE00, 0xFE0F),    # Selectores de variación
        (0x1F1E6, 0x1F1FF),  # Banderas (letras regionales)
        (0x1F004, 0x1F0CF),  # Símbolos de cartas
        (0x1F170, 0x1F251),  # Símbolos adicionales
        (0x1F3FB, 0x1F3FF),  # Tonos de piel
        (0x1F018, 0x1F0F5),  # Símbolos de mahjong
        (0x1F0A0, 0x1F0AE),  # Símbolos de cartas
        (0x1F200, 0x1F2FF),  # Símbolos CJK
        (0x1F300, 0x1F5FF),  # Pictogramas varios
        (0x1F600, 0x1F64F),  # Emojis faciales
        (0x1F680, 0x1F6FF),  # Transporte
        (0x1F900, 0x1F9FF),  # Emojis suplementarios
        (0x200D, 0x200D),    # Zero Width Joiner
        (0x20E3, 0x20E3),    # Combinación de teclas
        (0xFE0F, 0xFE0F),    # VS16 (Variation Selector-16)
    ]
    
    for inicio, fin in rangos_emoji:
        if inicio <= codigo <= fin:
            return True
    
    try:
        if unicodedata.name(caracter).startswith(('DIGIT', 'LATIN', 'SPACE', 'HYPHEN', 'COMMA', 'FULL STOP')):
            return False
        
        nombre = unicodedata.name(caracter, '')
        if 'EMOJI' in nombre or 'FACE' in nombre or 'HAND' in nombre:
            return True
    except:
        pass
    
    return False

def eliminar_emojis(texto):
    resultado = []
    emojis_eliminados = 0
    
    i = 0
    while i < len(texto):
        caracter = texto[i]
        
        if es_emoji(caracter):
            emojis_eliminados += 1
            i += 1
            continue
            
        if i + 1 < len(texto) and ord(texto[i+1]) == 0x200D:  
            j = i
            while j < len(texto) and (ord(texto[j]) == 0x200D or es_emoji(texto[j])):
                j += 1
            emojis_eliminados += (j - i)
            i = j
            continue
        
        resultado.append(caracter)
        i += 1
    
    return ''.join(resultado), emojis_eliminados

def procesar_archivo(archivo_entrada, archivo_salida):
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as file_in:
            contenido = file_in.read()

        contenido_filtrado, num_eliminados = eliminar_emojis(contenido)
        
        with open(archivo_salida, 'w', encoding='utf-8') as file_out:
            file_out.write(contenido_filtrado)
        
        print(f"Archivo procesado y guardado como {archivo_salida}")
        print(f"Se eliminaron {num_eliminados} emojis")
        print(f"Longitud original: {len(contenido)} caracteres")
        print(f"Longitud final: {len(contenido_filtrado)} caracteres")
    
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no existe.")
    except Exception as e:
        print(f"Error inesperado: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 eeliminator.py archivo_entrada.txt archivo_salida.txt")
        sys.exit(1)
    
    nombre_archivo_entrada = sys.argv[1]
    nombre_archivo_salida = sys.argv[2]
    
    print(f"Procesando {nombre_archivo_entrada}...")
    procesar_archivo(nombre_archivo_entrada, nombre_archivo_salida)
