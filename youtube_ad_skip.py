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

def saveScreenShot(x, y, width, height, i):
    hdesktop = win32gui.GetDesktopWindow()
    desktop_dc = win32gui.GetWindowDC(hdesktop)
    img_dc = win32ui.CreateDCFromHandle(desktop_dc)
    mem_dc = img_dc.CreateCompatibleDC()
    screenshot = win32ui.CreateBitmap()
    screenshot.CreateCompatibleBitmap(img_dc, width, height)
    mem_dc.SelectObject(screenshot)
    mem_dc.BitBlt((0, 0), (width, height), img_dc, (x, y), win32con.SRCCOPY)
    signedIntsArray = screenshot.GetBitmapBits(False)
    img = np.array(signedIntsArray).astype(dtype="uint8")
    img.shape = (height,width,4)
    img_dc.DeleteDC()
    mem_dc.DeleteDC()
    win32gui.ReleaseDC(hdesktop, desktop_dc)
    win32gui.DeleteObject(screenshot.GetHandle())
    return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# Posición de la zona a verificar
x = 1720
y = 850
w = 100
h = 50

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()

print("Running")
i = 0
try:
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\mchav\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
    custom_config = r"--oem 3 --psm 6"
    while (True):
        i = i + 1
        originalImage = saveScreenShot(x, y, w, h, i)
        grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
        thresholdImage = cv2.threshold(grayImage, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
##        cv2.imshow('cuadro', thresholdImage)
        d = pytesseract.image_to_string(thresholdImage, output_type=Output.DICT, config=custom_config, lang="spa")
        s = d['text'].upper().strip()
        if s != "":
            if s == "OMITIR":
                x1 = int(x + 50)
                y1 = int(y + 10)
                win32api.SetCursorPos((x1,y1))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x1, y1, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x1, y1, 0, 0)
                time.sleep(3)

        time.sleep(1)
        cv2.waitKey(1)
        
except KeyboardInterrupt:
    pass

cv2.destroyAllWindows()
print("Fin")
