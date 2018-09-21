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
        Class representing the second Farm level, recieves
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
        self.character = "diego"
        self.background = utils.load_image("background.png", "farm2")
        self.background_width = self.background.get_size()[0]
        self.current_slide = 1
        self.prompts = {
            "plant": Prompt(self.screen,
                            self.clock,
                            (716, 525),
                            "prompt.png",
                            "",
                            (440, 550)),
            "house": Prompt(self.screen,
                            self.clock,
                            (1989, 410),
                            "prompt.png",
                            "",
                            (350, 430)),
            "tape": Prompt(self.screen,
                           self.clock,
                           (2075, 340),
                           "prompt.png",
                           "",
                           (290, 360)),
            "abattoir": Prompt(self.screen,
                            self.clock,
                            (3798, 420),
                            "prompt.png",
                            "",
                            (350, 470)),
            "cattle": Prompt(self.screen,
                            self.clock,
                            (4352, 410),
                            "prompt.png",
                            "",
                            (350, 480)),
            "cover": Prompt(self.screen,
                            self.clock,
                            (4840, 460),
                            "prompt.png",
                            "",
                            (400, 500)),
            "dump": Prompt(self.screen,
                            self.clock,
                            (7852, 440),
                            "prompt.png",
                            "",
                            (360, 500)),
            "special": Prompt(self.screen,
                            self.clock,
                              (6270, 500),
                            "prompt.png",
                            "",
                            (430, 540))
        }
        self.props = {
            "plant": utils.load_image("plant.png", "farm2"),
            "cover": utils.load_image("cover.png", "farm2"),
            "tape": utils.load_image("tape.png", "farm2"),
            "special": utils.load_image("key_item.png", "farm2"),
            "house": (utils.load_image("base.png", "farm2/house"),
                      utils.load_image("inside1.png", "farm2/house"),
                      utils.load_image("inside2.png", "farm2/house")),
            "pasture": utils.load_image("pasture.png", "farm2"),
            "stable": utils.load_image("stable.png", "farm2"),
            "abattoir": (utils.load_image("base.png", "farm2/abattoir"),
                         utils.load_image("fixed.png", "farm2/abattoir")),
            "cow": (utils.load_image("cow1.png", "farm2"),
                    utils.load_image("cow2.png", "farm2")),
            "bull": (utils.load_image("bull1.png", "farm2"),
                    utils.load_image("bull2.png", "farm2")),
            "dump": (utils.load_image("base.png", "farm2/dump"),
                    utils.load_image("closed.png", "farm2/dump"))

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
            "bird_modal_1": utils.load_image("h1.png", "farm2/HUD"),
            "bird_modal_2": utils.load_image("h2.png", "farm2/HUD"),
            "bird_modal_3": utils.load_image("h3.png", "farm2/HUD"),
            "bird_modal_4": utils.load_image("h4.png", "farm2/HUD"),
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
            "unfocused_bag": utils.load_image("bag1.png", "farm2/HUD"),
            "focused_bag": utils.load_image("bag2.png", "farm2/HUD"),
            "plant": utils.load_image("plant.png", "farm2/HUD"),
            "tape": utils.load_image("tape.png", "farm2/HUD"),
            "key": utils.load_image("key.png", "farm2/HUD"),
            "cover": utils.load_image("cover.png", "farm2/HUD")
        }

        self.stats = {
            "inv": {}, # the items the player has
            "flags": {
                "plant": False, # the item is visible on map
                "house": False, #is not showing inside
                "tape": False, # the item is visible on map
                "cover": False, # the item is visible on map
                "fixed": False, # pipe is not taped
                "eating": False, # cattle have no food
                "covered": False, # dump is not covered
            }
        }

        self.dialogue = {
            "1": utils.load_image("d1.png", "farm2/dialogue"),#hen
            "2": utils.load_image("d2.png", "farm2/dialogue"),
            "3": utils.load_image("d3.png", "farm2/dialogue"),
            "4": utils.load_image("d4.png", "farm2/dialogue"),#diego
            "5": utils.load_image("d5.png", "farm2/dialogue"),
            "6": utils.load_image("d6.png", "farm2/dialogue"),
            "7": utils.load_image("d7.png", "farm2/dialogue"),
            "8": utils.load_image("d8.png", "farm2/dialogue"),
            "9": utils.load_image("d9.png", "farm2/dialogue"),
            "10": utils.load_image("d10.png", "farm2/dialogue"),
            "11": utils.load_image("d11.png", "farm2/dialogue"), #hen
            "12": utils.load_image("d12.png", "farm2/dialogue"),
        }

        self.icons = {
            "diego": utils.load_image("diego_icon.png", "farm2"),
            "hen": utils.load_image("hen_icon.png", "farm2")
        }
        self.show_bird_modal = False
        self.show_map_modal = False
        self.player = Player(self.screen,
                              self.clock,
                             (150, 520),
                             self.character,
                             9591,
                             True)
        self.focus = "game"

        self.prev = Button((178, 693),
                           "prev1.png",
                           "prev2.png",
                           48,
                           42,
                           "farm2")
        self.next = Button((1104, 693),
                           "next1.png",
                           "next2.png",
                           48,
                           42,
                           "farm2")

    def run(self):
        utils.load_bg("mazurk.ogg")
        pygame.mixer.music.set_volume(consts.BG_VOLUME)
        pygame.mixer.music.play(-1, 0.0)
        running = True
        while running:
            rel_x = self.player.stage["x"]
            if rel_x < consts.WIDTH_SCREEN:
                self.screen.blit(self.background, (rel_x, -100))
                self.screen.blit(self.props["pasture"], (387-abs(rel_x), 515))
                if self.stats["flags"]["plant"] is False:
                    self.screen.blit(self.props["plant"], (718-abs(rel_x), 590))

                if self.stats["flags"]["house"]:
                    if self.stats["flags"]["tape"]:
                        self.screen.blit(self.props["house"][1], (1844-abs(rel_x), 187))
                    else:
                        self.screen.blit(self.props["house"][2], (1844-abs(rel_x), 187))
                else:
                    self.screen.blit(self.props["house"][0], (1844-abs(rel_x), 187))
                if self.stats["flags"]["fixed"]:
                    self.screen.blit(self.props["abattoir"][1], (3278-abs(rel_x), 210))
                else:
                    self.screen.blit(self.props["abattoir"][0], (3278-abs(rel_x), 210))
                if self.stats["flags"]["cover"] is False:
                    self.screen.blit(self.props["cover"], (4730-abs(rel_x), 532))
                if self.stats["flags"]["eating"]:
                    self.screen.blit(self.props["cow"][1], (4241-abs(rel_x), 482))
                    self.screen.blit(self.props["cow"][1], (4394-abs(rel_x), 548))
                    self.screen.blit(self.props["bull"][1], (4630-abs(rel_x), 521))
                    self.screen.blit(self.props["cow"][1], (5022-abs(rel_x), 483))
                else:
                    self.screen.blit(self.props["cow"][0], (4241-abs(rel_x), 482))
                    self.screen.blit(self.props["cow"][0], (4394-abs(rel_x), 548))
                    self.screen.blit(self.props["bull"][0], (4630-abs(rel_x), 521))
                    self.screen.blit(self.props["cow"][0], (5022-abs(rel_x), 483))
                self.screen.blit(self.props["stable"], (5524-abs(rel_x), 238))
                if self.stats["flags"]["covered"]:
                    self.screen.blit(self.props["special"], (6255-abs(rel_x), 569))
                    self.screen.blit(self.props["dump"][1], (7751-abs(rel_x), 518))
                else:
                    self.screen.blit(self.props["dump"][0], (5751-abs(rel_x), 347))
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
                        if self.current_slide == 13:
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
                              or self.current_slide == 12):
                            self.prev.on_press(self.screen)
                            self.current_slide -= 1
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                        if self.current_slide == 13:
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
                        elif self.current_slide in (1, 2, 3, 11):
                            self.next.on_press(self.screen)
                            self.current_slide += 1
                        elif 3 < self.current_slide < 11:
                            self.next.on_press(self.screen)
                            self.current_slide = 13
                        elif self.current_slide == 12:
                            running = False
                            utils.loading_screen(self.screen)
                            #save here
                            if not self.slot["stages"]["granja2"] is True:
                                saves.save(4, "Granja de Crianza", "granja2")
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_KP2:
                        if self.current_slide == 13 and self.focus == "game":
                            self.player.direction = "down"
                            self.player.y_velocity = abs(self.player.y_velocity)
                    elif event.key == pygame.K_UP or event.key == pygame.K_KP8:
                        if self.current_slide == 13 and self.focus == "game":
                            self.player.direction = "up"
                            self.player.y_velocity = -abs(self.player.y_velocity)
                    elif event.key == pygame.K_RETURN or event.key == consts.K_CHECK:
                        if self.current_slide == 13 and self.focus == "game":
                            self.player.running = True
                    elif event.key == pygame.K_SPACE or event.key == consts.K_CROSS:
                        if self.current_slide == 13:
                            if self.focus == "game":
                                if (604 < self.player.real_x < 772
                                    and not self.stats["flags"]["plant"]):
                                    self.stats["flags"]["plant"] = True
                                    self.stats["inv"] = {"plant"}

                                #house
                                if (1832 < self.player.real_x < 2056
                                    and not self.stats["flags"]["house"]):
                                    self.stats["flags"]["house"] = True
                                    self.current_slide = 5
                                elif (2055 < self.player.real_x < 2157
                                      and self.stats["flags"]["house"]
                                      and not self.stats["flags"]["tape"]
                                      and "plant" in self.stats["inv"]):
                                    self.stats["flags"]["tape"] = True
                                    self.stats["inv"] = {"plant", "tape"}
                                    self.current_slide = 10
                                if (3720 < self.player.real_x < 3861
                                    and not self.stats["flags"]["fixed"]
                                    and "tape" in self.stats["inv"]):
                                    self.stats["flags"]["fixed"] = True
                                    self.stats["inv"] = {"plant"}
                                    self.current_slide = 6
                                if (4000 < self.player.real_x < 4197
                                    and self.stats["flags"]["fixed"]
                                    and not self.stats["flags"]["eating"]
                                    and "plant" in self.stats["inv"]):
                                    self.stats["flags"]["eating"] = True
                                    self.stats["inv"] = {}
                                    self.current_slide = 7
                                if (4696 < self.player.real_x < 5005
                                    and not self.stats["flags"]["cover"]):
                                    self.stats["flags"]["cover"] = True
                                    self.stats["inv"] = {"cover"}
                                    self.current_slide = 9
                                if (7634 < self.player.real_x < 7970
                                    and not self.stats["flags"]["covered"]):
                                    self.stats["flags"]["covered"] = True
                                    self.stats["inv"] = {}
                                    self.current_slide = 8
                                if (6120 < self.player.real_x < 6334
                                    and self.stats["flags"]["covered"]):
                                    self.current_slide = 11

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
                        if self.current_slide == 13:
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
        if number == 13:
            self.actors_load(rel_x)
        elif number in (1, 11):
            self.player.update()
            self.screen.blit(self.icons["hen"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.next.base, (1104, 693))
        elif number in (2, 3, 12):
            self.player.update()
            self.screen.blit(self.icons["hen"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.prev.base, (178, 693))
            self.screen.blit(self.next.base, (1104, 693))
        elif number == 4:
            self.player.update()
            self.screen.blit(self.icons["diego"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.prev.base, (178, 693))
            self.screen.blit(self.next.base, (1104, 693))
        elif 4 < number < 11:
            #diego commenting on an item
            self.player.update()
            self.screen.blit(self.icons["diego"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.next.base, (1104, 693))

    def actors_load(self, rel_x):
        if (604 < self.player.real_x < 772
            and not self.stats["flags"]["plant"]):
            self.prompts["plant"].float(rel_x)
        if (1832 < self.player.real_x < 2056
            and not self.stats["flags"]["house"]):
            self.prompts["house"].float(rel_x)
        if (2055 < self.player.real_x < 2157
            and self.stats["flags"]["house"]
            and not self.stats["flags"]["tape"]
            and "plant" in self.stats["inv"]):
            self.prompts["tape"].float(rel_x)
        if (3720 < self.player.real_x < 3861
            and not self.stats["flags"]["fixed"]
            and "tape" in self.stats["inv"]):
            self.prompts["abattoir"].float(rel_x)
        if (4000 < self.player.real_x < 4197
            and not self.stats["flags"]["eating"]
            and self.stats["flags"]["fixed"]
            and "plant" in self.stats["inv"]):
            self.prompts["cattle"].float(rel_x)
        if (self.player.real_x > 4196
            and not self.stats["flags"]["eating"]):
            if self.player.velocity > 0:
                self.player.stage["x"] = -3620
                self.player.real_x = 4196
        if (4696 < self.player.real_x < 5005
            and not self.stats["flags"]["cover"]):
            self.prompts["cover"].float(rel_x)
        if (5998 < self.player.real_x < 6901
            and self.player.rect.y < 570
            and not self.stats["flags"]["covered"]):
            if self.player.velocity > 0:
                self.player.rect.y = 569
        if (7634 < self.player.real_x < 7970
            and not self.stats["flags"]["covered"]):
            self.prompts["dump"].float(rel_x)
        if (6120 < self.player.real_x < 6334
            and self.stats["flags"]["covered"]):
            self.prompts["special"].float(rel_x)
        self.player.update()

    def load_hud(self):
        #top icons
        self.screen.blit(self.hud["bird_icon"].end, (1053, 15))
        self.screen.blit(self.hud["map_icon"].base, (903, 15))
        if self.show_bird_modal:
            if self.stats["flags"]["tape"]:
                self.screen.blit(self.hud["bird_modal_2"], (0, 0))
            elif self.stats["flags"]["eating"]:
                self.screen.blit(self.hud["bird_modal_3"], (0, 0))
            elif self.stats["flags"]["covered"]:
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
        if self.stats["inv"] == {"plant"}:
            self.screen.blit(self.inventory["plant"],  (300, 833))
        elif self.stats["inv"] == {"plant", "tape"}:
            self.screen.blit(self.inventory["plant"],  (300, 833))
            self.screen.blit(self.inventory["tape"], (425, 835))
        elif self.stats["inv"] == {"cover"}:
            self.screen.blit(self.inventory["cover"], (300, 839))

        # self.screen.blit(self.inventory["plant"], (300, 833))
        # self.screen.blit(self.inventory["tape"], (425, 835))
        # self.screen.blit(self.inventory["cover"], (530, 839))
