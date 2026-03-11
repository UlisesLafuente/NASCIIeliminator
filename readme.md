# Emoji Eliminator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Dos script de Python diseñados para eliminar caracteres indeseados de archivos de texto.

*NASCIIeliminator.py* elimina todos los caracteres no contenidos en el rango ASCII de un archivo y guarda el resultado en otro archivo de salida.

*eeliminator.py* elimina específicamente todos los emojis de un archivode texto y guarda el resultado en otro archivo de salida.


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

### Procesar múltiples archivos (usando bash)
```bash
for file in *.txt; do
    python emoji_eliminator.py "$file" "limpio_$file"
done
```
## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

