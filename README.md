# Chrome Dino Game-bot
This bot can play chrome dino game.

![](https://img.shields.io/badge/python-v3.9.5-blue) ![](https://img.shields.io/badge/numpy-v1.21.0-darkgreen) ![](https://img.shields.io/badge/pillow-v8.3.1-darkgreen)

## Technologies Used
### Languages Used
* Python 3.9.5

### Modules Used
* Pyautogui
* Numpy 1.21.0
* Pillow 8.3.1

## Modules Installation
**Numpy** and **Pillow** are not pre-installed with python.

To install these modules, type the following commands in terminal.

```
pip install numpy==1.21.0
```
```
pip install pillow==8.3.1
```
or use the **requirements.txt** file.
```
pip install -r requirements.txt
```

## Instructions
* **Open** google chrome browser.
* Type "**chrome://dino**" in address bar and press **Enter**.
* Chrome dino game will open.
* Make sure the window is **maximised**.
* **Run** the program and make the game tab active.
* Everytime the obstacle is in the path of dino, the dino jumps over.
* If the dino **crashes** with the obstacle, the game **restarts** automatically.
* To **terminate** the script, move the mouse cursor to any one of the four corners of the screen.
* This is the built-in **fail-safe** mechanism of pyautogui and the program is **terminated**.

## License
This repository is licensed under **GNU General Public License** family.

![](https://img.shields.io/badge/License-GPL-color)
