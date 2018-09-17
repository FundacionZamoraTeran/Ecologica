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
            "bar": utils.load_image("bar.png", "HUD"),
            "bird_icon": utils.load_image("icon.png", "HUD"),
            "counter": utils.load_image("counter.png", "HUD"),
            "bird_modal": utils.load_image("bird_modal.png", "HUD"),
            "exit_bird": utils.load_image("exit.png", "HUD"),
            "map_icon": utils.load_image("map.png", "HUD"),
            "map_modal": utils.load_image("modal.png", "HUD"),
            "yes": Button((503, 441),
                          "yes1.png",
                          "yes2.png",
                          83,
                          56,
                          "HUD",
                          flag=True),
            "no": Button((611, 441),
                         "no1.png",
                         "no2.png",
                         83,
                         56,
                         "HUD")
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

        self.player = Player(self.screen,
                              self.clock,
                             (150, 620),
                             self.character,
                             9600,
                             True)
        self.focus = "game"

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
                self.actors_load(abs(rel_x))
                self.screen.blit(self.props["handrail"], (4236-abs(rel_x), 548))
                if self.stats["flags"]["open"] is True:
                    self.screen.blit(self.props["cover"], (6297-abs(rel_x), 184))
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
                        self.player.direction = "left"
                        self.player.running_velocity = -abs(self.player.running_velocity)
                        self.player.velocity = -abs(self.player.velocity)
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                        self.player.direction = "right"
                        self.player.running_velocity = abs(self.player.running_velocity)
                        self.player.velocity = abs(self.player.velocity)
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_KP2:
                        self.player.direction = "down"
                        self.player.y_velocity = abs(self.player.y_velocity)
                    elif event.key == pygame.K_UP or event.key == pygame.K_KP8:
                        self.player.direction = "up"
                        self.player.y_velocity = -abs(self.player.y_velocity)
                    elif event.key == pygame.K_RETURN or event.key == consts.K_CHECK:
                        self.player.running = True
                    elif event.key == pygame.K_SPACE or event.key == consts.K_CROSS:
                        if (self.player.real_x+self.player.rect.width > 500
                            and self.player.real_x+self.player.rect.width < 553
                            and not self.stats["flags"]["money"]):
                            self.stats["flags"]["money"] = True
                            self.stats["inv"]= {"money"}
                        if (self.player.real_x+self.player.rect.width > 565
                            and self.player.real_x+self.player.rect.width < 685
                            and not self.stats["flags"]["net"]
                            and "money" in self.stats["inv"]):
                            self.stats["flags"]["net"] = True
                            self.stats["inv"]= {"money", "net"}
                        if (self.player.real_x+self.player.rect.width > 2400
                            and self.player.real_x+self.player.rect.width < 2595
                            and "axe" in self.stats["inv"]):
                            #trigger another dialog
                            self.stats["flags"]["logger"] = True
                            self.stats["inv"]= {"money", "wood"}
                        elif (self.player.real_x+self.player.rect.width > 2400
                              and self.player.real_x+self.player.rect.width < 2595):
                            pass#trigger dialog with logger
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
                            and self.stats["flags"]["cabin"] and not self.stats["flags"]["fished"]):
                            self.stats["flags"]["bridge"] = True
                            self.stats["inv"]= {"fishing_rod"}
                        if (self.player.real_x+self.player.rect.width > 3700
                            and self.player.real_x+self.player.rect.width < 3950
                            and self.stats["flags"]["cabin"] and self.stats["flags"]["fished"]):
                            self.stats["inv"]= {"key"}

                        if (self.player.real_x+self.player.rect.width > 4000
                            and self.player.real_x+self.player.rect.width <= 4104
                            and not self.stats["flags"]["trash"]
                            and "net" in self.stats["inv"]):
                            self.stats["flags"]["trash"] = True
                            self.stats["inv"]= {"money", "axe"}
                        if (self.player.real_x+self.player.rect.width > 5480
                            and self.player.real_x+self.player.rect.width < 5620
                            and not self.stats["flags"]["fished"]
                            and "fishing_rod" in self.stats["inv"]):
                            #logic for fishing stance on ezer
                            self.stats["flags"]["fished"] = True
                            self.stats["inv"]= {"fishing_rod", "fish"}

                        #purifier states
                        if (self.player.real_x+self.player.rect.width > 6018
                            and self.player.real_x+self.player.rect.width < 6296
                            and not self.stats["flags"]["open"]
                            and "key" in self.stats["inv"]):
                            self.stats["flags"]["open"] = True
                        elif (self.player.real_x+self.player.rect.width > 6018
                            and self.player.real_x+self.player.rect.width < 6296
                            and self.stats["flags"]["open"]):
                            self.stats["flags"]["purifier"] = True
                            self.stats["flags"]["purified"] = True

                        if (self.player.real_x+self.player.rect.width > 7000
                            and self.player.real_x+self.player.rect.width < 7316
                            and not self.stats["flags"]["picked"]):
                            self.stats["flags"]["picked"] = True
                            self.stats["inv"]= {"glass"}

                        #guard
                        if (self.player.real_x+self.player.rect.width > 8900
                            and self.player.real_x+self.player.rect.width < 9080
                            and not self.stats["flags"]["glass"]
                            and "glass" in self.stats["inv"]):
                            self.stats["flags"]["glass"] = True
                            self.stats["inv"]= {}
                        if (self.player.real_x+self.player.rect.width > 9080
                            and self.player.real_x+self.player.rect.width < 9200
                            and self.stats["flags"]["glass"]):
                            #something of a congrats modal here
                            running = False
                            utils.loading_screen(self.screen)
                            #save here
                            if not self.slot["stages"]["rio"] is True:
                                saves.save(6, "Rio Claro", "rio")



                    elif event.key == pygame.K_ESCAPE or event.key == consts.K_CIRCLE:
                        pass
                        # move focus to upper menu bar
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
            and self.player.real_x+self.player.rect.width < 2595):
            self.prompts["logger"].float(rel_x)
        if (self.player.real_x+self.player.rect.width > 3390
            and self.player.real_x+self.player.rect.width < 3650
            and self.stats["flags"]["logger"]):
            self.prompts["cabin"].float(rel_x)
        if (self.player.real_x+self.player.rect.width > 3700
            and self.player.real_x+self.player.rect.width < 3950
            and self.stats["flags"]["cabin"]):
            self.prompts["owner"].float(rel_x)
        if (self.player.real_x+self.player.rect.width > 4000
            and self.player.real_x+self.player.rect.width <= 4104
            and not self.stats["flags"]["trash"]
            and "net" in self.stats["inv"]):
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
        if 4790 < self.player.real_x  < 7500:
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
        print self.player.rect.y
        print self.player.real_x
        self.player.update()

    def load_items(self, rel_x):
        if self.stats["flags"]["money"] is False:
            self.screen.blit(self.props["money"], (523-rel_x, 617))
        if self.stats["flags"]["net"] is False:
            self.screen.blit(self.props["net"], (565-rel_x, 528))
        if self.stats["flags"]["picked"] is False:
            self.screen.blit(self.props["glass"], (7132-rel_x, 528))

    def load_hud(self):
        #top icons
        self.screen.blit(self.hud["bird_icon"], (1053, 15))
        self.screen.blit(self.hud["counter"], (1082, 117))
        text = self.font.render(str(self.slot["coins"]),True, (255,255,255))
        self.screen.blit(text, (1130, 126))
        self.screen.blit(self.hud["map_icon"], (903, 15))
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
