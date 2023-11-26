# youtube_ad_skip
Python script to skip youtube ads

## Introducción
Este script permite saltarse los anuncios de youtube presionando el botón "Omitir" automáticamente. Opera de la siguiente forma:

- El script captura la pantalla en forma periodica (cada 1 segundo)
- Dentro de la imagen capturada busca la zona del botón "Omitir" (esta posición se debe configurar y depende de la resolución de la pantalla)
- Se realiza un OCR (utilizando Tesseract) del contenido del botón buscando la palabra "Omitir" 
- Si se detecta la palabra "Omitir" entonces se realiza un click sobre el botón y se cierra la publicidad

## Botón
El botón de "Omitir" debe ser configurado en base a su posición en la pantalla, la cual depende de la resolución de esta. Para ello ajustar los datos definidos en:
```
# Posición de la zona a verificar
x = 1720
y = 850
w = 100
h = 50
```

## OCR
El OCR se realiza utilizando Tesseract. 

- La engine de Tesseract para Windows se puede descargar desde este link: https://github.com/UB-Mannheim/tesseract/wiki
- Lenguaje "spa" (español) desde este link: https://github.com/tesseract-ocr/tessdata_best, descargando el archivo "spa.traineddata" y copiarlo en la carpeta "tessdata" del directorio de instalación de Tesseract.
- Configurar el script con la ruta de instalación de Tesseract
```
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\mchav\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
```

## Paquetes requeridos
```
import time
import win32com.client as comclt
import win32gui
import win32ui
import win32con
import win32api
import ctypes
import cv2
import numpy as np
from datetime import datetime
import pytesseract
from pytesseract import Output
```

