import pygame

from gi.repository import Gtk
from scenarios.utils import utils
from scenarios.utils import consts
from scenarios.utils.button import Button
from scenarios.intro import school
from actors.parrot import Parrot
from actors.prompt import Prompt


class City:
    """
        Class representing the city portion of the intro comic,
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
        self.background = utils.load_image("background.png", "intro/screen_3")

        self.dialogue = {
            "1": utils.load_image("d1.png", "intro/screen_3/dialogue"),
            "2": utils.load_image("d2.png", "intro/screen_3/dialogue"),
            "3": utils.load_image("d3.png", "intro/screen_3/dialogue"),
        }

        self.prompt = Prompt(self.screen,
                             self.clock,
                             (1125, 540),
                             "prompt.png",
                             "",
                             (400,600))

        self.player = Parrot(self.screen,
                              self.clock,
                             (15, 710),
                             self.character)
        self.show_but = True

        self.prev = Button((503, 441),
                          "prev1.png",
                          "prev2.png",
                          48,
                          42,
                          "intro",
                          flag=True)
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
            self.screen.blit(self.background, (0, 0))
            self.actors_load()
            pygame.display.flip()
            self.clock.tick(consts.FPS)

            while Gtk.events_pending():
                Gtk.main_iteration()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.next_level = None
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
                        if 1005 < self.player.rect.x < 1201:
                            utils.loading_screen(self.screen)
                            scho = school.School(self.screen, self.clock)
                            scho.run()
                            del scho
                            running = False

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_KP4:
                        self.player.direction = "stand"
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                        self.player.direction = "stand"

    def actors_load(self):
        if 59 < self.player.rect.x < 316:
            self.screen.blit(self.dialogue["1"], (101, 576))
        elif 315 < self.player.rect.x < 691:
            self.screen.blit(self.dialogue["2"], (101, 576))
        elif 690 < self.player.rect.x < 1005:
            self.screen.blit(self.dialogue["3"], (101, 576))
        elif 1005 < self.player.rect.x < 1201:
            self.prompt.float(0)
        self.player.update()
        if self.show_but:
            self.screen.blit(self.next.base, (170, 730))
