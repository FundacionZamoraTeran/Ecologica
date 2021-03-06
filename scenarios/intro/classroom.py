import sys
import pygame

from gi.repository import Gtk
from scenarios.utils import utils
from scenarios.utils import consts
from scenarios.utils.button import Button
from scenarios.intro import bell
from actors.parrot import Parrot
from actors.prompt import Prompt


class Classroom:
    """
        Class representing the classroom segment of the intro comic,
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
        self.background = utils.load_image("background.png", "intro/screen_5")
        self.background_width = self.background.get_size()[0]
        #self.npc = utils.load_image("npc_icon.png", "intro/screen_5")

        self.dialogue = {
            "1": utils.load_image("d1.png", "intro/screen_5/dialogue"),
            "2": utils.load_image("d2.png", "intro/screen_5/dialogue"),
            "3": utils.load_image("d3.png", "intro/screen_5/dialogue"),
            "4": utils.load_image("d4.png", "intro/screen_5/dialogue"),
            "5": utils.load_image("d5.png", "intro/screen_5/dialogue"),
            "6": utils.load_image("d6.png", "intro/screen_5/dialogue"),
            "7": utils.load_image("d7.png", "intro/screen_5/dialogue"),
            "8": utils.load_image("d8.png", "intro/screen_5/dialogue")
        }

        self.voices = {
            "1": utils.load_vx("intro/screen_5/1.ogg"),
            "2": utils.load_vx("intro/screen_5/2.ogg"),
            "3": utils.load_vx("intro/screen_5/3.ogg"),
            "4": utils.load_vx("intro/screen_5/4.ogg"),
            "5": utils.load_vx("intro/screen_5/5.ogg"),
            "6": utils.load_vx("intro/screen_5/6.ogg"),
            "7": utils.load_vx("intro/screen_5/7.ogg"),
            "8": utils.load_vx("intro/screen_5/8.ogg")
        }

        self.played = [0] * 8

        self.prompt = Prompt(self.screen,
                             self.clock,
                             (2325, 500),
                             "prompt.png",
                             "",
                             (400, 600))

        self.player = Parrot(self.screen,
                              self.clock,
                             (15, 775),
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
                           flag=True)
        self.next = Button((611, 441),
                           "nnext.png",
                           "next2.png",
                           89,
                           77,
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
                        if 2220 < self.player.real_x < 2401:
                            self.vx_channel.stop()
                            utils.loading_screen(self.screen)
                            bel = bell.Bell(self.screen, self.clock)
                            bel.run()
                            del bel
                            running = False

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_KP4:
                        self.player.direction = "stand"
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                        self.player.direction = "stand"

    def actors_load(self, rel_x):
        self.player.update()
        if self.show_but:
            self.screen.blit(self.next.base, (280-rel_x, 795))

        if 59 < self.player.real_x < 166:
            if self.played[0] == 0:
                self.vx_channel.stop()
                self.vx_channel.play(self.voices["1"])
                self.played[1] = 0
                self.played[0] = 1
            self.screen.blit(self.dialogue["1"], (100, 631))
        elif 165 < self.player.real_x < 301:
            if self.played[1] == 0:
                self.vx_channel.stop()
                self.vx_channel.play(self.voices["2"])
                self.played[0] = 0
                self.played[2] = 0
                self.played[1] = 1
            self.screen.blit(self.dialogue["2"], (100, 631))
        elif 300 < self.player.real_x < 526:
            if self.played[2] == 0:
                self.vx_channel.stop()
                self.vx_channel.play(self.voices["3"])
                self.played[1] = 0
                self.played[3] = 0
                self.played[2] = 1
            self.screen.blit(self.dialogue["3"], (100, 631))
        elif 525 < self.player.real_x < 661:
            if self.played[3] == 0:
                self.vx_channel.stop()
                self.vx_channel.play(self.voices["4"])
                self.played[2] = 0
                self.played[4] = 0
                self.played[3] = 1
            self.screen.blit(self.dialogue["4"], (100, 631))
        elif 660 < self.player.real_x < 796:
            if self.played[4] == 0:
                self.vx_channel.stop()
                self.vx_channel.play(self.voices["5"])
                self.played[3] = 0
                self.played[5] = 0
                self.played[4] = 1
            self.screen.blit(self.dialogue["5"], (100, 631))
        elif 795 < self.player.real_x < 1036:
            if self.played[5] == 0:
                self.vx_channel.stop()
                self.vx_channel.play(self.voices["6"])
                self.played[4] = 0
                self.played[6] = 0
                self.played[5] = 1
            self.screen.blit(self.dialogue["6"], (100, 631))
        elif 1290 < self.player.real_x < 1756:
            if self.played[6] == 0:
                self.vx_channel.stop()
                self.vx_channel.play(self.voices["7"])
                self.played[5] = 0
                self.played[7] = 0
                self.played[6] = 1
            self.screen.blit(self.dialogue["7"], (1300-rel_x, 631))
        elif 1755 < self.player.real_x < 2221:
            if self.played[7] == 0:
                self.vx_channel.stop()
                self.vx_channel.play(self.voices["8"])
                self.played[0] = 0
                self.played[6] = 0
                self.played[7] = 1
            self.screen.blit(self.dialogue["8"], (1300-rel_x, 631))
        elif 2220 < self.player.real_x < 2401:
            self.prompt.float(rel_x)
