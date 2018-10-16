import sys
import pygame

from gi.repository import Gtk
from scenarios.utils import utils
from scenarios.utils import consts
from scenarios.utils.button import Button
from scenarios.intro import city
from actors.ena import Ena
from actors.wall import Wall
from actors.prompt import Prompt


class Walk:
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
        self.background = utils.load_image("background.png", "intro/screen_2")
        self.background_width = self.background.get_size()[0]
        self.current_scene = 1

        self.dialogue = {
            "1": utils.load_image("d1.png", "intro/screen_2/dialogue"),
            "2": utils.load_image("d2.png", "intro/screen_2/dialogue"),
            "3": utils.load_image("d3.png", "intro/screen_2/dialogue"),
            "4": utils.load_image("d4.png", "intro/screen_2/dialogue")
        }

        self.voices = {
            "1": utils.load_vx("intro/screen_2/1.ogg"),
            "2": utils.load_vx("intro/screen_2/2.ogg"),
            "3": utils.load_vx("intro/screen_2/3.ogg"),
            "4": utils.load_vx("intro/screen_2/4.ogg")
        }

        self.ezer = {
            "sprite": utils.load_image("ezer.png", "intro/screen_2"),
            "icon":utils.load_image("ezer_icon.png", "intro/screen_2")}

        self.npc = {
            "sprite": utils.load_image("npc.png", "intro/screen_2"),
            "icon": utils.load_image("npc_icon.png", "intro/screen_2")
        }

        self.prompts = {
            "ezer": Prompt(self.screen,
                           self.clock,
                           (883, 230),
                           "prompt.png",
                           "",
                           (230, 300)),
            "npc": Prompt(self.screen,
                          self.clock,
                          (1826, 429),
                          "prompt.png",
                          "",
                          (330, 440)),
            "exit": Prompt(self.screen,
                           self.clock,
                           (2341, 40),
                           "prompt.png",
                           "",
                           (30, 120))
        }

        self.wall_list = pygame.sprite.Group()
        self.wall_1 = Wall(self.screen,
                           self.clock,
                           (0, 0),
                           "1.png",
                           "intro/screen_2/walls")
        self.wall_2 = Wall(self.screen,
                           self.clock,
                           (0, 479),
                           "2.png",
                           "intro/screen_2/walls")
        self.wall_3 = Wall(self.screen,
                           self.clock,
                           (352, 0),
                           "3.png",
                           "intro/screen_2/walls")
        self.wall_4 = Wall(self.screen,
                           self.clock,
                           (857, 144),
                           "4.png",
                           "intro/screen_2/walls")
        self.wall_5 = Wall(self.screen,
                           self.clock,
                           (352, 365),
                           "5.png",
                           "intro/screen_2/walls")
        self.wall_6 = Wall(self.screen,
                           self.clock,
                           (857, 517),
                           "6.png",
                           "intro/screen_2/walls")
        self.wall_7 = Wall(self.screen,
                           self.clock,
                           (1114, 0),
                           "7.png",
                           "intro/screen_2/walls")
        self.wall_8 = Wall(self.screen,
                           self.clock,
                           (1414, 0),
                           "8.png",
                           "intro/screen_2/walls")
        self.wall_9 = Wall(self.screen,
                           self.clock,
                           (1728, 0),
                           "9.png",
                           "intro/screen_2/walls")
        self.wall_10 = Wall(self.screen,
                            self.clock,
                            (1837, 241),
                            "10.png",
                            "intro/screen_2/walls")
        self.wall_11 = Wall(self.screen,
                            self.clock,
                            (2037, 0),
                            "11.png",
                            "intro/screen_2/walls")
        self.wall_12 = Wall(self.screen,
                            self.clock,
                            (1611, 828),
                            "12.png",
                            "intro/screen_2/walls")
        self.wall_13 = Wall(self.screen,
                            self.clock,
                            (1833, 670),
                            "13.png",
                            "intro/screen_2/walls")
        self.wall_14 = Wall(self.screen,
                            self.clock,
                            (2274, 250),
                            "14.png",
                            "intro/screen_2/walls")
        self.wall_list.add(self.wall_1,
                           self.wall_2,
                           self.wall_3,
                           self.wall_4,
                           self.wall_5,
                           self.wall_6,
                           self.wall_7,
                           self.wall_8,
                           self.wall_9,
                           self.wall_10,
                           self.wall_11,
                           self.wall_12,
                           self.wall_13,
                           self.wall_14)

        self.player = Ena(self.screen,
                          self.clock,
                          (290, 610),
                          self.character,
                          2400,
                          True)
        self.player.walls = self.wall_list
        self.played = [0, 0, 0, 0]

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
            rel_x = self.player.stage["x"]
            if rel_x < consts.WIDTH_SCREEN:
                self.wall_list.update(abs(rel_x))
                self.screen.blit(self.background, (rel_x, 0))
                self.render_scene(abs(rel_x))
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
                        elif self.current_scene == 3 or self.current_scene == 5:
                            self.prev.on_press(self.screen)
                            self.current_scene -= 1
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                        if self.current_scene == 1:
                            self.player.direction = "right"
                            self.player.velocity = abs(self.player.velocity)
                        elif self.current_scene == 2 or self.current_scene == 4:
                            self.current_scene += 1
                            self.next.on_press(self.screen)
                        elif self.current_scene == 3 or self.current_scene == 5:
                            self.current_scene = 1
                            self.next.on_press(self.screen)
                    elif event.key == pygame.K_SPACE or event.key == consts.K_CROSS:
                        if self.current_scene == 1:
                            if 793 < self.player.real_x < 991:
                                self.current_scene = 2
                            elif ((1717 < self.player.real_x < 1887)
                                  and (469 < self.player.rect.y < 611)):
                                self.current_scene = 4
                            elif 2305 < self.player.real_x < 2401:
                                utils.loading_screen(self.screen)
                                cit = city.City(self.screen, self.clock)
                                cit.run()
                                del cit
                                running = False

                    elif event.key == pygame.K_DOWN or event.key == pygame.K_KP2:
                        if self.current_scene == 1:
                            self.player.direction = "down"
                            self.player.y_velocity = abs(self.player.y_velocity)
                    elif event.key == pygame.K_UP or event.key == pygame.K_KP8:
                        if self.current_scene == 1:
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
    def render_scene(self, rel_x):
        if self.current_scene == 1:
            self.vx_channel.stop()
            if 793 < self.player.real_x < 991:
                self.prompts["ezer"].float(rel_x)
            elif (1717 < self.player.real_x < 1887) and (469 < self.player.rect.y < 611):
                self.prompts["npc"].float(rel_x)
            elif 2305 < self.player.real_x < 2401:
                self.prompts["exit"].float(rel_x)
            self.actors_load(rel_x)
        elif self.current_scene == 2:
            if self.played[0] == 0:
                self.vx_channel.stop()
                self.vx_channel.play(self.voices["1"])
                self.played[0] = 1
                self.played[1] = 0
            self.actors_load(rel_x)
            self.screen.blit(self.dialogue["1"],(210, 678))
            self.screen.blit(self.ezer["icon"], (68, 721))
            self.screen.blit(self.next.base, (1058, 733))
        elif self.current_scene == 3:
            if self.played[1] == 0:
                self.vx_channel.stop()
                self.vx_channel.play(self.voices["2"])
                self.played[0] = 0
                self.played[1] = 1
            self.actors_load(rel_x)
            self.screen.blit(self.dialogue["2"],(210, 678))
            self.screen.blit(self.ezer["icon"], (68, 721))
            self.screen.blit(self.prev.base, (260, 733))
            self.screen.blit(self.next.base, (1058, 733))
        elif self.current_scene == 4:
            if self.played[2] == 0:
                self.vx_channel.stop()
                self.vx_channel.play(self.voices["3"])
                self.played[2] = 1
                self.played[3] = 0
            self.actors_load(rel_x)
            self.screen.blit(self.dialogue["3"],(210, 678))
            self.screen.blit(self.npc["icon"], (68, 721))
            self.screen.blit(self.next.base, (1058, 733))
        elif self.current_scene == 5:
            if self.played[3] == 0:
                self.vx_channel.stop()
                self.vx_channel.play(self.voices["4"])
                self.played[2] = 0
                self.played[3] = 1
            self.actors_load(rel_x)
            self.screen.blit(self.dialogue["4"],(210, 678))
            self.screen.blit(self.npc["icon"], (68, 721))
            self.screen.blit(self.prev.base, (260, 733))
            self.screen.blit(self.next.base, (1058, 733))

    def actors_load(self, rel_x):
        self.screen.blit(self.ezer["sprite"], (879-rel_x, 326))
        self.screen.blit(self.npc["sprite"], (1817-rel_x, 451))
        self.player.update()
