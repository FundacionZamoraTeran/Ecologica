import pygame

from gi.repository import Gtk
from scenarios.utils import utils
from scenarios.utils import consts
from scenarios.utils import saves
from scenarios.utils.button import Button
from actors.player import Player
from actors.prompt import Prompt


class River:
    """
        Class representing the River level, recieves
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
        self.font = utils.load_font("fedra.otf", 20)
        self.next_level = "m"
        self.character = "ezer"
        self.background = utils.load_image("background.png", "river")
        self.background_width = self.background.get_size()[0]
        self.current_slide = 1
        self.prompts = {
            "money": Prompt(self.screen,
                            self.clock,
                            (523, 480),
                            "prompt.png",
                            "",
                            (400, 600)),
            "net": Prompt(self.screen,
                          self.clock,
                          (601, 480),
                          "prompt.png",
                          "",
                          (400, 500)),
            "logger": Prompt(self.screen,
                             self.clock,
                             (2445, 380),
                             "prompt.png",
                            "",
                             (250, 400)),
            "cabin": Prompt(self.screen,
                            self.clock,
                            (3470, 480),
                            "prompt.png",
                            "",
                            (400, 600)),
            "owner": Prompt(self.screen,
                            self.clock,
                            (3740, 380),
                            "prompt.png",
                            "",
                            (250, 400)),
            "trash":  Prompt(self.screen,
                             self.clock,
                             (4383, 580),
                             "prompt.png",
                             "",
                             (500, 680)),
            "fish":  Prompt(self.screen,
                            self.clock,
                            (5539, 480),
                            "prompt.png",
                            "",
                            (400, 600)),
            "purifier":  Prompt(self.screen,
                                self.clock,
                                (6130, 480),
                                "prompt.png",
                                "",
                                (400, 600)),
            "glass":  Prompt(self.screen,
                                self.clock,
                                (7132, 380),
                                "prompt.png",
                                "",
                                (350, 450)),
            "guard":  Prompt(self.screen,
                             self.clock,
                             (8950, 380),
                             "prompt.png",
                             "",
                             (350, 450)),
            "special": Prompt(self.screen,
                            self.clock,
                            (9062, 480),
                            "prompt.png",
                            "",
                            (400, 600))
        }
        self.props = {
            "river": utils.load_image("good_river.png", "river"),
            "logger": (utils.load_image("logger1.png", "river"),
                       utils.load_image("logger2.png", "river")),
            "turbine": utils.load_image("turbine.png", "river"),
            "money": utils.load_image("money.png", "river"),
            "net": utils.load_image("net.png", "river"),
            "stumps": utils.load_image("stumps.png", "river"),
            "cabin": (utils.load_image("base.png", "river/cabin"),
                      utils.load_image("open.png", "river/cabin"),
                      utils.load_image("inside.png", "river/cabin")),
            "owner": utils.load_image("owner.png", "river"),
            "bridge": (utils.load_image("base.png", "river/bridge"),
                       utils.load_image("repaired.png", "river/bridge")),
            "handrail": utils.load_image("handrail.png", "river/bridge"),
            "trash": utils.load_image("trash.png", "river"),
            "trash2": utils.load_image("trash2.png", "river"),
            "canoe": utils.load_image("canoe.png", "river"),
            "trees": (utils.load_image("tree_1.png", "river"),
                      utils.load_image("tree_2.png", "river"),
                      utils.load_image("tree_3.png", "river")),
            "fish": utils.load_image("0.png", "river/fish"),
            "purifier": (utils.load_image("base.png", "river/purifier"),
                         utils.load_image("open.png", "river/purifier"),
                         utils.load_image("inside.png", "river/purifier")),
            "cover": utils.load_image("over.png", "river/purifier"),
            "fence": (utils.load_image("closed.png", "river/fence"),
                      utils.load_image("open.png", "river/fence")),
            "glass": utils.load_image("full.png", "river/glass"),
            "special": utils.load_image("key_item.png", "river"),
            "guard": utils.load_image("guard.png", "river")
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
            "counter": utils.load_image("counter.png", "HUD"),
            "bird_modal_1": utils.load_image("h1.png", "river/HUD"),
            "bird_modal_2": utils.load_image("h2.png", "river/HUD"),
            "bird_modal_3": utils.load_image("h3.png", "river/HUD"),
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
            "unfocused_bag": utils.load_image("bag1.png", "river/HUD"),
            "focused_bag": utils.load_image("bag2.png", "river/HUD"),
            "money": utils.load_image("money.png", "river/HUD"),
            "net": utils.load_image("net.png", "river/HUD"),
            "axe": utils.load_image("axe.png", "river/HUD"),
            "wood": utils.load_image("wood.png", "river/HUD"),
            "fishing_rod": utils.load_image("fishing_rod.png", "river/HUD"),
            "fish": utils.load_image("fish.png", "river/HUD"),
            "key": utils.load_image("key.png", "river/HUD"),
            "glass": utils.load_image("glass.png", "river/HUD"),
            "selector": utils.load_image("selector.png", "river/HUD")
        }

        self.stats = {
            "inv": {}, # the items the player has
            "flags": {
                "money": False, # the item is visible on map
                "net": False, # the item is visible on map
                "logger": False, # not with his full axe
                "cabin": False, #is not showing inside
                "bridge": False, # is not repaired
                "trash": False, # Trash on river not cleaned
                "fishing": False,
                "fished": False, # have not caught the fish
                "open": False, # the purifying plant is closed
                "purifier": False, # is not showing inside
                "purified": False, # river is not pure yet
                "picked": False, #glass is on the ground
                "glass": False # the is guard not refreshed 
            }
        }

        self.dialogue = {
            "1": utils.load_image("d1.png", "river/dialogue"),#parrot
            "2": utils.load_image("d2.png", "river/dialogue"),
            "3": utils.load_image("d3.png", "river/dialogue"),
            "4": utils.load_image("d4.png", "river/dialogue"), #ezer
            "5": utils.load_image("d5.png", "river/dialogue"),
            "6": utils.load_image("d6.png", "river/dialogue"),
            "7": utils.load_image("d7.png", "river/dialogue"), #logger
            "8": utils.load_image("d8.png", "river/dialogue"), #ezer
            "9": utils.load_image("d9.png", "river/dialogue"), #logger
            "10": utils.load_image("d10.png", "river/dialogue"), #ezer
            "11": utils.load_image("d11.png", "river/dialogue"), #logger
            "12": utils.load_image("d12.png", "river/dialogue"), #ezer
            "13": utils.load_image("d13.png", "river/dialogue"),
            "14": utils.load_image("d14.png", "river/dialogue"),
            "15": utils.load_image("d15.png", "river/dialogue"),
            "16": utils.load_image("d16.png", "river/dialogue"), #logger
            "17": utils.load_image("d17.png", "river/dialogue"), #ezer
            "18": utils.load_image("d18.png", "river/dialogue"), #logger
            "19": utils.load_image("d19.png", "river/dialogue"), #owner
            "20": utils.load_image("d20.png", "river/dialogue"), #ezer
            "21": utils.load_image("d21.png", "river/dialogue"), #owner
            "22": utils.load_image("d22.png", "river/dialogue"), #ezer
            "23": utils.load_image("d23.png", "river/dialogue"),
            "24": utils.load_image("d24.png", "river/dialogue"),
            "25": utils.load_image("d25.png", "river/dialogue"),  #owner
            "26": utils.load_image("d26.png", "river/dialogue"),
            "27": utils.load_image("d27.png", "river/dialogue"), #parrot
            "28": utils.load_image("d28.png", "river/dialogue"),
            "29": utils.load_image("d29.png", "river/dialogue"),
            "30": utils.load_image("d30.png", "river/dialogue"), #guard
            "31": utils.load_image("d31.png", "river/dialogue"), #guard
            "32": utils.load_image("d32.png", "river/dialogue"), #ezer
            "33": utils.load_image("d33.png", "river/dialogue"),  #guard
            "34": utils.load_image("d34.png", "river/dialogue"), #parrot
            "35": utils.load_image("d35.png", "river/dialogue") #ezer
        }

        self.icons = {
            "ezer": utils.load_image("ezer_icon.png", "river"),
            "owner": utils.load_image("owner_icon.png", "river"),
            "logger": utils.load_image("logger_icon.png", "river"),
            "guard": utils.load_image("guard_icon.png", "river"),
            "parrot": utils.load_image("parrot_icon.png", "river")
        }
        self.show_bird_modal = False
        self.show_map_modal = False
        self.player = Player(self.screen,
                              self.clock,
                             (150, 620),
                             self.character,
                             9600,
                             True)
        self.focus = "game"

        self.prev = Button((178, 703),
                           "prev1.png",
                           "prev2.png",
                           48,
                           42,
                           "river")
        self.next = Button((1104, 703),
                           "next1.png",
                           "next2.png",
                           48,
                           42,
                           "river")

    def run(self):
        utils.load_bg("hungarian.ogg")
        pygame.mixer.music.set_volume(consts.BG_VOLUME)
        pygame.mixer.music.play(-1, 0.0)
        running = True
        while running:
            rel_x = self.player.stage["x"]
            if rel_x < consts.WIDTH_SCREEN:
                self.screen.blit(self.background, (rel_x, -100))
                self.load_items(abs(rel_x))
                self.screen.blit(self.props["turbine"], (72-abs(rel_x), 131))
                self.screen.blit(self.props["turbine"], (843-abs(rel_x), 181))
                self.screen.blit(self.props["turbine"], (2017-abs(rel_x), 161))
                self.screen.blit(self.props["turbine"], (3036-abs(rel_x), 181))
                if self.stats["flags"]["purified"] is True:
                    self.screen.blit(self.props["river"], (3804-abs(rel_x), 449))
                self.screen.blit(self.props["stumps"], (992-abs(rel_x), 432))
                if self.stats["flags"]["logger"] is True:
                    self.screen.blit(self.props["logger"][1], (2415-abs(rel_x), 405))
                    if self.stats["flags"]["cabin"] is True:
                        self.screen.blit(self.props["cabin"][2], (3240-abs(rel_x), 220))
                        self.screen.blit(self.props["owner"], (3712-abs(rel_x), 420))
                    else:
                        self.screen.blit(self.props["cabin"][1], (3240-abs(rel_x), 220))
                else:
                    self.screen.blit(self.props["logger"][0], (2415-abs(rel_x), 405))
                    self.screen.blit(self.props["cabin"][0], (3240-abs(rel_x), 220))
                if self.stats["flags"]["bridge"] is True:
                    self.screen.blit(self.props["bridge"][1], (4104-abs(rel_x), 482))
                else:
                    self.screen.blit(self.props["bridge"][0], (4104-abs(rel_x), 482))
                if self.stats["flags"]["trash"] is False:
                    self.screen.blit(self.props["trash2"], (4354-abs(rel_x), 622))
                    self.screen.blit(self.props["trash"], (4333-abs(rel_x), 678))
                self.screen.blit(self.props["canoe"], (4678-abs(rel_x), 650))
                self.screen.blit(self.props["trees"][0], (4673-abs(rel_x), -100))
                if self.stats["flags"]["fished"] is False:
                    self.screen.blit(self.props["fish"], (5539-abs(rel_x), 690))
                self.screen.blit(self.props["trees"][1], (5863-abs(rel_x), -100))
                if self.stats["flags"]["open"] is True:
                    if self.stats["flags"]["purifier"] is True:
                        self.screen.blit(self.props["purifier"][2], (6079-abs(rel_x), 183))
                    else:
                        self.screen.blit(self.props["purifier"][1], (6079-abs(rel_x), 183))
                else:
                    self.screen.blit(self.props["purifier"][0], (6079-abs(rel_x), 183))
                self.screen.blit(self.props["trees"][2], (7347-abs(rel_x), -100))
                if self.stats["flags"]["glass"] is True:
                    self.screen.blit(self.props["fence"][1], (8209-abs(rel_x), 398))
                    self.screen.blit(self.props["special"], (8815-abs(rel_x), 326))
                    self.screen.blit(self.props["guard"], (8820-abs(rel_x), 501))
                else:
                    self.screen.blit(self.props["fence"][0], (8209-abs(rel_x), 398))
                    self.screen.blit(self.props["special"], (8815-abs(rel_x), 326))
                    self.screen.blit(self.props["guard"], (8920-abs(rel_x), 501))
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
                        if self.current_slide == 36:
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
                        elif ((1 < self.current_slide < 5)
                              or (7 < self.current_slide < 12)
                              or (15 < self.current_slide < 19)
                              or (19 < self.current_slide < 23)
                              or 25 < self.current_slide < 28
                              or self.current_slide == 29
                              or 31 < self.current_slide < 34):
                            self.prev.on_press(self.screen)
                            self.current_slide -= 1
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                        if self.current_slide == 36:
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
                        elif ((self.current_slide < 4)
                              or (6 < self.current_slide <11)
                              or (14 < self.current_slide < 18)
                              or (18 < self.current_slide <22)
                              or (24 < self.current_slide < 27)
                              or self.current_slide == 28
                              or 30 < self.current_slide < 33):
                            self.next.on_press(self.screen)
                            self.current_slide +=1
                        elif ((3 < self.current_slide < 7)
                              or self.current_slide == 11
                              or (12 < self.current_slide < 15)
                              or self.current_slide == 18
                              or self.current_slide == 22
                              or (22 < self.current_slide < 25)
                              or self.current_slide == 27
                              or self.current_slide == 29
                              or self.current_slide == 30
                              or self.current_slide == 33
                              or self.current_slide == 35):
                            self.next.on_press(self.screen)
                            self.current_slide = 36
                        elif self.current_slide == 34:
                            running = False
                            utils.loading_screen(self.screen)
                            #save here
                            if not self.slot["stages"]["rio"] is True:
                                saves.save(6, "Rio Claro", "rio")
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_KP2:
                        if self.current_slide == 36 and self.focus == "game":
                            self.player.direction = "down"
                            self.player.y_velocity = abs(self.player.y_velocity)
                    elif event.key == pygame.K_UP or event.key == pygame.K_KP8:
                        if self.current_slide == 36 and self.focus == "game":
                            self.player.direction = "up"
                            self.player.y_velocity = -abs(self.player.y_velocity)
                    elif event.key == pygame.K_RETURN or event.key == consts.K_CHECK:
                        if self.current_slide == 36 and self.focus == "game":
                            self.player.running = True
                    elif event.key == pygame.K_SPACE or event.key == consts.K_CROSS:
                        if self.current_slide == 36:
                            if self.focus == "game":
                                if (self.player.real_x+self.player.rect.width > 500
                                        and self.player.real_x+self.player.rect.width < 553
                                        and not self.stats["flags"]["money"]):
                                    self.stats["flags"]["money"] = True
                                    self.stats["inv"] = {"money"}
                                    self.current_slide = 5
                                if (self.player.real_x+self.player.rect.width > 565
                                    and self.player.real_x+self.player.rect.width < 685
                                    and not self.stats["flags"]["net"]
                                    and "money" in self.stats["inv"]):
                                    self.stats["flags"]["net"] = True
                                    self.stats["inv"] = {"money", "net"}
                                    self.current_slide = 6
                                if (self.player.real_x+self.player.rect.width > 2400
                                    and self.player.real_x+self.player.rect.width < 2595
                                    and "axe" in self.stats["inv"]):
                                    self.current_slide = 15
                                    self.stats["flags"]["logger"] = True
                                    self.stats["inv"] = {"money", "wood"}
                                elif (self.player.real_x+self.player.rect.width > 2400
                                      and self.player.real_x+self.player.rect.width < 2595
                                      and self.stats["flags"]["logger"] is False):
                                    self.current_slide = 7
                                if (self.player.real_x+self.player.rect.width > 3390
                                    and self.player.real_x+self.player.rect.width < 3650
                                    and self.stats["flags"]["logger"]):
                                    self.stats["flags"]["cabin"] = True
                                elif (self.player.real_x+self.player.rect.width > 3390
                                    and self.player.real_x+self.player.rect.width < 3650
                                    and self.stats["flags"]["cabin"]):
                                    self.stats["flags"]["cabin"] = False

                                #the various interactions with the cabin owner
                                if (self.player.real_x+self.player.rect.width > 3700
                                    and self.player.real_x+self.player.rect.width < 3950
                                    and self.stats["flags"]["cabin"]
                                    and not self.stats["flags"]["bridge"]
                                    and not self.stats["flags"]["fished"]):
                                    self.current_slide = 19
                                    self.stats["flags"]["bridge"] = True
                                    self.stats["inv"] = {"fishing_rod"}
                                if (self.player.real_x+self.player.rect.width > 3700
                                    and self.player.real_x+self.player.rect.width < 3950
                                    and self.stats["flags"]["cabin"]
                                    and self.stats["flags"]["fished"]
                                    and not self.stats["flags"]["open"]
                                    and "key" not in self.stats["inv"]):
                                    self.current_slide = 25
                                    self.stats["inv"] = {"key"}

                                #trash state
                                if (self.player.real_x+self.player.rect.width > 4000
                                    and self.player.real_x+self.player.rect.width <= 4104
                                    and not self.stats["flags"]["trash"]
                                    and "net" in self.stats["inv"]):
                                    self.current_slide = 14
                                    self.stats["flags"]["trash"] = True
                                    self.stats["inv"] = {"money", "axe"}
                                elif (self.player.real_x+self.player.rect.width > 4000
                                      and self.player.real_x+self.player.rect.width <= 4104
                                      and not self.stats["flags"]["trash"]
                                      and "net" not in self.stats["inv"]):
                                    self.current_slide = 13

                                #fishing states
                                if (self.player.real_x+self.player.rect.width > 5480
                                    and self.player.real_x+self.player.rect.width < 5620
                                    and not self.stats["flags"]["fished"]
                                    and "fishing_rod" in self.stats["inv"]):
                                    self.current_slide = 24
                                    self.stats["flags"]["fished"] = True
                                    self.stats["inv"] = {"fishing_rod", "fish"}
                                elif (self.player.real_x+self.player.rect.width > 5480
                                    and self.player.real_x+self.player.rect.width < 5620
                                    and not self.stats["flags"]["fished"]
                                    and "fishing_rod" not in self.stats["inv"]):
                                    self.current_slide = 23
                                    self.stats["flags"]["fished"] = True
                                    self.stats["inv"] = {"fishing_rod", "fish"}

                                #purifier states
                                if (self.player.real_x+self.player.rect.width > 6018
                                    and self.player.real_x+self.player.rect.width < 6296
                                    and not self.stats["flags"]["open"]
                                    and "key" in self.stats["inv"]):
                                    self.stats["flags"]["open"] = True
                                elif (self.player.real_x+self.player.rect.width > 6018
                                    and self.player.real_x+self.player.rect.width < 6296
                                    and self.stats["flags"]["open"]
                                    and not self.stats["flags"]["purified"]):
                                    self.current_slide = 28
                                    self.stats["inv"] = {}
                                    self.stats["flags"]["purifier"] = True
                                    self.stats["flags"]["purified"] = True

                                if (self.player.real_x+self.player.rect.width > 7000
                                    and self.player.real_x+self.player.rect.width < 7316
                                    and not self.stats["flags"]["picked"]):
                                    self.current_slide = 35
                                    self.stats["flags"]["picked"] = True
                                    self.stats["inv"] = {"glass"}

                                #guard
                                if (self.player.real_x+self.player.rect.width > 8900
                                    and self.player.real_x+self.player.rect.width < 9080
                                    and not self.stats["flags"]["glass"]
                                    and "glass" in self.stats["inv"]):
                                    self.current_slide = 31
                                    self.stats["flags"]["glass"] = True
                                    self.stats["inv"] = {}
                                elif (self.player.real_x+self.player.rect.width > 8900
                                    and self.player.real_x+self.player.rect.width < 9080
                                    and not self.stats["flags"]["glass"]
                                    and "glass" not in self.stats["inv"]):
                                    self.current_slide = 30
                                if (self.player.real_x+self.player.rect.width > 9080
                                    and self.player.real_x+self.player.rect.width < 9200
                                    and self.stats["flags"]["glass"]):
                                    self.current_slide = 34
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
                        if self.current_slide == 36:
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
        if number == 36:
            self.actors_load(rel_x)
        elif number in (1, 28, 34) :
            self.player.update()
            self.screen.blit(self.icons["parrot"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.next.base, (1104, 703))
        elif (1 < number < 4) or number == 27 or number == 29:
            self.player.update()
            self.screen.blit(self.icons["parrot"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.prev.base, (178, 703))
            self.screen.blit(self.next.base, (1104, 703))
        elif number == 4:
            self.player.update()
            self.screen.blit(self.icons["ezer"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.prev.base, (178, 703))
            self.screen.blit(self.next.base, (1104, 703))
        elif ((4 < number < 7)
              or (12 < number < 15)
              or (22 < number < 25)
              or number == 35):
            #ezer commenting on an item
            self.player.update()
            self.screen.blit(self.icons["ezer"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.next.base, (1104, 703))
        elif number == 7: #logger initiating a conversation
            self.player.update()
            self.screen.blit(self.icons["logger"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.next.base, (1104, 703))
        elif number in (8, 10, 17, 20, 22, 32):
            self.player.update()
            self.screen.blit(self.icons["ezer"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.prev.base, (178, 703))
            self.screen.blit(self.next.base, (1104, 703))
        elif number in (9, 11, 16, 18):
            self.player.update()
            self.screen.blit(self.icons["logger"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.prev.base, (178, 703))
            self.screen.blit(self.next.base, (1104, 703))
        elif number == 15: #ezer initiating a conversation
            self.player.update()
            self.screen.blit(self.icons["ezer"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.next.base, (1104, 703))
        elif number in (19, 25):  #owner initiating a conversation
            self.player.update()
            self.screen.blit(self.icons["owner"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.next.base, (1104, 703))
        elif number in (21, 26):
            self.player.update()
            self.screen.blit(self.icons["owner"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.prev.base, (178, 703))
            self.screen.blit(self.next.base, (1104, 703))
        elif number in (30, 31):  #guard initiating a conversation
            self.player.update()
            self.screen.blit(self.icons["guard"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.next.base, (1104, 703))
        elif number == 33:
            self.player.update()
            self.screen.blit(self.icons["guard"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.prev.base, (178, 703))
            self.screen.blit(self.next.base, (1104, 703))


    def actors_load(self, rel_x):
        if (self.player.real_x+self.player.rect.width > 500
            and self.player.real_x+self.player.rect.width < 553
            and not self.stats["flags"]["money"]):
            self.prompts["money"].float(rel_x)
        if (self.player.real_x+self.player.rect.width > 565
            and self.player.real_x+self.player.rect.width < 685
            and not self.stats["flags"]["net"]
            and "money" in self.stats["inv"]):
            self.prompts["net"].float(rel_x)
        if (self.player.real_x+self.player.rect.width > 2400
            and self.player.real_x+self.player.rect.width < 2595
            and self.stats["flags"]["logger"] == False):
            self.prompts["logger"].float(rel_x)
        if (self.player.real_x+self.player.rect.width > 3390
            and self.player.real_x+self.player.rect.width < 3650
            and self.stats["flags"]["logger"]
            and self.stats["flags"]["cabin"] == False):
            self.prompts["cabin"].float(rel_x)
        if (self.player.real_x+self.player.rect.width > 3700
            and self.player.real_x+self.player.rect.width < 3950
            and self.stats["flags"]["cabin"]
            and (self.stats["flags"]["bridge"] == False or
                 ( self.stats["flags"]["fished"] and
                   not self.stats["flags"]["open"] and
                   "key" not in self.stats["inv"]))):
            self.prompts["owner"].float(rel_x)
        if (self.player.real_x+self.player.rect.width > 4000
            and self.player.real_x+self.player.rect.width <= 4104
            and not self.stats["flags"]["trash"]):
            self.prompts["trash"].float(rel_x)
        if (self.player.real_x+self.player.rect.width > 5480
            and self.player.real_x+self.player.rect.width < 5620
            and not self.stats["flags"]["fished"]):
            self.prompts["fish"].float(rel_x)
        if (self.player.real_x+self.player.rect.width > 6018
            and self.player.real_x+self.player.rect.width < 6296
            and "key" in self.stats["inv"]):
            self.prompts["purifier"].float(rel_x)
        if (self.player.real_x+self.player.rect.width > 7000
            and self.player.real_x+self.player.rect.width < 7316
            and not self.stats["flags"]["picked"]):
            self.prompts["glass"].float(rel_x)
        if (self.player.real_x+self.player.rect.width > 8900
            and self.player.real_x+self.player.rect.width < 9080
            and not self.stats["flags"]["glass"]):
            self.prompts["guard"].float(rel_x)
        if (self.player.real_x+self.player.rect.width > 9080
            and self.player.real_x+self.player.rect.width < 9200
            and self.stats["flags"]["glass"]):
            self.prompts["guard"].float(rel_x)
        if 4090 < self.player.real_x < 4790:
            self.player.rect.y = 444
        if 4790 < self.player.real_x < 7500:
            if self.player.rect.y > 500:
                self.player.rect.y = 500
        if 8554 < self.player.real_x:
            if self.player.rect.y < 492:
                self.player.rect.y = 492
        if self.player.real_x+self.player.rect.width > 4004 and self.stats["flags"]["bridge"] is False:
            if self.player.velocity > 0:
                self.player.stage["x"] = -3340
                self.player.real_x =  4004 -self.player.rect.width
        elif self.player.real_x+self.player.rect.width > 6158 and self.stats["flags"]["purifier"] is False:
            if self.player.velocity > 0:
                self.player.stage["x"] = -5632
                self.player.real_x =  6158
        self.player.update()
        self.screen.blit(self.props["handrail"], (4236-abs(rel_x), 548))
        if self.stats["flags"]["open"] is True:
            self.screen.blit(self.props["cover"], (6297-abs(rel_x), 184))

    def load_items(self, rel_x):
        if self.stats["flags"]["money"] is False:
            self.screen.blit(self.props["money"], (523-rel_x, 617))
        if self.stats["flags"]["net"] is False:
            self.screen.blit(self.props["net"], (565-rel_x, 528))
        if self.stats["flags"]["picked"] is False:
            self.screen.blit(self.props["glass"], (7132-rel_x, 528))

    def load_hud(self):
        #top icons
        if self.focus == "bar":
            self.screen.blit(self.hud["bg"], (0, 0))
        self.screen.blit(self.hud["bird_icon"].end, (1053, 15))
        # self.screen.blit(self.hud["counter"], (1082, 117))
        # text = self.font.render(str(self.slot["coins"]),True, (255, 255, 255))
        # self.screen.blit(text, (1130, 126))
        self.screen.blit(self.hud["map_icon"].base, (903, 15))
        if self.show_bird_modal:
            if self.stats["flags"]["bridge"]:
                self.screen.blit(self.hud["bird_modal_2"], (0, 0))
            elif self.stats["flags"]["purified"]:
                self.screen.blit(self.hud["bird_modal_3"], (0, 0))
            else:
                self.screen.blit(self.hud["bird_modal_1"], (0, 0))
        if self.show_map_modal:
            self.screen.blit(self.hud["map_modal"], (367, 191))
            self.screen.blit(self.hud["yes"].base, (517, 429))
            self.screen.blit(self.hud["no"].end, (656, 429))
        #inventory
        self.screen.blit(self.hud["bar"], (1, 800))
        if self.focus == "inventory":
            self.screen.blit(self.inventory["focused_bag"], (9, 805))
        else:
            self.screen.blit(self.inventory["unfocused_bag"], (9, 805))
        #ideally all these items should be behave as a kind of button
        if self.stats["inv"] == {"money"}:
            self.screen.blit(self.inventory["money"], (270, 834))
        elif self.stats["inv"] == {"money", "net"}:
            self.screen.blit(self.inventory["money"], (270, 834))
            self.screen.blit(self.inventory["net"], (370, 823))
        elif self.stats["inv"] == {"money", "axe"}:
            self.screen.blit(self.inventory["money"], (270, 834))
            self.screen.blit(self.inventory["axe"], (370, 821))
        elif self.stats["inv"] == {"money", "wood"}:
            self.screen.blit(self.inventory["money"], (270, 834))
            self.screen.blit(self.inventory["wood"], (370, 835))
        elif self.stats["inv"] == {"fishing_rod"}:
            self.screen.blit(self.inventory["fishing_rod"], (270, 830))
        elif self.stats["inv"] == {"fishing_rod", "fish"}:
            self.screen.blit(self.inventory["fishing_rod"], (270, 830))
            self.screen.blit(self.inventory["fish"], (430, 829))
        elif self.stats["inv"] == {"key"}:
            self.screen.blit(self.inventory["key"], (270, 837))
        elif self.stats["inv"] == {"glass"}:
            self.screen.blit(self.inventory["glass"], (270, 825))
        # self.screen.blit(self.inventory["money"], (270, 834))
        # self.screen.blit(self.inventory["net"], (370, 823))
        # self.screen.blit(self.inventory["axe"], (490, 821))
        # self.screen.blit(self.inventory["wood"], (570, 835))
        # self.screen.blit(self.inventory["fishing_rod"], (670, 830))
        # self.screen.blit(self.inventory["fish"], (830, 829))
        # self.screen.blit(self.inventory["key"], (930, 837))
        # self.screen.blit(self.inventory["glass"], (1030, 825))
