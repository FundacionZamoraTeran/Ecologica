#!/usr/bin/python2
import sys
import pygame

from pygame.locals import *
from scenarios.utils import consts
from scenarios.menu import menu
from scenarios.intro import intro
from scenarios.map import mapp
from scenarios.farm import farm
from scenarios.farm2 import farm2
from scenarios.school import school
from scenarios.river import river
from scenarios.forest import forest
from scenarios.end import end

pygame.mixer.pre_init(44100, -16, 4, 2048)
pygame.mixer.init()
pygame.font.init()

class Eco:
    """
        Main class that handle the game loop
    """
    running = True
    def __init__(self):
        self.clock = None
        self.running = True
        self.next_level = 0

        self.levels = {
            "0": intro.Intro,
            "m": mapp.Map,
            "1": school.School,
            "2": "city.City",
            "3": farm2.Farm,
            "4": farm.Farm,
            "5": river.River,
            "6": forest.Forest,
            "7": end.End
        }

    def reset_clock(self):
        self.clock = pygame.time.Clock()

    def quit(self):
        self.running = False
    def run(self):
        pygame.mouse.set_visible(False)
        screen = pygame.display.get_surface()
        pygame.event.set_blocked([MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN])
        self.reset_clock()
        self.clock.tick(consts.FPS)
        meny = menu.Menu(screen, self.clock)
        meny.run()
        self.next_level = meny.level_selected
        del meny
        while self.next_level is not None:
            self.level_selector(screen, self.next_level)
        pygame.quit()
        sys.exit(0)

    def level_selector(self, screen, level):
        if level is not None:
            #here we should load against a dict the selected level
            var = self.levels[str(level)](screen, self.clock)
            var.run()
            self.next_level = var.next_level
