import pygame

from gi.repository import Gtk
from scenarios.utils import utils
from scenarios.utils import consts
from scenarios.utils import saves
from scenarios.utils.button import Button
from scenarios.school import library
from actors.player import Player
from actors.prompt import Prompt

class School:
    """
        Class representing the School level, recieves
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
        self.character = "ena"
        self.background = utils.load_image("background.png", "school")
        self.background_width = self.background.get_size()[0]
        self.current_slide = 12
        self.prompts = {
            "npc1": Prompt(self.screen,
                            self.clock,
                            (523, 500),
                            "prompt.png",
                            "",
                            (400, 520)),
            "npc2": Prompt(self.screen,
                            self.clock,
                            (1142, 500),
                            "prompt.png",
                            "",
                            (380, 510)),
            "npc3": Prompt(self.screen,
                            self.clock,
                            (1901, 510),
                            "prompt.png",
                            "",
                            (380, 530)),
            "principal": Prompt(self.screen,
                             self.clock,
                             (2812, 440),
                             "prompt.png",
                             "",
                             (300, 480)),
            "library": Prompt(self.screen,
                           self.clock,
                           (3374, 375),
                           "prompt.png",
                           "",
                           (290, 480))
        }
        self.props = {
            "npc1": utils.load_image("npc1.png", "school"),
            "npc2": utils.load_image("npc2.png", "school"),
            "npc3": utils.load_image("npc3.png", "school"),
            "principal": utils.load_image("principal.png", "school")
        }

        self.hud = {
            "bar": utils.load_image("bar.png", "HUD"),
            "bird_icon": Button((1053, 15),
                                "icon1.png",
                                "icon2.png",
                                136,
                                112,
                                "HUD",
                                flag=True),
            "bird_modal_1": utils.load_image("h1.png", "school/HUD"),
            "exit_bird": utils.load_image("exit.png", "HUD"),
            "map_icon": Button((903, 15),
                               "map1.png",
                               "map2.png",
                               140,
                               108,
                               "HUD",
                               flag=True),
            "map_modal": utils.load_image("modal.png", "HUD"),
            "yes": Button((532, 449),
                          "yes1.png",
                          "yes2.png",
                          83,
                          56,
                          "HUD"),
            "no": Button((606, 449),
                         "no1.png",
                         "no2.png",
                         83,
                         56,
                         "HUD",
                         flag=True)
        }


        self.dialogue = {
            "1": utils.load_image("d1.png", "school/dialogue"), #ena
            "2": utils.load_image("d2.png", "school/dialogue"), #npc1
            "3": utils.load_image("d3.png", "school/dialogue"), #ena
            "4": utils.load_image("d4.png", "school/dialogue"), #npc1
            "5": utils.load_image("d5.png", "school/dialogue"), #ena
            "6": utils.load_image("d6.png", "school/dialogue"), #npc2
            "7": utils.load_image("d7.png", "school/dialogue"), #ena
            "8": utils.load_image("d8.png", "school/dialogue"), #npc3
            "9": utils.load_image("d9.png", "school/dialogue"), #ena
            "10": utils.load_image("d10.png", "school/dialogue"), #principal
            "11": utils.load_image("d11.png", "school/dialogue") #ena
        }

        self.icons = {
            "ena": utils.load_image("ena_icon.png", "school"),
            "npc1": utils.load_image("npc1_icon.png", "school"),
            "npc2": utils.load_image("npc2_icon.png", "school"),
            "npc3": utils.load_image("npc3_icon.png", "school"),
            "principal": utils.load_image("principal_icon.png", "school")
        }

        self.show_bird_modal = False
        self.show_map_modal = False
        self.player = Player(self.screen,
                              self.clock,
                             (150, 620),
                             self.character,
                             3600,
                             True,
                             limit_y=564)
        self.talked = [False, False, False, False]
        self.focus = "game"

        self.prev = Button((178, 703),
                           "prev1.png",
                           "prev2.png",
                           48,
                           42,
                           "school")
        self.next = Button((1104, 703),
                           "next1.png",
                           "next2.png",
                           48,
                           42,
                           "school")

    def run(self):
        utils.load_bg("talk.ogg")
        pygame.mixer.music.set_volume(consts.BG_VOLUME)
        pygame.mixer.music.play(-1, 0.0)
        running = True
        while running:
            rel_x = self.player.stage["x"]
            if rel_x < consts.WIDTH_SCREEN:
                self.screen.blit(self.background, (rel_x, 0))
                self.screen.blit(self.props["npc1"], (517-abs(rel_x), 554))
                self.screen.blit(self.props["npc2"], (1130-abs(rel_x), 554))
                self.screen.blit(self.props["npc3"], (1902-abs(rel_x), 574))
                self.screen.blit(self.props["principal"], (2801-abs(rel_x), 520))
                self.render_scene(self.current_slide, abs(rel_x))
                self.load_hud()
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
                        if self.current_slide == 12:
                            if self.focus == "game":
                                self.player.direction = "left"
                                self.player.running_velocity = -abs(self.player.running_velocity)
                                self.player.velocity = -abs(self.player.velocity)
                            elif self.focus == "bar":
                                if self.show_map_modal:
                                    if self.hud["no"].flag:
                                        self.hud["no"].flag = False
                                        self.hud["yes"].flag = True
                                        self.hud["no"].on_focus(self.screen)
                                        self.hud["yes"].on_focus(self.screen)
                                else:
                                    if self.hud["bird_icon"].flag:
                                        self.hud["bird_icon"].flag = False
                                        self.hud["map_icon"].flag = True
                                        self.hud["bird_icon"].on_focus(self.screen)
                                        self.hud["map_icon"].on_focus(self.screen)
                        elif self.current_slide not in (1, 5, 7, 9):
                            self.prev.on_press(self.screen)
                            self.current_slide -= 1
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                        if self.current_slide == 12:
                            if self.focus == "game":
                                self.player.direction = "right"
                                self.player.running_velocity = abs(self.player.running_velocity)
                                self.player.velocity = abs(self.player.velocity)
                            elif self.focus == "bar":
                                if self.show_map_modal:
                                    if self.hud["yes"].flag:
                                        self.hud["yes"].flag = False
                                        self.hud["no"].flag = True
                                        self.hud["yes"].on_focus(self.screen)
                                        self.hud["no"].on_focus(self.screen)
                                else:
                                    if self.hud["map_icon"].flag:
                                        self.hud["map_icon"].flag = False
                                        self.hud["bird_icon"].flag = True
                                        self.hud["map_icon"].on_focus(self.screen)
                                        self.hud["bird_icon"].on_focus(self.screen)
                        elif self.current_slide in (1, 2, 3, 5, 7, 9, 10, 11):
                            self.next.on_press(self.screen)
                            self.current_slide +=1
                        elif self.current_slide in (4, 6, 8):
                            self.next.on_press(self.screen)
                            self.current_slide = 12
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_KP2:
                        if self.current_slide == 12 and self.focus == "game":
                            self.player.direction = "down"
                            self.player.y_velocity = abs(self.player.y_velocity)
                    elif event.key == pygame.K_UP or event.key == pygame.K_KP8:
                        if self.current_slide == 12 and self.focus == "game":
                            self.player.direction = "up"
                            self.player.y_velocity = -abs(self.player.y_velocity)
                    elif event.key == pygame.K_RETURN or event.key == consts.K_CHECK:
                        if self.current_slide == 12 and self.focus == "game":
                            self.player.running = True
                    elif event.key == pygame.K_SPACE or event.key == consts.K_CROSS:
                        if self.current_slide == 12:
                            if self.focus == "game":
                                if (396 < self.player.real_x < 676):
                                    self.current_slide = 1
                                    self.talked[0] = True
                                if (998 < self.player.real_x < 1194):
                                    self.current_slide = 5
                                    self.talked[1] = True
                                if (1788 < self.player.real_x < 1984):
                                    self.current_slide = 7
                                    self.talked[2] = True
                                if (2716 < self.player.real_x < 2884):
                                    self.current_slide = 9
                                    self.talked[3] = True
                                if (3219 < self.player.real_x < 3601) and all(self.talked):
                                    utils.loading_screen(self.screen)
                                    lib = library.Library(self.screen, self.clock)
                                    lib.run()
                                    del lib
                                    running = False
                                    utils.loading_screen(self.screen)
                                    #save here
                                    if not self.slot["stages"]["escuela"] is True:
                                        saves.save(2, "Escuela de Tololapa", "escuela")


                            elif self.focus == "bar":
                                if self.show_map_modal:
                                    if self.hud["yes"].flag:
                                        running = False
                                    elif self.hud["no"].flag:
                                        self.focus = "game"
                                        self.show_bird_modal = False
                                        self.show_map_modal = False
                                else:
                                    if self.hud["bird_icon"].flag:
                                        self.show_bird_modal = True
                                    elif self.hud["map_icon"].flag:
                                        self.show_map_modal = True


                    elif event.key == pygame.K_ESCAPE or event.key == consts.K_CIRCLE:
                        if self.current_slide == 12:
                            self.show_bird_modal = False
                            self.show_map_modal = False
                            if self.focus == "game":
                                self.focus = "bar"
                            elif self.focus == "bar":
                                self.focus = "game"

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_KP4:
                        self.player.direction = "stand"
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                        self.player.direction = "stand"
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_KP2:
                        self.player.direction = "stand"
                    elif event.key == pygame.K_UP or event.key == pygame.K_KP8:
                        self.player.direction = "stand"
                    elif event.key == pygame.K_RETURN or event.key == consts.K_CHECK:
                        self.player.running = False

    def render_scene(self, number, rel_x):
        if number == 12:
            self.actors_load(rel_x)
        elif number in (1, 5, 7, 9):
            self.player.update()
            self.screen.blit(self.icons["ena"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.next.base, (1104, 703))
        elif number in (3, 11):
            self.player.update()
            self.screen.blit(self.icons["ena"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.prev.base, (178, 703))
            self.screen.blit(self.next.base, (1104, 703))
        elif number in (2, 4):
            self.player.update()
            self.screen.blit(self.icons["npc1"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.prev.base, (178, 703))
            self.screen.blit(self.next.base, (1104, 703))
        elif number == 6:
            self.player.update()
            self.screen.blit(self.icons["npc2"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.prev.base, (178, 703))
            self.screen.blit(self.next.base, (1104, 703))
        elif number == 8:
            self.player.update()
            self.screen.blit(self.icons["npc3"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.prev.base, (178, 703))
            self.screen.blit(self.next.base, (1104, 703))
        elif number == 10:
            self.player.update()
            self.screen.blit(self.icons["principal"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.prev.base, (178, 703))
            self.screen.blit(self.next.base, (1104, 703))

    def actors_load(self, rel_x):
        if (396 < self.player.real_x < 676):
            self.prompts["npc1"].float(rel_x)
        if (998 < self.player.real_x < 1194):
            self.prompts["npc2"].float(rel_x)
        if (1788 < self.player.real_x < 1984):
            self.prompts["npc3"].float(rel_x)
        if (2716 < self.player.real_x < 2884):
            self.prompts["principal"].float(rel_x)
        if (3219 < self.player.real_x < 3601) and all(self.talked):
            self.prompts["library"].float(rel_x)
        self.player.update()

    def load_hud(self):
        #top icons
        self.screen.blit(self.hud["bird_icon"].end, (1053, 15))
        self.screen.blit(self.hud["map_icon"].base, (903, 15))
        if self.show_bird_modal:
            self.screen.blit(self.hud["bird_modal_1"], (0, 0))
        if self.show_map_modal:
            self.screen.blit(self.hud["map_modal"], (367, 191))
            self.screen.blit(self.hud["yes"].base, (517, 429))
            self.screen.blit(self.hud["no"].end, (656, 429))
