import os
from pygame.locals import *
MAIN_DIR = os.path.split(os.path.abspath(__file__))[0]

# General constants

FPS = 60
WIDTH_SCREEN = 1200
HEIGHT_SCREEN = 900
RESOLUTION = (WIDTH_SCREEN, HEIGHT_SCREEN)

# Save values

SAVEFILE = "../../saves.json"
MAX_SAVES = "3"

# Keybindings
K_CHECK = 257
K_CIRCLE = 265
K_CROSS = 259
K_SQUARE = 263

# Mixer Values
vol_list = ()
path = os.path.join(MAIN_DIR, "../../config.ini")
with open(path, "r+") as f:
    from ast import literal_eval
    vol_list = literal_eval(f.read()) # tuple (vx,bg,fx)
VX_VOLUME = vol_list[0]
BG_VOLUME = vol_list[1]
FX_VOLUME = vol_list[2]
