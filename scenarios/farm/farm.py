import pygame

from gi.repository import Gtk
from scenarios.utils import utils
from scenarios.utils import consts
from scenarios.utils import saves
from scenarios.utils.button import Button
from actors.player import Player
from actors.prompt import Prompt

class Farm:
    """
        Class representing the Farm level, recieves
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
        self.character = "cesar"
        self.background = utils.load_image("background.png", "farm")
        self.background_width = self.background.get_size()[0]
        self.current_slide = 29
        self.prompts = {
            "tools": Prompt(self.screen,
                            self.clock,
                            (523, 480),
                            "prompt.png",
                            "",
                            (400, 600)),
            "valve": Prompt(self.screen,
                            self.clock,
                            (601, 480),
                            "prompt.png",
                            "",
                            (400, 500)),
            "house": Prompt(self.screen,
                            self.clock,
                            (2445, 380),
                            "prompt.png",
                            "",
                            (250, 400)),
            "farmer": Prompt(self.screen,
                             self.clock,
                             (3470, 480),
                             "prompt.png",
                             "",
                             (400, 600)),
            "barn": Prompt(self.screen,
                           self.clock,
                           (3740, 380),
                           "prompt.png",
                           "",
                           (250, 400)),
            "dog":  Prompt(self.screen,
                           self.clock,
                           (4383, 580),
                           "prompt.png",
                           "",
                           (500, 680)),
            "fabric":  Prompt(self.screen,
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
            "system":  Prompt(self.screen,
                              self.clock,
                              (7132, 380),
                              "prompt.png",
                              "",
                              (350, 450)),
            "plant":  Prompt(self.screen,
                             self.clock,
                             (8950, 380),
                             "prompt.png",
                             "",
                             (350, 450)),
            "greenhouse": Prompt(self.screen,
                                 self.clock,
                                 (9062, 480),
                                 "prompt.png",
                                 "",
                                 (400, 600)),
            "tube": Prompt(self.screen,
                           self.clock,
                           (9062, 480),
                           "prompt.png",
                           "",
                           (400, 600)),
            "hole": Prompt(self.screen,
                           self.clock,
                           (9062, 480),
                           "prompt.png",
                           "",
                           (400, 600)),
            "other": Prompt(self.screen,
                            self.clock,
                            (9062, 480),
                            "prompt.png",
                            "",
                            (400, 600))
        }
        self.props = {
            "tools": utils.load_image("tools.png", "farm"),
            "farmer": utils.load_image("farmer.png", "farm"),
            "valve": utils.load_image("valve.png", "farm"),
            "tube": utils.load_image("tube.png", "farm"),
            "plant": utils.load_image("plant.png", "farm"),
            "fabric": utils.load_image("fabric.png", "farm"),
            "cabbage": utils.load_image("cabbage.png", "farm"),
            "dogfood": utils.load_image("dogfood.png", "farm"),
            "special": utils.load_image("key_item.png", "farm"),
            "turbines": (utils.load_image("turbine1.png", "farm"),
                         utils.load_image("turbine2.png", "farm"),
                         utils.load_image("turbine3.png", "farm")),
            "house": (utils.load_image("base.png", "farm/house"),
                      utils.load_image("inside.png", "farm/house")),
            "barn": (utils.load_image("base.png", "farm/barn"),
                     utils.load_image("inside1.png", "farm/barn"),
                     utils.load_image("inside3.png", "farm/barn")),
            "fruit": (utils.load_image("dry.png", "farm/fruit"),
                      utils.load_image("normal.png", "farm/fruit"),
                      utils.load_image("mud.png", "farm/fruit")),
            "sprinklers": (utils.load_image("sprinklers.png", "farm/fruit"),
                           utils.load_image("fixed_sprinklers.png", "farm/fruit")),
            "greenhouse": (utils.load_image("base.png", "farm/greenhouse"),
                           utils.load_image("inside1.png", "farm/greenhouse"),
                           utils.load_image("base2.png", "farm/greenhouse"),
                           utils.load_image("inside2.png", "farm/greenhouse")),
            "seeds": (utils.load_image("1.png", "farm/seeds"),
                      utils.load_image("5.png", "farm/seeds"),
                      utils.load_image("hole.png", "farm/seeds")),
            "system": (utils.load_image("base.png", "farm/system"),
                       utils.load_image("repaired.png", "farm/system")),
            "broken": (utils.load_image("valve1.png", "farm/system"),
                       utils.load_image("valve2.png", "farm/system")),
            "stumps": (utils.load_image("stump1.png", "farm"),
                       utils.load_image("stump2.png", "farm"))
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
            "counter": utils.load_image("counter.png", "HUD"),
            "bird_modal_1": utils.load_image("h1.png", "farm/HUD"),
            "bird_modal_2": utils.load_image("h2.png", "farm/HUD"),
            "bird_modal_3": utils.load_image("h3.png", "farm/HUD"),
            "bird_modal_4": utils.load_image("h4.png", "farm/HUD"),
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

        self.inventory = {
            "unfocused_bag": utils.load_image("bag1.png", "farm/HUD"),
            "focused_bag": utils.load_image("bag2.png", "farm/HUD"),
            "tools": utils.load_image("tools.png", "farm/HUD"),
            "valve": utils.load_image("valve.png", "farm/HUD"),
            "cabbage": utils.load_image("cabbage.png", "farm/HUD"),
            "dogfood": utils.load_image("dogfood.png", "farm/HUD"),
            "fabric": utils.load_image("fabric.png", "farm/HUD"),
            "plant": utils.load_image("plant.png", "farm/HUD"),
            "tube": utils.load_image("tube.png", "farm/HUD")
        }

        self.stats = {
            "inv": {}, # the items the player has
            "flags": {
                "tools": False, # the item is visible on map
                "valve": False, # the item is visible on map
                "house": False, #is not showing inside
                "farmer": False, # have not talked first time with him
                "barn": False, #barn is not showing inside
                "dog": False, # have not met the dog without the food
                "fabric": False, # the item is visible on map
                "pump": False, # system is not repaired
                "plant": False, # the item is visible on map
                "greenhouse": False, #is not showing inside
                "repaired": False, # greenhouse is not repaired
                "tube": False, # the item is visible on map
                "planted": False, # hole is visible
                "fixed": False, # seeder pump is not repaired
                "good_dog": False #dog is not eating its food
            }
        }

        self.dialogue = {
            "1": utils.load_image("d1.png", "farm/dialogue"),#rooster
            "2": utils.load_image("d2.png", "farm/dialogue"),
            "3": utils.load_image("d3.png", "farm/dialogue"),#cesar
            "4": utils.load_image("d4.png", "farm/dialogue"),
            "5": utils.load_image("d5.png", "farm/dialogue"),
            "6": utils.load_image("d6.png", "farm/dialogue"),#farmer
            "7": utils.load_image("d7.png", "farm/dialogue"),#cesar
            "8": utils.load_image("d8.png", "farm/dialogue"),#farmer
            "9": utils.load_image("d9.png", "farm/dialogue"),#cesar
            "10": utils.load_image("d10.png", "farm/dialogue"), #farmer
            "11": utils.load_image("d11.png", "farm/dialogue"), #cesar
            "12": utils.load_image("d12.png", "farm/dialogue"),
            "13": utils.load_image("d13.png", "farm/dialogue"),
            "14": utils.load_image("d14.png", "farm/dialogue"),
            "15": utils.load_image("d15.png", "farm/dialogue"),
            "16": utils.load_image("d16.png", "farm/dialogue"),
            "17": utils.load_image("d17.png", "farm/dialogue"),
            "18": utils.load_image("d18.png", "farm/dialogue"),
            "19": utils.load_image("d19.png", "farm/dialogue"),
            "20": utils.load_image("d20.png", "farm/dialogue"),
            "21": utils.load_image("d21.png", "farm/dialogue"),
            "22": utils.load_image("d22.png", "farm/dialogue"),
            "23": utils.load_image("d23.png", "farm/dialogue"),
            "24": utils.load_image("d24.png", "farm/dialogue"),
            "25": utils.load_image("d25.png", "farm/dialogue"), #farmer
            "26": utils.load_image("d26.png", "farm/dialogue"), #cesar
            "27": utils.load_image("d27.png", "farm/dialogue"), #farmer
            "28": utils.load_image("d28.png", "farm/dialogue") #rooster
        }

        self.icons = {
            "cesar": utils.load_image("cesar_icon.png", "farm"),
            "farmer": utils.load_image("farmer_icon.png", "farm"),
            "rooster": utils.load_image("rooster_icon.png", "farm")
        }
        self.show_bird_modal = False
        self.show_map_modal = False
        self.player = Player(self.screen,
                              self.clock,
                             (150, 620),
                             self.character,
                             9591,
                             True)
        self.focus = "game"

        self.prev = Button((178, 703),
                           "prev1.png",
                           "prev2.png",
                           48,
                           42,
                           "farm")
        self.next = Button((1104, 703),
                           "next1.png",
                           "next2.png",
                           48,
                           42,
                           "farm")

    def run(self):
        utils.load_bg("impromptu.ogg")
        pygame.mixer.music.set_volume(consts.BG_VOLUME)
        pygame.mixer.music.play(-1, 0.0)
        running = True
        while running:
            rel_x = self.player.stage["x"]
            if rel_x < consts.WIDTH_SCREEN:
                self.screen.blit(self.background, (rel_x, -100))
                self.screen.blit(self.props["turbines"][2], (70-abs(rel_x), 133))
                self.screen.blit(self.props["turbines"][2], (845-abs(rel_x), 104))
                self.screen.blit(self.props["turbines"][0], (3037-abs(rel_x), 148))
                self.screen.blit(self.props["turbines"][1], (6387-abs(rel_x), 150))
                self.screen.blit(self.props["turbines"][1], (8030-abs(rel_x), 166))
                self.screen.blit(self.props["turbines"][0], (8928-abs(rel_x), 101))
                self.screen.blit(self.props["stumps"][0], (2473-abs(rel_x), 478))
                self.screen.blit(self.props["stumps"][1], (2763-abs(rel_x), 460))
                self.screen.blit(self.props["stumps"][1], (4500-abs(rel_x), 458))

                if self.stats["flags"]["house"] is True:
                         self.screen.blit(self.props["house"][1], (1472-abs(rel_x), 208))
                         self.screen.blit(self.props["farmer"], (1896-abs(rel_x), 402))
                else:
                    self.screen.blit(self.props["house"][0], (1472-abs(rel_x), 208))

                if self.stats["flags"]["barn"] is True:
                    if self.stats["flags"]["good_dog"] is True:
                        self.screen.blit(self.props["barn"][2], (3454-abs(rel_x), 245))
                    else:
                        self.screen.blit(self.props["barn"][1], (3454-abs(rel_x), 245))
                else:
                    self.screen.blit(self.props["barn"][0], (3454-abs(rel_x), 245))
                if self.stats["flags"]["pump"] is True:
                    self.screen.blit(self.props["system"][1], (5300-abs(rel_x), 255))
                    self.screen.blit(self.props["fruit"][1], (5757-abs(rel_x), -100))
                    self.screen.blit(self.props["sprinklers"][0], (5893-abs(rel_x), 638))
                else:
                    self.screen.blit(self.props["fruit"][2], (5694-abs(rel_x), 473))
                    self.screen.blit(self.props["system"][0], (5300-abs(rel_x), 255))
                    self.screen.blit(self.props["fruit"][0], (5757-abs(rel_x), -100))
                    self.screen.blit(self.props["sprinklers"][0], (5893-abs(rel_x), 638))
                if self.stats["flags"]["greenhouse"] is True:
                    if self.stats["flags"]["repaired"] is True:
                        self.screen.blit(self.props["greenhouse"][3], (6833-abs(rel_x), 71))
                    else:
                        self.screen.blit(self.props["greenhouse"][1], (6833-abs(rel_x), 71))
                else:
                    if self.stats["flags"]["repaired"] is True:
                        self.screen.blit(self.props["greenhouse"][2], (6833-abs(rel_x), 71))
                    else:
                        self.screen.blit(self.props["greenhouse"][0], (6833-abs(rel_x), 71))
                if self.stats["flags"]["fixed"] is True:
                    if self.stats["flags"]["planted"] is True:
                        self.screen.blit(self.props["seeds"][2], (7650-abs(rel_x), 552))
                        self.screen.blit(self.props["plant"], (7650-abs(rel_x), 502))
                        self.screen.blit(self.props["seeds"][1], (7763-abs(rel_x), 549))
                        self.screen.blit(self.props["sprinklers"][1], (7759-abs(rel_x), 640))
                        self.screen.blit(self.props["broken"][1], (8216-abs(rel_x), 530))
                    else:
                        self.screen.blit(self.props["seeds"][2], (7650-abs(rel_x), 552))
                        self.screen.blit(self.props["seeds"][0], (7763-abs(rel_x), 549))
                        self.screen.blit(self.props["sprinklers"][1], (7759-abs(rel_x), 640))
                        self.screen.blit(self.props["broken"][1], (8216-abs(rel_x), 530))
                else:
                    if self.stats["flags"]["planted"] is True:
                        self.screen.blit(self.props["seeds"][2], (7650-abs(rel_x), 552))
                        self.screen.blit(self.props["plant"], (7650-abs(rel_x), 502))
                        self.screen.blit(self.props["seeds"][0], (7763-abs(rel_x), 549))
                        self.screen.blit(self.props["sprinklers"][0], (7759-abs(rel_x), 640))
                        self.screen.blit(self.props["broken"][0], (8216-abs(rel_x), 530))
                    else:
                        self.screen.blit(self.props["seeds"][2], (7650-abs(rel_x), 552))
                        self.screen.blit(self.props["seeds"][0], (7763-abs(rel_x), 549))
                        self.screen.blit(self.props["sprinklers"][0], (7759-abs(rel_x), 640))
                        self.screen.blit(self.props["broken"][0], (8216-abs(rel_x), 530))
                # else:
                #     self.screen.blit(self.props["logger"][0], (2415-abs(rel_x), 405))
                #     self.screen.blit(self.props["cabin"][0], (3240-abs(rel_x), 220))
                # if self.stats["flags"]["bridge"] is True:
                #     self.screen.blit(self.props["bridge"][1], (4104-abs(rel_x), 482))
                # else:
                #     self.screen.blit(self.props["bridge"][0], (4104-abs(rel_x), 482))
                # if self.stats["flags"]["trash"] is False:
                #     self.screen.blit(self.props["trash"], (4333-abs(rel_x), 678))
                # self.screen.blit(self.props["canoe"], (4678-abs(rel_x), 650))
                # self.screen.blit(self.props["trees"][0], (4673-abs(rel_x), -100))
                # if self.stats["flags"]["fished"] is False:
                #     self.screen.blit(self.props["fish"], (5539-abs(rel_x), 690))
                # self.screen.blit(self.props["trees"][1], (5863-abs(rel_x), -100))
                # if self.stats["flags"]["open"] is True:
                #     if self.stats["flags"]["purifier"] is True:
                #         self.screen.blit(self.props["purifier"][2], (6079-abs(rel_x), 183))
                #     else:
                #         self.screen.blit(self.props["purifier"][1], (6079-abs(rel_x), 183))
                # else:
                #     self.screen.blit(self.props["purifier"][0], (6079-abs(rel_x), 183))
                # self.screen.blit(self.props["trees"][2], (7347-abs(rel_x), -100))
                # if self.stats["flags"]["glass"] is True:
                #     self.screen.blit(self.props["fence"][1], (8209-abs(rel_x), 398))
                #     self.screen.blit(self.props["special"], (8815-abs(rel_x), 326))
                #     self.screen.blit(self.props["guard"], (8820-abs(rel_x), 501))
                # else:
                #     self.screen.blit(self.props["fence"][0], (8209-abs(rel_x), 398))
                #     self.screen.blit(self.props["special"], (8815-abs(rel_x), 326))
                #     self.screen.blit(self.props["guard"], (8920-abs(rel_x), 501))
                self.load_items(abs(rel_x))
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
                        if self.current_slide == 29:
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
                              or 25 < self.current_slide < 28):
                            self.prev.on_press(self.screen)
                            self.current_slide -= 1
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                        if self.current_slide == 29:
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
                              or (6 < self.current_slide < 11)
                              or (14 < self.current_slide < 18)
                              or (18 < self.current_slide < 22)
                              or (24 < self.current_slide < 27)):
                            self.next.on_press(self.screen)
                            self.current_slide +=1
                        elif ((3 < self.current_slide < 7)
                              or self.current_slide == 11
                              or (12 < self.current_slide < 15)
                              or self.current_slide == 18
                              or self.current_slide == 22
                              or (22 < self.current_slide < 25)
                              or self.current_slide == 27):
                            self.next.on_press(self.screen)
                            self.current_slide = 29
                        elif self.current_slide == 28:
                            running = False
                            utils.loading_screen(self.screen)
                            #save here
                            if not self.slot["stages"]["granja"] is True:
                                saves.save(5, "Granja de Cultivos", "granja")
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_KP2:
                        if self.current_slide == 29 and self.focus == "game":
                            self.player.direction = "down"
                            self.player.y_velocity = abs(self.player.y_velocity)
                    elif event.key == pygame.K_UP or event.key == pygame.K_KP8:
                        if self.current_slide == 29 and self.focus == "game":
                            self.player.direction = "up"
                            self.player.y_velocity = -abs(self.player.y_velocity)
                    elif event.key == pygame.K_RETURN or event.key == consts.K_CHECK:
                        if self.current_slide == 29 and self.focus == "game":
                            self.player.running = True
                    elif event.key == pygame.K_SPACE or event.key == consts.K_CROSS:
                        if self.current_slide == 29:
                            if self.focus == "game":
                                pass
                                # if (self.player.real_x+self.player.rect.width > 500
                                #         and self.player.real_x+self.player.rect.width < 553
                                #         and not self.stats["flags"]["tools"]):
                                #     self.stats["flags"]["tools"] = True
                                #     self.stats["inv"] = {"tools"}
                                #     self.current_slide = 5
                                # if (self.player.real_x+self.player.rect.width > 565
                                #     and self.player.real_x+self.player.rect.width < 685
                                #     and not self.stats["flags"]["valve"]
                                #     and "tools" in self.stats["inv"]):
                                #     self.stats["flags"]["valve"] = True
                                #     self.stats["inv"] = {"tools", "valve"}
                                #     self.current_slide = 6
                                # if (self.player.real_x+self.player.rect.width > 2400
                                #     and self.player.real_x+self.player.rect.width < 2595
                                #     and "axe" in self.stats["inv"]):
                                #     self.current_slide = 15
                                #     self.stats["flags"]["logger"] = True
                                #     self.stats["inv"] = {"tools", "wood"}
                                # elif (self.player.real_x+self.player.rect.width > 2400
                                #       and self.player.real_x+self.player.rect.width < 2595
                                #       and self.stats["flags"]["logger"] is False):
                                #     self.current_slide = 7
                                # if (self.player.real_x+self.player.rect.width > 3390
                                #     and self.player.real_x+self.player.rect.width < 3650
                                #     and self.stats["flags"]["logger"]):
                                #     self.stats["flags"]["cabin"] = True
                                # elif (self.player.real_x+self.player.rect.width > 3390
                                #     and self.player.real_x+self.player.rect.width < 3650
                                #     and self.stats["flags"]["cabin"]):
                                #     self.stats["flags"]["cabin"] = False

                                # #the various interactions with the cabin owner
                                # if (self.player.real_x+self.player.rect.width > 3700
                                #     and self.player.real_x+self.player.rect.width < 3950
                                #     and self.stats["flags"]["cabin"]
                                #     and not self.stats["flags"]["bridge"]
                                #     and not self.stats["flags"]["fished"]):
                                #     self.current_slide = 19
                                #     self.stats["flags"]["bridge"] = True
                                #     self.stats["inv"] = {"fishing_rod"}
                                # if (self.player.real_x+self.player.rect.width > 3700
                                #     and self.player.real_x+self.player.rect.width < 3950
                                #     and self.stats["flags"]["cabin"]
                                #     and self.stats["flags"]["fished"]
                                #     and not self.stats["flags"]["open"]
                                #     and "key" not in self.stats["inv"]):
                                #     self.current_slide = 25
                                #     self.stats["inv"] = {"key"}

                                # #trash state
                                # if (self.player.real_x+self.player.rect.width > 4000
                                #     and self.player.real_x+self.player.rect.width <= 4104
                                #     and not self.stats["flags"]["trash"]
                                #     and "valve" in self.stats["inv"]):
                                #     self.current_slide = 14
                                #     self.stats["flags"]["trash"] = True
                                #     self.stats["inv"] = {"tools", "axe"}
                                # elif (self.player.real_x+self.player.rect.width > 4000
                                #       and self.player.real_x+self.player.rect.width <= 4104
                                #       and not self.stats["flags"]["trash"]
                                #       and "valve" not in self.stats["inv"]):
                                #     self.current_slide = 13

                                # #fishing states
                                # if (self.player.real_x+self.player.rect.width > 5480
                                #     and self.player.real_x+self.player.rect.width < 5620
                                #     and not self.stats["flags"]["fished"]
                                #     and "fishing_rod" in self.stats["inv"]):
                                #     self.current_slide = 24
                                #     self.stats["flags"]["fished"] = True
                                #     self.stats["inv"] = {"fishing_rod", "fish"}
                                # elif (self.player.real_x+self.player.rect.width > 5480
                                #     and self.player.real_x+self.player.rect.width < 5620
                                #     and not self.stats["flags"]["fished"]
                                #     and "fishing_rod" not in self.stats["inv"]):
                                #     self.current_slide = 23
                                #     self.stats["flags"]["fished"] = True
                                #     self.stats["inv"] = {"fishing_rod", "fish"}

                                # #purifier states
                                # if (self.player.real_x+self.player.rect.width > 6018
                                #     and self.player.real_x+self.player.rect.width < 6296
                                #     and not self.stats["flags"]["open"]
                                #     and "key" in self.stats["inv"]):
                                #     self.stats["flags"]["open"] = True
                                # elif (self.player.real_x+self.player.rect.width > 6018
                                #     and self.player.real_x+self.player.rect.width < 6296
                                #     and self.stats["flags"]["open"]
                                #     and not self.stats["flags"]["purified"]):
                                #     self.current_slide = 28
                                #     self.stats["inv"] = {}
                                #     self.stats["flags"]["purifier"] = True
                                #     self.stats["flags"]["purified"] = True

                                # if (self.player.real_x+self.player.rect.width > 7000
                                #     and self.player.real_x+self.player.rect.width < 7316
                                #     and not self.stats["flags"]["picked"]):
                                #     self.current_slide = 35
                                #     self.stats["flags"]["picked"] = True
                                #     self.stats["inv"] = {"glass"}

                                # #guard
                                # if (self.player.real_x+self.player.rect.width > 8900
                                #     and self.player.real_x+self.player.rect.width < 9080
                                #     and not self.stats["flags"]["glass"]
                                #     and "glass" in self.stats["inv"]):
                                #     self.current_slide = 31
                                #     self.stats["flags"]["glass"] = True
                                #     self.stats["inv"] = {}
                                # elif (self.player.real_x+self.player.rect.width > 8900
                                #     and self.player.real_x+self.player.rect.width < 9080
                                #     and not self.stats["flags"]["glass"]
                                #     and "glass" not in self.stats["inv"]):
                                #     self.current_slide = 30
                                # if (self.player.real_x+self.player.rect.width > 9080
                                #     and self.player.real_x+self.player.rect.width < 9200
                                #     and self.stats["flags"]["glass"]):
                                #     self.current_slide = 34
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
                        if self.current_slide == 29:
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
        if number == 29:
            self.actors_load(rel_x)
        elif number in (1, 28, 34):
            self.player.update()
            self.screen.blit(self.icons["rooster"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.next.base, (1104, 703))
        elif (1 < number < 4) or number == 27:
            self.player.update()
            self.screen.blit(self.icons["rooster"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.prev.base, (178, 703))
            self.screen.blit(self.next.base, (1104, 703))
        elif number == 4:
            self.player.update()
            self.screen.blit(self.icons["cesar"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.prev.base, (178, 703))
            self.screen.blit(self.next.base, (1104, 703))
        elif ((4 < number < 7)
              or (12 < number < 15)
              or (22 < number < 25)):
            #cesar commenting on an item
            self.player.update()
            self.screen.blit(self.icons["cesar"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.next.base, (1104, 703))
        elif number == 7: #logger initiating a conversation
            self.player.update()
            self.screen.blit(self.icons["logger"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.next.base, (1104, 703))
        elif number in (8, 10, 17, 20, 22, 32):
            self.player.update()
            self.screen.blit(self.icons["cesar"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.prev.base, (178, 703))
            self.screen.blit(self.next.base, (1104, 703))
        elif number in (9, 11, 16, 18):
            self.player.update()
            self.screen.blit(self.icons["logger"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.prev.base, (178, 703))
            self.screen.blit(self.next.base, (1104, 703))
        elif number == 15: #cesar initiating a conversation
            self.player.update()
            self.screen.blit(self.icons["cesar"], (9, 654))
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



    def actors_load(self, rel_x):
        # if (self.player.real_x+self.player.rect.width > 500
        #     and self.player.real_x+self.player.rect.width < 553
        #     and not self.stats["flags"]["tools"]):
        #     self.prompts["tools"].float(rel_x)
        # if (self.player.real_x+self.player.rect.width > 565
        #     and self.player.real_x+self.player.rect.width < 685
        #     and not self.stats["flags"]["valve"]
        #     and "tools" in self.stats["inv"]):
        #     self.prompts["valve"].float(rel_x)
        # if (self.player.real_x+self.player.rect.width > 2400
        #     and self.player.real_x+self.player.rect.width < 2595
        #     and self.stats["flags"]["logger"] == False):
        #     self.prompts["logger"].float(rel_x)
        # if (self.player.real_x+self.player.rect.width > 3390
        #     and self.player.real_x+self.player.rect.width < 3650
        #     and self.stats["flags"]["logger"]
        #     and self.stats["flags"]["cabin"] == False):
        #     self.prompts["cabin"].float(rel_x)
        # if (self.player.real_x+self.player.rect.width > 3700
        #     and self.player.real_x+self.player.rect.width < 3950
        #     and self.stats["flags"]["cabin"]
        #     and (self.stats["flags"]["bridge"] == False or
        #          ( self.stats["flags"]["fished"] and
        #            not self.stats["flags"]["open"] and
        #            "key" not in self.stats["inv"]))):
        #     self.prompts["owner"].float(rel_x)
        # if (self.player.real_x+self.player.rect.width > 4000
        #     and self.player.real_x+self.player.rect.width <= 4104
        #     and not self.stats["flags"]["trash"]):
        #     self.prompts["trash"].float(rel_x)
        # if (self.player.real_x+self.player.rect.width > 5480
        #     and self.player.real_x+self.player.rect.width < 5620
        #     and not self.stats["flags"]["fished"]):
        #     self.prompts["fish"].float(rel_x)
        # if (self.player.real_x+self.player.rect.width > 6018
        #     and self.player.real_x+self.player.rect.width < 6296
        #     and "key" in self.stats["inv"]):
        #     self.prompts["purifier"].float(rel_x)
        # if (self.player.real_x+self.player.rect.width > 7000
        #     and self.player.real_x+self.player.rect.width < 7316
        #     and not self.stats["flags"]["picked"]):
        #     self.prompts["glass"].float(rel_x)
        # if (self.player.real_x+self.player.rect.width > 8900
        #     and self.player.real_x+self.player.rect.width < 9080
        #     and not self.stats["flags"]["glass"]):
        #     self.prompts["guard"].float(rel_x)
        # if (self.player.real_x+self.player.rect.width > 9080
        #     and self.player.real_x+self.player.rect.width < 9200
        #     and self.stats["flags"]["glass"]):
        #     self.prompts["guard"].float(rel_x)
        # if 4090 < self.player.real_x < 4790:
        #     self.player.rect.y = 444
        # if 4790 < self.player.real_x < 7500:
        #     if self.player.rect.y > 500:
        #         self.player.rect.y = 500
        # if 8554 < self.player.real_x:
        #     if self.player.rect.y < 492:
        #         self.player.rect.y = 492
        # if self.player.real_x+self.player.rect.width > 4004 and self.stats["flags"]["bridge"] is False:
        #     if self.player.velocity > 0:
        #         self.player.stage["x"] = -3340
        #         self.player.real_x =  4004 -self.player.rect.width
        print self.player.real_x
        print self.player.rect.y
        self.player.update()

    def load_items(self, rel_x):
        if self.stats["flags"]["tools"] is False:
            self.screen.blit(self.props["tools"], (447-rel_x, 496))
        if (self.stats["flags"]["valve"] is False and
            self.stats["flags"]["house"] is True):
            self.screen.blit(self.props["valve"], (1680-rel_x, 396))
        if self.stats["flags"]["fabric"] is False:
            self.screen.blit(self.props["fabric"], (4009-rel_x, 608))
        if self.stats["flags"]["plant"] is False:
            self.screen.blit(self.props["plant"], (5822-rel_x, 532))
        if (self.stats["flags"]["tube"] is False and
            self.stats["flags"]["greenhouse"] is True):
            self.screen.blit(self.props["tube"], (6953-rel_x, 532))

    def load_hud(self):
        #top icons
        self.screen.blit(self.hud["bird_icon"].end, (1053, 15))
        self.screen.blit(self.hud["map_icon"].base, (903, 15))
        if self.show_bird_modal:
            if self.stats["flags"]["farmer"]:
                self.screen.blit(self.hud["bird_modal_2"], (0, 0))
            elif self.stats["flags"]["repaired"]:
                self.screen.blit(self.hud["bird_modal_3"], (0, 0))
            elif self.stats["flags"]["fixed"]:
                self.screen.blit(self.hud["bird_modal_4"], (0, 0))
            else:
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
        elif self.stats["inv"] == {"tools", "valve"}:
            self.screen.blit(self.inventory["tools"], (275, 813))
            self.screen.blit(self.inventory["valve"], (425, 823))
        elif self.stats["inv"] == {"tools", "valve", "fabric"}:
            self.screen.blit(self.inventory["tools"], (275, 813))
            self.screen.blit(self.inventory["valve"], (425, 823))
            self.screen.blit(self.inventory["fabric"], (520, 831))
        elif self.stats["inv"] == {"tools", "fabric"}:
            self.screen.blit(self.inventory["tools"], (275, 813))
            self.screen.blit(self.inventory["fabric"], (425, 831))
        elif self.stats["inv"] == {"tools", "fabric", "plant"}:
            self.screen.blit(self.inventory["tools"], (275, 813))
            self.screen.blit(self.inventory["fabric"], (425, 831))
            self.screen.blit(self.inventory["plant"], (600, 815))
        elif self.stats["inv"] == {"tools", "plant"}:
            self.screen.blit(self.inventory["tools"], (275, 813))
            self.screen.blit(self.inventory["plant"], (425, 815))
        elif self.stats["inv"] == {"tools", "plant", "tube"}:
            self.screen.blit(self.inventory["tools"], (275, 813))
            self.screen.blit(self.inventory["plant"], (425, 815))
            self.screen.blit(self.inventory["tube"], (530, 830))
        elif self.stats["inv"] == {"tools", "plant", "tube"}:
            self.screen.blit(self.inventory["tools"], (275, 813))
            self.screen.blit(self.inventory["plant"], (425, 815))
            self.screen.blit(self.inventory["tube"], (530, 830))
        elif self.stats["inv"] == {"tube"}:
            self.screen.blit(self.inventory["tube"], (275, 830))
        elif self.stats["inv"] == {"cabbage"}:
            self.screen.blit(self.inventory["cabbage"], (275, 832))
        elif self.stats["inv"] == {"dogfood"}:
            self.screen.blit(self.inventory["dogfood"], (275, 830))

        # self.screen.blit(self.inventory["tools"], (275, 813))
        # self.screen.blit(self.inventory["valve"], (425, 823))
        # self.screen.blit(self.inventory["fabric"], (520, 831))
        # self.screen.blit(self.inventory["plant"], (690, 815))
        # self.screen.blit(self.inventory["tube"], (790, 830))
        # self.screen.blit(self.inventory["cabbage"], (900, 832))
        # self.screen.blit(self.inventory["dogfood"], (990, 830))
