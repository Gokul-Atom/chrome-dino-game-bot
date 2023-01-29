import pyautogui as gui
from PIL import ImageGrab
from numpy import asarray, unique

gui.sleep(2)
gui.press("space")
x = 0
while True:
    image = asarray(ImageGrab.grab(bbox=(500, 540, 550 + x, 644)))
    if len(unique(image)) > 1:
        gui.press("space")
        x += 5
    if gui.pixelMatchesColor(675, 373, (83, 83, 83)):
        x = 0
        gui.press("space")
    if gui.pixelMatchesColor(675, 373, (172, 172, 172)):
        x = 0
        gui.press("space")
