import sys
import pygame

from gi.repository import Gtk
from scenarios.utils import utils
from scenarios.utils import consts
from scenarios.utils.button import Button
from scenarios.intro import court
from actors.parrot import Parrot
from actors.prompt import Prompt

class Book:
    """
        Class representing the book part of the intro comic,
        recieves a Surface as a screen, and a Clock as clock
    """
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.fx_channel = pygame.mixer.Channel(0)
        self.fx_channel.set_volume(consts.FX_VOLUME)
        self.vx_channel = pygame.mixer.Channel(1)
        self.vx_channel.set_volume(consts.VX_VOLUME)
        self.character = "parrot"
        self.background = utils.load_image("background.png", "intro/screen_7")
        self.background_width = self.background.get_size()[0]
        self.poem = utils.load_image("poem.png", "intro/screen_7")

        self.dialogue = {
            "1": utils.load_image("d1.png", "intro/screen_7/dialogue"),
            "2": utils.load_image("d2.png", "intro/screen_7/dialogue"),
            "3": utils.load_image("d3.png", "intro/screen_7/dialogue")
        }

        self.prompt = Prompt(self.screen,
                             self.clock,
                             (2325, 540),
                             "prompt.png",
                             "",
                             (400, 600))

        self.player = Parrot(self.screen,
                              self.clock,
                             (15, 810),
                             self.character,
                             2400,
                             True)
        self.show_but = True

        self.prev = Button((503, 441),
                           "prev1.png",
                           "prev2.png",
                           48,
                           42,
                           "intro",
                           flag=True),
        self.next = Button((611, 441),
                           "next1.png",
                           "next2.png",
                           48,
                           42,
                           "intro")

    def run(self):
        utils.load_bg("khachaturian.ogg")
        pygame.mixer.music.set_volume(consts.BG_VOLUME)
        pygame.mixer.music.play(-1, 0.0)
        running = True

        while running:
            rel_x = self.player.stage["x"]
            if rel_x < consts.WIDTH_SCREEN:
                self.screen.blit(self.background, (rel_x, 0))
                self.actors_load(abs(rel_x))
            pygame.display.flip()
            self.clock.tick(consts.FPS)

            while Gtk.events_pending():
                Gtk.main_iteration()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_KP4:
                        self.show_but = False
                        self.player.direction = "left"
                        self.player.velocity = -abs(self.player.velocity)
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                        self.show_but = False
                        self.player.direction = "right"
                        self.player.velocity = abs(self.player.velocity)
                    elif event.key == pygame.K_SPACE or event.key == consts.K_CROSS:
                        if 2222 < self.player.real_x < 2401:
                            utils.loading_screen(self.screen)
                            cou = court.Court(self.screen, self.clock)
                            cou.run()
                            del cou
                            running = False

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_KP4:
                        self.player.direction = "stand"
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                        self.player.direction = "stand"

    def actors_load(self, rel_x):
        self.player.update()
        if self.show_but:
            self.screen.blit(self.next.base, (270-rel_x, 830))

        if 59 < self.player.real_x < 511:
            self.screen.blit(self.dialogue["1"], (200, 606))
        elif 510 < self.player.real_x < 1216:
            self.screen.blit(self.poem, (98, 50))
        elif 1290 < self.player.real_x < 1756:
            self.screen.blit(self.dialogue["2"], (1350-rel_x, 606))
        elif 1755 < self.player.real_x < 2223:
            self.screen.blit(self.dialogue["3"], (1350-rel_x, 606))
        elif 2222 < self.player.real_x < 2401:
            self.prompt.float(rel_x)
