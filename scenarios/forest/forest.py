import pygame

from gi.repository import Gtk
from scenarios.utils import utils
from scenarios.utils import consts
from scenarios.utils import saves
from scenarios.utils.button import Button
from actors.player import Player
from actors.prompt import Prompt

class Forest:
    """
        Class representing the forest level, recieves
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
        self.character = "luis"
        self.background = utils.load_image("background.png", "forest")
        self.background_width = self.background.get_size()[0]
        self.foreground = utils.load_image("foreground.png", "forest")
        self.current_slide = 1
        self.prompts = {
            "bin": Prompt(self.screen,
                            self.clock,
                            (704, 440),
                            "prompt.png",
                            "",
                            (380, 475)),
            "special": Prompt(self.screen,
                              self.clock,
                              (1100, 430),
                              "prompt.png",
                              "",
                              (330, 460)),
            "hole": Prompt(self.screen,
                           self.clock,
                           (1395, 500),
                           "prompt.png",
                           "",
                           (450, 540)),
            "ranger": Prompt(self.screen,
                           self.clock,
                           (1705, 345),
                           "prompt.png",
                           "",
                           (280, 380)),
            "logger": Prompt(self.screen,
                            self.clock,
                            (2870, 370),
                            "prompt.png",
                            "",
                            (290, 400)),
            "tools": Prompt(self.screen,
                            self.clock,
                            (3015, 430),
                            "prompt.png",
                            "",
                            (330, 460)),
            "dirt": Prompt(self.screen,
                            self.clock,
                            (3921, 480),
                            "prompt.png",
                            "",
                            (390, 510)),
            "trash": Prompt(self.screen,
                            self.clock,
                            (4217, 460),
                            "prompt.png",
                            "",
                            (360, 500))
        }
        self.props = {
            "special": utils.load_image("key_item.png", "forest"),
            "hole": utils.load_image("hole.png", "forest"),
            "ranger": utils.load_image("ranger.png", "forest"),
            "loggers": (utils.load_image("logger1.png", "forest"),
                      utils.load_image("logger2.png", "forest"),
                      utils.load_image("logger3.png", "forest")),
            "tools": utils.load_image("tools.png", "forest"),
            "dirt": utils.load_image("dirt.png", "forest"),
            "trash": utils.load_image("trash1.png", "forest"),
            "plant": utils.load_image("plant.png", "forest"),
        }

        self.hud = {
            "bg": utils.load_image("upper.png", ""),
            "bar": utils.load_image("bar.png", "HUD"),
            "bird_icon": Button((1053, 15),
                                "icon1.png",
                                "icon2.png",
                                136,
                                112,
                                "HUD",
                                flag=True),
            "bird_modal_1": utils.load_image("h1.png", "forest/HUD"),
            "exit_bird": utils.load_image("exit.png", "HUD"),
            "map_icon": Button((903, 15),
                               "map1.png",
                               "map2.png",
                               140,
                               108,
                               "HUD"),
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

        self.inventory = {
            "unfocused_bag": utils.load_image("bag1.png", "forest/HUD"),
            "focused_bag": utils.load_image("bag2.png", "forest/HUD"),
            "plant": utils.load_image("plant.png", "forest/HUD"),
            "dirt": utils.load_image("dirt.png", "forest/HUD"),
            "tools": utils.load_image("tools.png", "forest/HUD"),
            "trash": utils.load_image("trash.png", "forest/HUD")
        }

        self.stats = {
            "inv": {}, # the items the player has
            "flags": {
                "ranger": False, # have not talked at all
                "logger": False, # have not talked with logger
                "recycled": False, #trash is there
                "extinguished": False, #fire is not off
                "dirt": False, # dirt is displayed
                "hole": False, # hole is displayed
                "tools": False, # tools is displayed
                "plant": False # have not recieved plant
            }
        }

        self.dialogue = {
            "1": utils.load_image("d1.png", "forest/dialogue"), # motmot
            "2": utils.load_image("d2.png", "forest/dialogue"),
            "3": utils.load_image("d3.png", "forest/dialogue"),
            "4": utils.load_image("d4.png", "forest/dialogue"), # ranger
            "5": utils.load_image("d5.png", "forest/dialogue"),
            "6": utils.load_image("d6.png", "forest/dialogue"), # luis
            "7": utils.load_image("d7.png", "forest/dialogue"), # luis
            "8": utils.load_image("d8.png", "forest/dialogue"), # logger
            "9": utils.load_image("d9.png", "forest/dialogue"), # luis
            "10": utils.load_image("d10.png", "forest/dialogue"), # logger
            "11": utils.load_image("d11.png", "forest/dialogue"), # motmot
            "12": utils.load_image("d12.png", "forest/dialogue"), # luis
            "13": utils.load_image("d13.png", "forest/dialogue"),
            "14": utils.load_image("d14.png", "forest/dialogue"), # ranger
            "15": utils.load_image("d15.png", "forest/dialogue"), # luis
            "16": utils.load_image("d16.png", "forest/dialogue") # motmot
        }

        self.icons = {
            "luis": utils.load_image("luis_icon.png", "forest"),
            "ranger": utils.load_image("ranger_icon.png", "forest"),
            "logger": utils.load_image("logger1_icon.png", "forest"),
            "motmot": utils.load_image("motmot_icon.png", "forest")
        }
        self.show_bird_modal = False
        self.show_map_modal = False
        self.player = Player(self.screen,
                              self.clock,
                             (150, 520),
                             self.character,
                             4800,
                             True)
        self.focus = "game"

        self.prev = Button((178, 703),
                           "prev1.png",
                           "prev2.png",
                           48,
                           42,
                           "forest")
        self.next = Button((1104, 703),
                           "next1.png",
                           "next2.png",
                           48,
                           42,
                           "forest")

    def run(self):
        utils.load_bg("shosta.ogg")
        pygame.mixer.music.set_volume(consts.BG_VOLUME)
        pygame.mixer.music.play(-1, 0.0)
        running = True
        while running:
            rel_x = self.player.stage["x"]
            if rel_x < consts.WIDTH_SCREEN:
                self.screen.blit(self.background, (rel_x, -100))

                if self.stats["flags"]["hole"]:
                    self.screen.blit(self.props["special"], (1085-abs(rel_x), 497))
                    self.screen.blit(self.props["plant"], (1392-abs(rel_x), 560))
                else:
                    self.screen.blit(self.props["hole"], (1391-abs(rel_x), 584))
                self.screen.blit(self.props["ranger"], (1681-abs(rel_x), 415))
                if not self.stats["flags"]["logger"]:
                    self.screen.blit(self.props["loggers"][0], (2857-abs(rel_x), 435))
                    self.screen.blit(self.props["loggers"][1], (3300-abs(rel_x), 383))
                    self.screen.blit(self.props["loggers"][2], (2581-abs(rel_x), 359))
                if not self.stats["flags"]["tools"]:
                    self.screen.blit(self.props["tools"], (2954-abs(rel_x), 495))
                if not self.stats["flags"]["dirt"]:
                    self.screen.blit(self.props["dirt"], (3790-abs(rel_x), 543))
                if not self.stats["flags"]["extinguished"]:
                    self.screen.blit(self.props["trash"], (4164-abs(rel_x), 450))
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
                        if self.current_slide == 17:
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
                        elif self.current_slide not in (1, 4, 7, 12, 13, 14, 16 ):
                            self.prev.on_press(self.screen)
                            self.current_slide -= 1
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                        if self.current_slide == 17:
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
                        elif self.current_slide in (1, 2, 4, 5, 7, 8, 9, 10, 14):
                            self.next.on_press(self.screen)
                            self.current_slide += 1
                        elif self.current_slide not in (1, 2, 4, 5, 7, 8,
                                                        9, 10, 14, 16):
                            self.next.on_press(self.screen)
                            self.current_slide = 17

                        elif self.current_slide == 16:
                            self.next.on_press(self.screen)
                            running = False
                            utils.loading_screen(self.screen)
                            #save here
                            if not self.slot["stages"]["bosque"] is True:
                                saves.save(7, "Bosque", "bosque")
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_KP2:
                        if self.current_slide == 17 and self.focus == "game":
                            self.player.direction = "down"
                            self.player.y_velocity = abs(self.player.y_velocity)
                    elif event.key == pygame.K_UP or event.key == pygame.K_KP8:
                        if self.current_slide == 17 and self.focus == "game":
                            self.player.direction = "up"
                            self.player.y_velocity = -abs(self.player.y_velocity)
                    elif event.key == pygame.K_RETURN or event.key == consts.K_CHECK:
                        if self.current_slide == 17 and self.focus == "game":
                            self.player.running = True
                    elif event.key == pygame.K_SPACE or event.key == consts.K_CROSS:
                        if self.current_slide == 17:
                            if self.focus == "game":
                                if (573 < self.player.real_x < 799
                                    and self.stats["flags"]["extinguished"]
                                    and "trash" in self.stats["inv"]):
                                    self.stats["flags"]["recycled"] = True
                                    self.stats["inv"] = {}
                                    self.current_slide = 12
                                if (957 < self.player.real_x < 1183
                                    and self.stats["flags"]["hole"]):
                                    pass
                                    self.current_slide = 16
                                if (1293 < self.player.real_x < 1463
                                    and not self.stats["flags"]["hole"]
                                    and "plant" in self.stats["inv"]):
                                    self.stats["flags"]["hole"] = True
                                    self.stats["inv"] = {}
                                if (1557 < self.player.real_x < 1804
                                    and (not self.stats["flags"]["ranger"])):
                                    self.stats["flags"]["ranger"] = True
                                    self.current_slide = 4
                                elif (1557 < self.player.real_x < 1804
                                      and (self.stats["flags"]["ranger"] and
                                            (not self.stats["flags"]["plant"]
                                             and self.stats["flags"]["recycled"]))):
                                      self.stats["flags"]["plant"] = True
                                      self.stats["inv"] = {"plant"}
                                      self.current_slide = 14
                                if (2671 < self.player.real_x < 2919
                                    and not self.stats["flags"]["logger"]):
                                    self.current_slide = 7
                                if (2918 < self.player.real_x < 3171
                                    and not self.stats["flags"]["tools"]):
                                      self.stats["flags"]["tools"] = True
                                      self.stats["inv"] = {"tools"}
                                if (3729 < self.player.real_x < 4067
                                    and not self.stats["flags"]["dirt"]
                                    and self.stats["flags"]["tools"]):
                                      self.stats["flags"]["dirt"] = True
                                      self.stats["inv"] = {"tools", "dirt"}
                                if (4013 < self.player.real_x < 4375
                                    and not self.stats["flags"]["extinguished"]
                                    and {"tools", "dirt"} == self.stats["inv"]):
                                      self.stats["flags"]["extinguished"] = True
                                      self.stats["flags"]["logger"] = True
                                      self.stats["inv"] = {"trash"}
                                      self.current_slide = 13

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
                        if self.current_slide == 17:
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
        if number == 17:
            self.actors_load(rel_x)
            self.screen.blit(self.foreground, (1427-rel_x, -100))
        elif number in (1, 16):
            self.player.update()
            self.screen.blit(self.foreground, (1427-rel_x, -100))
            self.screen.blit(self.icons["motmot"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.next.base, (1104, 703))
        elif number in (2, 3, 11):
            self.player.update()
            self.screen.blit(self.foreground, (1427-rel_x, -100))
            self.screen.blit(self.icons["motmot"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.prev.base, (178, 703))
            self.screen.blit(self.next.base, (1104, 703))
        elif number in (6, 9, 15):
            self.player.update()
            self.screen.blit(self.foreground, (1427-rel_x, -100))
            self.screen.blit(self.icons["luis"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.prev.base, (178, 703))
            self.screen.blit(self.next.base, (1104, 703))
        elif number in (7, 12, 13):
            #luis commenting on an item or initiating
            self.player.update()
            self.screen.blit(self.foreground, (1427-rel_x, -100))
            self.screen.blit(self.icons["luis"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.next.base, (1104, 703))
        elif number in (4, 14):
            #ranger initiating conversation
            self.player.update()
            self.screen.blit(self.foreground, (1427-rel_x, -100))
            self.screen.blit(self.icons["ranger"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.next.base, (1104, 703))
        elif number == 5:
            #ranger conversation
            self.player.update()
            self.screen.blit(self.foreground, (1427-rel_x, -100))
            self.screen.blit(self.icons["ranger"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.prev.base, (178, 703))
            self.screen.blit(self.next.base, (1104, 703))
        elif number in (8, 10):
            #logger conversation
            self.player.update()
            self.screen.blit(self.foreground, (1427-rel_x, -100))
            self.screen.blit(self.icons["logger"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.prev.base, (178, 703))
            self.screen.blit(self.next.base, (1104, 703))

    def actors_load(self, rel_x):
        if (573 < self.player.real_x < 799
            and self.stats["flags"]["extinguished"]
            and "trash" in self.stats["inv"]):
            self.prompts["bin"].float(rel_x)
        if (957 < self.player.real_x < 1183
            and self.stats["flags"]["hole"]):
            self.prompts["special"].float(rel_x)
        if (1293 < self.player.real_x < 1463
            and not self.stats["flags"]["hole"]
            and "plant" in self.stats["inv"]):
            self.prompts["hole"].float(rel_x)
        if (1557 < self.player.real_x < 1804
            and (not self.stats["flags"]["ranger"]
                 or (not self.stats["flags"]["plant"]
                     and self.stats["flags"]["recycled"]))):
            self.prompts["ranger"].float(rel_x)
        if (2671 < self.player.real_x < 2919
            and not self.stats["flags"]["logger"]):
            self.prompts["logger"].float(rel_x)
        if (2918 < self.player.real_x < 3171
            and not self.stats["flags"]["tools"]):
            self.prompts["tools"].float(rel_x)
        if (3729 < self.player.real_x < 4067
            and not self.stats["flags"]["dirt"]
            and self.stats["flags"]["tools"]):
            self.prompts["dirt"].float(rel_x)
        if (4013 < self.player.real_x < 4375
            and not self.stats["flags"]["extinguished"]
            and {"tools", "dirt"} == self.stats["inv"]):
            self.prompts["trash"].float(rel_x)
        self.player.update()

    def load_hud(self):
        #top icons
        if self.focus == "bar":
            self.screen.blit(self.hud["bg"], (0, 0))
        self.screen.blit(self.hud["bird_icon"].end, (1053, 15))
        self.screen.blit(self.hud["map_icon"].base, (903, 15))
        if self.show_bird_modal:
            self.screen.blit(self.hud["bird_modal_1"], (0, 0))
        if self.show_map_modal:
            self.screen.blit(self.hud["map_modal"], (367, 191))
            self.screen.blit(self.hud["yes"].base, (517, 429))
            self.screen.blit(self.hud["no"].end, (656, 429))

        #inventory
        self.screen.blit(self.hud["bar"], (1, 800))
        self.screen.blit(self.inventory["focused_bag"], (9, 805))
        if self.stats["inv"] == {"tools"}:
            self.screen.blit(self.inventory["tools"], (275, 813))
        elif self.stats["inv"] == {"tools", "dirt"}:
            self.screen.blit(self.inventory["tools"], (275, 813))
            self.screen.blit(self.inventory["dirt"], (430, 830))
        elif self.stats["inv"] == {"trash"}:
            self.screen.blit(self.inventory["trash"], (275, 819))
        elif self.stats["inv"] == {"plant"}:
            self.screen.blit(self.inventory["plant"], (275, 815))

        # self.screen.blit(self.inventory["tools"], (275, 813))
        # self.screen.blit(self.inventory["dirt"], (430, 830))
        # self.screen.blit(self.inventory["trash"], (550, 819))
        # self.screen.blit(self.inventory["plant"], (670, 815))
