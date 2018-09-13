#!/usr/bin/python2
import sys
import pygame

from pygame.locals import *
from scenarios.utils import consts
from scenarios.menu import menu

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

        self.levels = {}

    def reset_clock(self):
        self.clock = pygame.time.Clock()


    def quit(self):
        self.running = False
    def run(self):
        screen = pygame.display.get_surface()
        pygame.event.set_blocked([MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN])
        self.reset_clock()
        self.clock.tick(consts.FPS)
        meny = menu.Menu(screen, self.clock)
        meny.run()
        pygame.quit()
        sys.exit(0)

    def level_selector(self, screen, level, slot):
        if level is not None and slot is not None:
            #here we should load against a dict the selected level
            var = self.levels[str(level)](screen, self.clock, slot)
            var.run()
            self.next_level = var.next_level
