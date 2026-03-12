#!/usr/bin/env python3

import os
import sys

#Este script borra todos los caracteres no ASCII de un archivo.

def es_caracter_ascii(caracter):
    return ord(caracter) < 128

def procesar_archivo(archivo_entrada, archivo_salida):
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as file_in:
            contenido = file_in.read()
        
        contenido_filtrado = ''.join(caracter for caracter in contenido if es_caracter_ascii(caracter))
        
        with open(archivo_salida, 'w', encoding='ascii') as file_out:
            file_out.write(contenido_filtrado)
        
        print(f"Archivo procesado y guardado como {archivo_salida}")
    
    except FileNotFoundError:
        print("El archivo de entrada no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 emoji_eliminator.py archivo_entrada.txt archivo_salida.txt")
        sys.exit(1)
        
    nombre_archivo_entrada = sys.argv[1]
    nombre_archivo_salida = sys.argv[2]

    procesar_archivo(nombre_archivo_entrada, nombre_archivo_salida)
