import pygame

from scenarios.utils import utils
from scenarios.utils import consts

class Wall(pygame.sprite.Sprite):
    """
        Class representing a collisionable object
    """
    def __init__(self, screen, clock, pos, platform, folder):
        pygame.sprite.Sprite.__init__(self)

        self.screen = screen
        self.clock = clock
        self.image = utils.load_image(platform, folder)
        self.mask = pygame.mask.from_surface(self.image)
        self.x = pos[0]
        self.y = pos[1]
        self.frame = 0
        self.rect = pygame.Rect(pos, self.image.get_size())
        self.rect.topleft = pos

    def update(self, rel_x=0):
        self.rect.x= self.x-rel_x
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
