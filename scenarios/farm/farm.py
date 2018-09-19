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
        self.current_slide = 1
        self.prompts = {
            "tools": Prompt(self.screen,
                            self.clock,
                            (523, 400),
                            "prompt.png",
                            "",
                            (380, 500)),
            "valve": Prompt(self.screen,
                            self.clock,
                            (1695, 350),
                            "prompt.png",
                            "",
                            (300, 400)),
            "house": Prompt(self.screen,
                            self.clock,
                            (1718, 420),
                            "prompt.png",
                            "",
                            (350, 480)),
            "farmer": Prompt(self.screen,
                             self.clock,
                             (1934, 350),
                             "prompt.png",
                             "",
                             (300, 400)),
            "barn": Prompt(self.screen,
                           self.clock,
                           (3800, 420),
                           "prompt.png",
                           "",
                           (350, 480)),
            "dog":  Prompt(self.screen,
                           self.clock,
                           (3896, 300),
                           "prompt.png",
                           "",
                           (250, 400)),
            "fabric":  Prompt(self.screen,
                              self.clock,
                              (4086, 480),
                              "prompt.png",
                              "",
                              (400, 600)),
            "system":  Prompt(self.screen,
                              self.clock,
                              (5721, 380),
                              "prompt.png",
                              "",
                              (350, 500)),
            "plant":  Prompt(self.screen,
                             self.clock,
                             (5850, 380),
                             "prompt.png",
                             "",
                             (350, 450)),
            "greenhouse": Prompt(self.screen,
                                 self.clock,
                                 (7092, 480),
                                 "prompt.png",
                                 "",
                                 (400, 600)),
            "repair": Prompt(self.screen,
                                 self.clock,
                                 (6840, 480),
                                 "prompt.png",
                                 "",
                                 (400, 600)),
            "tube": Prompt(self.screen,
                           self.clock,
                           (6980, 420),
                           "prompt.png",
                           "",
                           (400, 500)),
            "hole": Prompt(self.screen,
                           self.clock,
                           (7680, 420),
                           "prompt.png",
                           "",
                           (380, 530)),
            "cabbage": Prompt(self.screen,
                           self.clock,
                           (7940, 420),
                           "prompt.png",
                           "",
                           (380, 530)),
            "seeder_pump": Prompt(self.screen,
                           self.clock,
                           (8304, 420),
                           "prompt.png",
                           "",
                           (380, 530)),
            "special": Prompt(self.screen,
                            self.clock,
                              (4055, 380),
                            "prompt.png",
                            "",
                            (350, 450))
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
                "cabbage": False, # does not have the item
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
                        self.screen.blit(self.props["sprinklers"][1], (7680-abs(rel_x), 563))
                        self.screen.blit(self.props["broken"][1], (8216-abs(rel_x), 530))
                    else:
                        self.screen.blit(self.props["seeds"][2], (7650-abs(rel_x), 552))
                        self.screen.blit(self.props["seeds"][0], (7763-abs(rel_x), 549))
                        self.screen.blit(self.props["sprinklers"][1], (7680-abs(rel_x), 563))
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
                        elif ((1 < self.current_slide < 4)
                              or self.current_slide in (7, 8,  9, 10, 26, 27)):
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
                        elif ((self.current_slide < 3)
                              or self.current_slide in (6, 7, 8, 9, 25, 26)):
                            self.next.on_press(self.screen)
                            self.current_slide +=1
                        elif ((10 < self.current_slide < 25)
                              or self.current_slide in (3, 4, 5, 10, 27)):
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
                                if (396 < self.player.real_x < 676
                                    and not self.stats["flags"]["tools"]):
                                    self.stats["flags"]["tools"] = True
                                    self.stats["inv"] = {"tools"}
                                    self.current_slide = 4
                                #house interactions
                                if (1606 <self.player.real_x < 1802
                                    and self.stats["flags"]["house"] is False):
                                    self.stats["flags"]["house"] = True
                                    self.current_slide = 5
                                elif (1610 < self.player.real_x < 1722
                                    and not self.stats["flags"]["valve"]
                                    and self.stats["flags"]["house"] == True
                                    and "tools" in self.stats["inv"]):
                                    self.stats["flags"]["valve"] = True
                                    self.stats["inv"] = {"tools", "valve"}
                                    self.current_slide = 11
                                elif ( 1836 <self.player.real_x < 2006
                                       and self.stats["flags"]["house"] == True
                                       and self.stats["flags"]["farmer"] is False
                                       and "cabbage" not in self.stats["inv"]):
                                    self.current_slide = 6
                                elif ( 1838 <self.player.real_x < 2006
                                     and self.stats["flags"]["house"] == True
                                     and "cabbage" in self.stats["inv"]) :
                                    self.stats["inv"] = {"dogfood"}
                                    self.current_slide = 25

                                #barn interactions
                                if (3628 < self.player.real_x< 3908
                                    and self.stats["flags"]["barn"] is False):
                                    self.stats["flags"]["barn"] = True
                                    self.current_slide = 15
                                elif (443 < self.player.rect.y < 480
                                      and 3616 < self.player.real_x < 3701
                                      and self.stats["flags"]["good_dog"] is False
                                      and self.stats["flags"]["dog"] is False
                                      and self.stats["flags"]["barn"] == True):
                                    self.stats["flags"]["dog"] = True
                                    self.current_slide = 16
                                elif (443 < self.player.rect.y < 480
                                      and 3616 < self.player.real_x < 3701
                                      and self.stats["flags"]["good_dog"] is False
                                      and "dogfood" in self.stats["inv"]
                                      and self.stats["flags"]["barn"] == True):
                                    self.stats["flags"]["good_dog"] = True
                                    self.stats["inv"] = {}
                                if (443 < self.player.rect.y < 480
                                    and 3916 < self.player.real_x < 4158
                                    and self.stats["flags"]["good_dog"] == True
                                    and self.stats["flags"]["barn"] == True):
                                    self.current_slide = 28

                                #fabric/plastic
                                if (3964 < self.player.real_x< 4216
                                    and {"tools", "valve"} == self.stats["inv"]
                                    and self.stats["flags"]["fabric"] is False):
                                    self.stats["flags"]["fabric"] = True
                                    self.stats["inv"] = {"tools", "valve", "fabric"}
                                    self.current_slide = 12

                                #pump and plant
                                if (5632 < self.player.real_x< 5772
                                    and "valve" in self.stats["inv"]
                                    and self.stats["flags"]["pump"] is False):
                                    self.stats["flags"]["pump"] = True
                                    self.stats["inv"] = {"tools", "fabric"}
                                    self.current_slide = 14
                                if (5771 < self.player.real_x< 5912
                                    and {"tools", "fabric"} == self.stats["inv"]
                                    and self.stats["flags"]["pump"] == True
                                    and self.stats["flags"]["plant"] is False):
                                    self.stats["flags"]["plant"] = True
                                    self.stats["inv"] = {"tools", "fabric", "plant"}
                                    self.current_slide = 17

                                #greenhouse interactions
                                if (6924 <self.player.real_x < 7232
                                    and self.stats["flags"]["greenhouse"] is False):
                                    self.stats["flags"]["greenhouse"] = True
                                    self.current_slide = 18
                                if (6784 <self.player.real_x < 6952
                                    and self.stats["flags"]["greenhouse"]
                                    and "fabric" in self.stats["inv"]):
                                    self.stats["flags"]["repaired"] = True
                                    self.stats["inv"] = {"tools", "plant"}
                                    self.current_slide = 19
                                if (6951 <self.player.real_x < 7037
                                    and self.stats["flags"]["greenhouse"]
                                    and {"tools", "plant"} ==self.stats["inv"]):
                                    self.stats["flags"]["tube"] = True
                                    self.stats["inv"] = {"tools", "plant", "tube"}
                                    self.current_slide = 20

                                #seeder lot interactions
                                if (7596 <self.player.real_x < 7764
                                    and self.stats["flags"]["planted"] is False
                                    and "plant" in self.stats["inv"]):
                                    self.stats["flags"]["planted"] = True
                                    self.stats["inv"].remove("tools")
                                    self.stats["inv"].remove("plant")
                                    self.current_slide = 22
                                if (7763 <self.player.real_x < 8164
                                    and self.stats["flags"]["planted"]
                                    and self.stats["flags"]["cabbage"] is False
                                    and self.stats["flags"]["fixed"]):
                                    self.stats["flags"]["cabbage"] = True
                                    self.stats["inv"] = {"cabbage"}
                                    self.current_slide = 24
                                if (8163 <self.player.real_x < 8416
                                    and self.stats["flags"]["fixed"] is False
                                    and "tube" in self.stats["inv"]):
                                    self.stats["flags"]["fixed"] = True
                                    self.stats["inv"].remove("tube")
                                    self.current_slide = 21

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
        elif number in (1, 28):
            self.player.update()
            self.screen.blit(self.icons["rooster"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.next.base, (1104, 703))
        elif number == 2:
            self.player.update()
            self.screen.blit(self.icons["rooster"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.prev.base, (178, 703))
            self.screen.blit(self.next.base, (1104, 703))
        elif number in (3, 7, 9, 26):
            self.player.update()
            self.screen.blit(self.icons["cesar"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.prev.base, (178, 703))
            self.screen.blit(self.next.base, (1104, 703))
        elif ((3 < number < 6)
              or (10 < number < 25)):
            #cesar commenting on an item
            self.player.update()
            self.screen.blit(self.icons["cesar"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.next.base, (1104, 703))
        elif number in (6, 25): #farmer initiating a conversation
            self.player.update()
            self.screen.blit(self.icons["farmer"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.next.base, (1104, 703))
        elif number in (8, 10, 27):
            self.player.update()
            self.screen.blit(self.icons["farmer"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.prev.base, (178, 703))
            self.screen.blit(self.next.base, (1104, 703))



    def actors_load(self, rel_x):
        if (396 < self.player.real_x < 676
            and not self.stats["flags"]["tools"]):
            self.prompts["tools"].float(rel_x)
        if (1610 <self.player.real_x < 1722
            and not self.stats["flags"]["valve"]
            and self.stats["flags"]["house"] == True
            and "tools" in self.stats["inv"]):
            self.prompts["valve"].float(rel_x)
        if (1606 <self.player.real_x < 1802
            and self.stats["flags"]["house"] is False):
            self.prompts["house"].float(rel_x)
        if ( 1836 <self.player.real_x < 2006
            and self.stats["flags"]["house"] == True
            and (self.stats["flags"]["farmer"] is False
                 or self.stats["flags"]["cabbage"] == True)):
            self.prompts["farmer"].float(rel_x)
        if (3628 < self.player.real_x< 3908
            and self.stats["flags"]["barn"] is False):
            self.prompts["barn"].float(rel_x)
        if (443 < self.player.rect.y < 480
            and 3616 < self.player.real_x < 3701
            and self.stats["flags"]["good_dog"] is False
            and (self.stats["flags"]["dog"] is False
                 or "dogfood" in self.stats["inv"])
            and self.stats["flags"]["barn"] == True):
            self.prompts["dog"].float(rel_x)
        if (443 < self.player.rect.y < 480
            and 3916 < self.player.real_x < 4158
            and self.stats["flags"]["good_dog"] == True
            and self.stats["flags"]["barn"] == True):
            self.prompts["special"].float(rel_x)
        if (443 < self.player.rect.y < 480
            and 3430 < self.player.real_x < 4158
            and self.stats["flags"]["good_dog"] is False
            and self.stats["flags"]["barn"] == True):
            if 3672 < self.player.real_x < 3711:
                if self.player.velocity > 0:
                    self.player.rect.y = 450
                    self.player.stage["x"] = -3108
                    self.player.real_x =  3700
            elif self.player.real_x > 3711:
                self.player.rect.y = 556

        if (3964 < self.player.real_x< 4216
            and {"tools", "valve"} == self.stats["inv"]
            and self.stats["flags"]["fabric"] is False):
            self.prompts["fabric"].float(rel_x)
        if (5632 < self.player.real_x< 5772
            and "valve" in self.stats["inv"]
            and self.stats["flags"]["pump"] is False):
            self.prompts["system"].float(rel_x)
        if (5771 < self.player.real_x< 5912
            and {"tools", "fabric"} == self.stats["inv"]
            and self.stats["flags"]["pump"] == True
            and self.stats["flags"]["plant"] is False):
            self.prompts["plant"].float(rel_x)

        if (6924 <self.player.real_x < 7232
            and self.stats["flags"]["greenhouse"] is False):
            self.prompts["greenhouse"].float(rel_x)
        if (6784 <self.player.real_x < 6952
            and self.stats["flags"]["greenhouse"]
            and "fabric" in self.stats["inv"]):
            self.prompts["repair"].float(rel_x)
        if (6951 <self.player.real_x < 7037
            and self.stats["flags"]["greenhouse"]
            and {"tools", "plant"} ==self.stats["inv"]):
            self.prompts["tube"].float(rel_x)
        if (7596 <self.player.real_x < 7764
            and self.stats["flags"]["planted"] is False
            and "plant" in self.stats["inv"]):
            self.prompts["hole"].float(rel_x)
        if (7763 <self.player.real_x < 8164
            and self.stats["flags"]["planted"]
            and self.stats["flags"]["cabbage"] is False
            and self.stats["flags"]["fixed"]):
            self.prompts["cabbage"].float(rel_x)
        if (8163 <self.player.real_x < 8416
            and self.stats["flags"]["fixed"] is False
            and "tube" in self.stats["inv"]):
            self.prompts["seeder_pump"].float(rel_x)

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
        if self.stats["flags"]["good_dog"] is True:
            self.screen.blit(self.props["special"], (4033-rel_x, 465))

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
        elif self.stats["inv"] == {"valve"}:
            self.screen.blit(self.inventory["valve"], (275, 813))
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
