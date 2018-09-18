import pygame

from scenarios.utils import utils
from scenarios.utils import consts

class Ena(pygame.sprite.Sprite):
    """
        Class representing the ena in the prologue
        physics => (velocity in x, velocity in y, running velocity)
    """
    def __init__(self, screen, clock, pos, character,
                 stage_width=1200, scrolls=False,
                 physics=(28, 28, 38)):
        pygame.sprite.Sprite.__init__(self)

        self.screen = screen
        self.clock = clock
        self.character = character
        self.x = pos[0]
        self.y = pos[1]
        self.frame = 0
        self.stage = {
            "width": stage_width,
            "x": 0,
            "startscroll": consts.WIDTH_SCREEN/2
        }
        self.velocity = physics[0]
        self.y_velocity = physics[1]
        self.running_velocity = physics[2]

        self.sprites = {
            "up": utils.load_image("up.png", self.character),
            "down": (utils.load_image("down1.png", self.character),
                     utils.load_image("down2.png", self.character)),
            "left": (utils.load_image("left1.png", self.character),
                     utils.load_image("left2.png", self.character),
                     utils.load_image("left3.png", self.character),
                     utils.load_image("left4.png", self.character)),
            "right": (utils.load_image("right1.png", self.character),
                      utils.load_image("right2.png", self.character),
                      utils.load_image("right3.png", self.character),
                      utils.load_image("right4.png", self.character))
        }
        self.direction = "stand"
        self.rect = pygame.Rect(pos, self.sprites["down"][0].get_size())
        self.rect.topleft = (self.x, self.rect.y)
        self.real_x = self.x
        self.scrolls = scrolls
        self.walls = []
        self.collision = False

    def control(self, x, y):
        self.rect.x += x
        self.rect.y += y
        if self.direction == "right":
            self.rect = pygame.Rect(self.rect.topleft, self.sprites["right"][0].get_size())
            block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
            self.collision = False
            for block in block_hit_list:
                if block.rect.collidepoint(self.rect.bottomright):
                    self.rect.x -= x
                    self.rect.y -= y
                    self.collision = True
                else:
                    self.collision = False
        elif  self.direction == "left":
            self.rect = pygame.Rect(self.rect.topleft, self.sprites["left"][0].get_size())
            block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
            self.collision = False
            for block in block_hit_list:
                if block.rect.collidepoint(self.rect.bottomleft):
                    self.rect.x -= x
                    self.rect.y -= y
                    self.collision = True
                else:
                    self.collision = False
        elif self.direction == "up":
            self.rect = pygame.Rect(self.rect.topleft, self.sprites["up"].get_size())
            block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
            for block in block_hit_list:
                if block.rect.collidepoint(self.rect.midbottom):
                    self.rect.x -= x
                    self.rect.y -= y
                    self.collision = False
        elif self.direction == "down":
            self.rect = pygame.Rect(self.rect.topleft, self.sprites["down"][0].get_size())
            block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
            for block in block_hit_list:
                if block.rect.collidepoint(self.rect.midbottom):
                    self.rect.x -= x
                    self.rect.y -= y
                    self.collision = False

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > consts.WIDTH_SCREEN:
            self.rect.x = consts.WIDTH_SCREEN-self.rect.width

        if self.rect.y+self.rect.height > 900:

            self.rect.y = 900-self.rect.height
        elif self.rect.y < 0:
            self.rect.y = 0

    def update(self):
        if self.direction == "right" or self.direction == "left":
            self.control(self.velocity, 0)
            self.frame += 1
            if self.frame > 7:
                self.frame = 0
            self.screen.blit(self.sprites[self.direction][(self.frame//2)], (self.rect.x, self.rect.y))
        elif self.direction == "stand":
            if self.velocity < 0:
                self.screen.blit(self.sprites["down"][1], (self.rect.x, self.rect.y))
            else:
                self.screen.blit(self.sprites["down"][0], (self.rect.x, self.rect.y))
        if self.direction == "up":
            self.control(0, self.y_velocity)
            self.screen.blit(self.sprites["up"], (self.rect.x, self.rect.y))
        elif self.direction == "down":
            self.control(0, self.y_velocity)
            self.frame += 1
            if self.frame > 7:
                self.frame = 0
            if self.velocity < 0:
                self.screen.blit(self.sprites["left"][(self.frame//2)], (self.rect.x, self.rect.y))
            else:
                self.screen.blit(self.sprites["right"][(self.frame//2)], (self.rect.x, self.rect.y))
        if self.scrolls is True:
            self.scroll()

    def scroll(self):
        if self.direction not in {"stand", "up", "down"} and self.collision is False:
            self.real_x += self.velocity
            if self.real_x > self.stage["width"]- self.rect.width:
                self.real_x = self.stage["width"] - self.rect.width
            elif self.real_x < 0:
                self.real_x = 0
            elif self.real_x <= self.stage["startscroll"]:
                self.stage["x"] = 0
            elif self.real_x >= self.stage["width"] - self.stage["startscroll"]:
                self.rect.x = self.real_x - self.stage["width"] + consts.WIDTH_SCREEN
                self.stage["x"] = -(self.stage["width"]-consts.WIDTH_SCREEN)
            else:
                self.rect.x = self.stage["startscroll"]
                self.stage["x"] += -self.velocity
