import json
import os

MAIN_DIR = os.path.split(os.path.abspath(__file__))[0]

PATH = os.path.join(MAIN_DIR, "../../saves.json")
with open(PATH, "r") as f:
    saves = json.load(f)

SLOT1 = saves["slot_1"]
STAGES = ("escuela",
          "bosque",
          "granja",
          "granja2",
          "rio",
          "ciudad",
          "completado")

def load():
    """
       Method's function is to return
       the save slot.
    """
    return saves["slot_1"]

def first_save():
    """
       used when initialising an empty save slot
    """
    saves["slot_1"] = {}
    saves["slot_1"]["coins"] = 8
    saves["slot_1"]["stages"] = {}
    saves["slot_1"]["last_level_passed"] = {"code": 1, "name": "Inicio"}
    saves["slot_1"]["stages"]["inicio"] = True
    for stage in STAGES:
        saves["slot_1"]["stages"][stage] = False

    with open(PATH, "w") as s:
        json.dump(saves, s)

def save(code, name, stage):
    saves["slot_1"]["last_level_passed"] = {"code": code, "name": name}
    saves["slot_1"]["stages"][stage] = True
    with open(PATH, "w") as s:
        json.dump(saves, s)

def specific_save(slot, attr, value):
    saves[slot][attr] = value
    with open(PATH, "w") as s:
        json.dump(saves, s)
