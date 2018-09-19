import pygame

from gi.repository import Gtk
from scenarios.utils import utils
from scenarios.utils import consts
from scenarios.utils.button import Button
from actors.player import Player
from actors.prompt import Prompt

class Library:
    """
        Class representing the library part of the  School level, recieves
        a Surface as a screen, and a Clock as clock
    """
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.fx_channel = pygame.mixer.Channel(0)
        self.fx_channel.set_volume(consts.FX_VOLUME)
        self.vx_channel = pygame.mixer.Channel(1)
        self.vx_channel.set_volume(consts.VX_VOLUME)
        self.character = "ena"
        self.background = utils.load_image("background2.png", "school")
        self.background_width = self.background.get_size()[0]
        self.current_slide = 2
        self.prompts = {
            "special": Prompt(self.screen,
                           self.clock,
                           (1094, 580),
                           "prompt.png",
                           "",
                           (520, 630))
        }
        self.props = {
            "special": utils.load_image("key_item.png", "school"),
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
            "1": utils.load_image("d1.png", "school/dialogue"), #parrot
        }

        self.icons = {
            "parrot": utils.load_image("parrot_icon.png", "school"),
        }

        self.show_bird_modal = False
        self.show_map_modal = False
        self.player = Player(self.screen,
                              self.clock,
                             (150, 620),
                             self.character,
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
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.props["special"], (1048, 642))
            self.render_scene(self.current_slide)
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
                        if self.current_slide == 2:
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
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                        if self.current_slide == 2:
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
                        elif self.current_slide == 1:
                            self.next.on_press(self.screen)
                            running = False
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_KP2:
                        if self.current_slide == 2 and self.focus == "game":
                            self.player.direction = "down"
                            self.player.y_velocity = abs(self.player.y_velocity)
                    elif event.key == pygame.K_UP or event.key == pygame.K_KP8:
                        if self.current_slide == 2 and self.focus == "game":
                            self.player.direction = "up"
                            self.player.y_velocity = -abs(self.player.y_velocity)
                    elif event.key == pygame.K_RETURN or event.key == consts.K_CHECK:
                        if self.current_slide == 2 and self.focus == "game":
                            self.player.running = True
                    elif event.key == pygame.K_SPACE or event.key == consts.K_CROSS:
                        if self.current_slide == 2:
                            if self.focus == "game":
                                if 929 < self.player.rect.x < 1201:
                                    self.current_slide = 1
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
                        if self.current_slide == 2:
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

    def render_scene(self, number):
        if number == 2:
            self.actors_load()
        elif number == 1:
            self.player.update()
            self.screen.blit(self.icons["parrot"], (9, 654))
            self.screen.blit(self.dialogue[str(number)], (139, 653))
            self.screen.blit(self.next.base, (1104, 703))

    def actors_load(self):
        if 929 < self.player.rect.x < 1201:
            self.prompts["special"].float(0)
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
