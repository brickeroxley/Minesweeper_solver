# config.py
import platform

from pathlib import Path

# Construct an absolute path to the image
script_location = Path(__file__).resolve().parent
mine_image = str(script_location / 'assets' / 'bomb.png')
task_tray_image = str(script_location / 'assets' / 'task_tray.png')
task_tray_image_ico = str(script_location / 'assets' / 'task_tray_ico.ico')
game_over_png = str(script_location / 'assets' / 'game_over.png')


DIFFICULTIES = {
    "Beginner": {"size": 9, "mines": 10},
    "Intermediate": {"size": 16, "mines": 40},
    "Expert": {"size": 24, "mines": 99}
}

# gui related configuration

button_width = 30
button_height = 30

def get_task_tray_icon():
    if platform.system() == "Windows":
        return task_tray_image_ico
    else:
        return task_tray_image