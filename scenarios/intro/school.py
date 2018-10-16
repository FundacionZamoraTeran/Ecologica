import sys
import pygame

from gi.repository import Gtk
from scenarios.utils import utils
from scenarios.utils import consts
from scenarios.utils.button import Button
from scenarios.intro import classroom
from actors.ena import Ena
from actors.wall import Wall
from actors.prompt import Prompt


class School:
    """
        Class representing the road to school part, recieves
        a Surface as a screen, and a Clock as clock
    """
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.fx_channel = pygame.mixer.Channel(0)
        self.fx_channel.set_volume(consts.FX_VOLUME)
        self.vx_channel = pygame.mixer.Channel(1)
        self.vx_channel.set_volume(consts.VX_VOLUME)
        self.character = "ena/prologue"
        self.background = utils.load_image("background.png", "intro/screen_4")
        self.current_scene = 1

        self.dialogue = {
            "1": utils.load_image("d1.png", "intro/screen_4/dialogue"),
            "2": utils.load_image("d2.png", "intro/screen_4/dialogue")
        }

        self.voices = {
            "1": utils.load_vx("intro/screen_4/1.ogg"),
            "2": utils.load_vx("intro/screen_4/2.ogg")
        }

        self.npc = {
            "sprite": utils.load_image("npc.png", "intro/screen_4"),
            "icon": utils.load_image("npc_icon.png", "intro/screen_4")
        }

        self.prompts = {
            "npc": Prompt(self.screen,
                          self.clock,
                          (510, 200),
                          "prompt.png",
                          "",
                          (200, 300)),
            "exit": Prompt(self.screen,
                             self.clock,
                             (970, 56),
                             "prompt.png",
                             "",
                             (30, 220))
        }

        self.wall_list = pygame.sprite.Group()
        self.wall_1 = Wall(self.screen,
                           self.clock,
                           (0, 0),
                           "1.png",
                           "intro/screen_4/walls")
        self.wall_2 = Wall(self.screen,
                           self.clock,
                           (463, 0),
                           "2.png",
                           "intro/screen_4/walls")
        self.wall_3 = Wall(self.screen,
                           self.clock,
                           (771, 0),
                           "3.png",
                           "intro/screen_4/walls")
        self.wall_4 = Wall(self.screen,
                           self.clock,
                           (0, 661),
                           "4.png",
                           "intro/screen_4/walls")
        self.wall_5 = Wall(self.screen,
                           self.clock,
                           (535, 520),
                           "5.png",
                           "intro/screen_4/walls")
        self.wall_6 = Wall(self.screen,
                           self.clock,
                           (867, 0),
                           "6.png",
                           "intro/screen_4/walls")

        self.wall_list.add(self.wall_1,
                           self.wall_2,
                           self.wall_3,
                           self.wall_4,
                           self.wall_5,
                           self.wall_6)

        self.player = Ena(self.screen,
                          self.clock,
                          (290, 510),
                          self.character)
        self.player.walls = self.wall_list

        self.played = [0, 0]

        self.prev = Button((260, 733),
                          "prev1.png",
                          "prev2.png",
                          48,
                          42,
                          "intro")
        self.next = Button((1058, 733),
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
            self.wall_list.update()
            self.screen.blit(self.background, (0, 0))
            self.render_scene()
            self.player.walls = self.wall_list
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
                        if self.current_scene == 1:
                            self.player.direction = "left"
                            self.player.velocity = -abs(self.player.velocity)
                        elif self.current_scene == 3:
                            self.prev.on_press(self.screen)
                            self.current_scene -= 1
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                        if self.current_scene == 1:
                            self.player.direction = "right"
                            self.player.velocity = abs(self.player.velocity)
                        elif self.current_scene == 2:
                            self.current_scene += 1
                            self.next.on_press(self.screen)
                        elif self.current_scene == 3:
                            self.current_scene = 1
                            self.next.on_press(self.screen)
                    elif event.key == pygame.K_SPACE or event.key == consts.K_CROSS:
                        if self.current_scene == 1:
                            if (457 < self.player.rect.x < 598) and (340 < self.player.rect.y < 399):
                                self.current_scene = 2
                            elif 766 < self.player.rect.x < 1201:
                                utils.loading_screen(self.screen)
                                cla = classroom.Classroom(self.screen, self.clock)
                                cla.run()
                                del cla
                                running = False

                    elif event.key == pygame.K_DOWN or event.key == pygame.K_KP2:
                        self.player.direction = "down"
                        self.player.y_velocity = abs(self.player.y_velocity)
                    elif event.key == pygame.K_UP or event.key == pygame.K_KP8:
                        self.player.direction = "up"
                        self.player.y_velocity = -abs(self.player.y_velocity)

                elif event.type == pygame.KEYUP:
                    if self.current_scene == 1:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_KP4:
                            self.player.direction = "stand"
                        elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                            self.player.direction = "stand"
                        elif event.key == pygame.K_DOWN or event.key == pygame.K_KP2:
                            self.player.direction = "stand"
                        elif event.key == pygame.K_UP or event.key == pygame.K_KP8:
                            self.player.direction = "stand"
    def render_scene(self):
        if self.current_scene == 1:
            self.vx_channel.stop()
            if (457 < self.player.rect.x < 598) and (340 < self.player.rect.y < 399):
                self.prompts["npc"].float(0)
            elif 766 < self.player.rect.x < 1201:
                self.prompts["exit"].float(0)
            self.actors_load()
        elif self.current_scene == 2:
            if self.played[0] == 0:
                self.vx_channel.stop()
                self.vx_channel.play(self.voices["1"])
                self.played[0] = 1
                self.played[1] = 0
            self.actors_load()
            self.screen.blit(self.dialogue["1"],(210, 678))
            self.screen.blit(self.npc["icon"], (68, 721))
            self.screen.blit(self.next.base, (1058, 733))
        elif self.current_scene == 3:
            if self.played[1] == 0:
                self.vx_channel.stop()
                self.vx_channel.play(self.voices["2"])
                self.played[0] = 0
                self.played[1] = 1
            self.actors_load()
            self.screen.blit(self.dialogue["2"], (210, 678))
            self.screen.blit(self.npc["icon"], (68, 721))
            self.screen.blit(self.prev.base, (260, 733))
            self.screen.blit(self.next.base, (1058, 733))

    def actors_load(self):
        self.screen.blit(self.npc["sprite"], (502, 326))
        self.player.update()
