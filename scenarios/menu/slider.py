import pygame
from scenarios.utils import utils

class Slider(pygame.sprite.Sprite):
    """
       Acts as a slider constructor, expects:
       pos => a tuple with the X & Y positions,
       folder => the base directory where the images are,
       width => the width the slider should be
       height => the height the slider should be
       level => the level the slider should be initialised
    """
    def __init__(self, pos, folder, width=383, height=98, level=1.0, flag=False):
        # pygame Sprite class constructor
        pygame.sprite.Sprite.__init__(self)

        self.pos = pos

        self.zero = utils.load_image("0.0.png",
                                     folder,
                                     -1,
                                     (width, height))
        self.twenty = utils.load_image("0.2.png",
                                       folder,
                                       -1,
                                       (width, height))
        self.forty = utils.load_image("0.4.png",
                                      folder,
                                      -1,
                                      (width, height))
        self.sixty = utils.load_image("0.6.png",
                                      folder,
                                      -1,
                                      (width, height))
        self.eighty = utils.load_image("0.8.png",
                                       folder,
                                       -1,
                                       (width, height))
        self.hundred = utils.load_image("1.0.png",
                                        folder,
                                        -1,
                                        (width, height))
        self.repo = {"0.0": self.zero,
                     "0.2": self.twenty,
                     "0.4": self.forty,
                     "0.6": self.sixty,
                     "0.8": self.eighty,
                     "1.0": self.hundred}

        # define the rects for all the sprite's states
        self.zero_rect = self.zero.get_rect(topleft=self.pos)
        self.twenty_rect = self.twenty.get_rect(topleft=self.pos)
        self.forty_rect = self.forty.get_rect(topleft=self.pos)
        self.sixty_rect = self.sixty.get_rect(topleft=self.pos)
        self.eighty_rect = self.eighty.get_rect(topleft=self.pos)
        self.hundred_rect = self.hundred.get_rect(topleft=self.pos)

        self.flag = flag
        self.level = level


    def get_current_level_image(self):
        return self.repo[str(self.level)]

    def increase_level(self, screen):
        if self.level != 1.0:
            self.level += 0.2
            self.level = round(self.level, 1)
            screen.blit(self.repo[str(self.level)], self.pos)
    def decrease_level(self, screen):
        if self.level != 0.0:
            self.level -= 0.2
            self.level = round(self.level, 1)
            screen.blit(self.repo[str(self.level)], self.pos)
