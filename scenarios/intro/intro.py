import pygame

from gi.repository import Gtk
from scenarios.utils import utils
from scenarios.utils import consts
from scenarios.utils import saves
from scenarios.utils.button import Button
from scenarios.intro import walk
from actors.parrot import Parrot
from actors.prompt import Prompt


class Intro:
    """
        Class representing the intro comic, recieves
        a Surface as a screen, and a Clock as clock
    """
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.slot = saves.load()
        self.fx_channel = pygame.mixer.Channel(0)
        self.fx_channel.set_volume(consts.FX_VOLUME)
        self.vx_channel = pygame.mixer.Channel(1)
        self.vx_channel.set_volume(consts.VX_VOLUME)
        self.next_level = "m"
        self.character = "parrot"
        self.background = utils.load_image("background.png", "intro/screen_1")
        self.background_width = self.background.get_size()[0]

        self.dialogue = {
            "1": utils.load_image("d1.png", "intro/screen_1/dialogue"),
            "2": utils.load_image("d2.png", "intro/screen_1/dialogue"),
            "3": utils.load_image("d3.png", "intro/screen_1/dialogue"),
            "4": utils.load_image("d4.png", "intro/screen_1/dialogue"),
            "5": utils.load_image("d5.png", "intro/screen_1/dialogue"),
            "6": utils.load_image("d6.png", "intro/screen_1/dialogue"),
            "7": utils.load_image("d7.png", "intro/screen_1/dialogue")
        }

        self.prompt = Prompt(self.screen,
                             self.clock,
                             (2925, 540),
                             "prompt.png",
                             "",
                             (400,600))

        self.player = Parrot(self.screen,
                              self.clock,
                             (150, 710),
                             self.character,
                             3000,
                             True)
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
            rel_x = self.player.stage["x"]
            if rel_x < consts.WIDTH_SCREEN:
                self.screen.blit(self.background, (rel_x, 0))
                self.screen.blit(self.dialogue["1"], (44-abs(rel_x), 523))
                self.actors_load(abs(rel_x))
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
                        if 2789 < self.player.real_x < 3000:
                            utils.loading_screen(self.screen)
                            wal = walk.Walk(self.screen, self.clock)
                            wal.run()
                            del wal
                            running = False
                            utils.loading_screen(self.screen)
                            #save here
                            saves.first_save()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_KP4:
                        self.player.direction = "stand"
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                        self.player.direction = "stand"

    def actors_load(self, rel_x):
        if 448 < self.player.real_x < 980:
            self.screen.blit(self.dialogue["2"], (506-rel_x, 506))
        elif 1018 < self.player.real_x < 1298:
            self.screen.blit(self.dialogue["3"], (1083-rel_x, 506))
        elif 1297 < self.player.real_x < 1578:
            self.screen.blit(self.dialogue["4"], (1083-rel_x, 506))
        elif 1605 < self.player.real_x < 2166:
            self.screen.blit(self.dialogue["5"], (1668-rel_x, 506))
        elif 2194 < self.player.real_x < 2446:
            self.screen.blit(self.dialogue["6"], (2250-rel_x, 506))
        elif 2445 < self.player.real_x < 2754:
            self.screen.blit(self.dialogue["7"], (2250-rel_x, 506))
        elif 2789 < self.player.real_x < 3000:
            self.prompt.float(rel_x)
        self.player.update()
        if self.show_but:
            self.screen.blit(self.next.base, (270-rel_x, 730))
