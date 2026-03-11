# Emoji Eliminator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Tres script de Python diseñados para eliminar caracteres indeseados de archivos de texto.

*NASCIIeliminator.py* elimina todos los caracteres no contenidos en el rango ASCII de un archivo y guarda el resultado en otro archivo de salida.

*eeliminator.py* elimina específicamente todos los emojis de un archivo de texto y guarda el resultado en otro archivo de salida.

*NASCIIrenamer.py* renombra todos los archivos de una carpeta, eliminando emojis, espacios y símbolos diacríticos.


## Requisitos

- Python 3.6 o superior
- No requiere librerías externas (solo usa módulos estándar)

## Uso:

### Básico
```bash
python3 eeliminator.py archivo_entrada.txt archivo_salida.txt
```
```bash
python3 NASCIIeliminator.py archivo_entrada.txt archivo_salida.txt
```
```bash
python3 NASCIIrenamer.py /ruta/directorio/renombrar/archivos
```

### Procesar múltiples archivos (usando bash)
```bash
for file in *.txt; do
    python3 emoji_eliminator.py "$file" "limpio_$file"
done
```
## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [license.txt](license.txt) para más detalles.

