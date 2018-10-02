# named mapp just because i don't want
# a clash between this and the map function
import pygame

from gi.repository import Gtk
from scenarios.utils import utils
from scenarios.utils import consts
from scenarios.utils import saves
from scenarios.utils.button import Button

class Map:
    """
        Class representing the Map, recieves
        a Surface as a screen, a Clock as clock
    """
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.slot = saves.load()
        self.fx_channel = pygame.mixer.Channel(0)
        self.fx_channel.set_volume(consts.FX_VOLUME)
        self.vx_channel = pygame.mixer.Channel(1)
        self.vx_channel.set_volume(consts.VX_VOLUME)
        self.next_level = 1
        self.frame = 0
        self.real_level = 1

        self.session = {
            "stages": self.slot["stages"],
            "is_new?": True if self.slot["last_level_passed"]["code"] == 1 else False,
            "current_level":  self.slot["last_level_passed"]["code"],
            "completed": self.slot["stages"]["completado"]
        }

        if self.session["is_new?"]:
            self.current_slide = 1
            self.marker_level = 1
        else:
            self.current_slide = 2
            self.marker_level = self.session["current_level"]
            if self.marker_level == 6 and len(filter(lambda x: x is True, self.slot["stages"].values())) < 4:
                self.marker_level = 5
                self.real_level = 5
            elif self.marker_level == 2:
                self.real_level = 3
                self.marker_level = 3

        if self.session["completed"]:
            self.background = utils.load_image("good.png", "map")
        else:
            self.background = utils.load_image("bad.png", "map")

        self.modal = utils.load_image("modal.png", "map")
        self.denied = utils.load_fx("denied.ogg")

        self.parrot = {
            "0" : utils.load_image("marker1.png", "map"),
            "1" : utils.load_image("marker2.png", "map")
        }

        self.worlds = {
            "1" : utils.load_image("school.png", "map/worlds"),
            "2" : utils.load_image("city.png", "map/worlds"),
            "3" : utils.load_image("farm2.png", "map/worlds"),
            "4" : utils.load_image("farm.png", "map/worlds"),
            "5" : utils.load_image("river.png", "map/worlds"),
            "6" : utils.load_image("forest.png", "map/worlds")
        }

    def run(self):
        utils.load_bg("etwas.ogg")
        pygame.mixer.music.set_volume(consts.BG_VOLUME)
        pygame.mixer.music.play(-1, 0.0)
        running = True

        while running:
            self.screen.blit(self.background, (0, 0))
            self.render_scene()
            pygame.display.flip()
            self.clock.tick(consts.FPS)
            while Gtk.events_pending():
                Gtk.main_iteration()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.next_level = None
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == consts.K_CHECK:
                        if 0 < self.marker_level < 8:
                            self.next_level = self.real_level
                            running = False
                            utils.loading_screen(self.screen)
                        elif self.marker_level > 7:
                            self.next_level = 7
                            running = False
                            utils.loading_screen(self.screen)

                    elif event.key == pygame.K_LEFT or event.key == pygame.K_KP4:
                        if 1 < self.marker_level < 7:
                            if self.marker_level == 3:
                                self.marker_level = 1
                            else:
                                self.marker_level -= 1
                        elif self.marker_level >= 7:
                            self.marker_level = 6
                        else:
                            self.marker_level = 1
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                        if self.marker_level < 5:
                            if self.marker_level == 1:
                                self.marker_level = 3
                            else:
                                self.marker_level += 1
                        elif (self.marker_level == 6 and not self.slot["stages"]["bosque"]):
                            self.marker_level = 6
                        elif (4 < self.marker_level < 7 and
                              len(filter(lambda x: x is True, self.slot["stages"].values())) >= 5):
                            self.marker_level += 1
                        elif (self.marker_level == 5 and
                              len(filter(lambda x: x is True, self.slot["stages"].values())) < 5):
                            self.marker_level = 5
                            #if forest is not passed?
                        else:
                            self.marker_level = 7
                    elif event.key == pygame.K_ESCAPE or event.key == consts.K_CIRCLE:
                        self.current_slide = 2

    def render_scene(self):
        if self.current_slide == 1:
            self.screen.blit(self.modal, (0, 0))
        elif self.current_slide == 2:
            if not self.session["is_new?"]:
                self.load_worlds()
            self.animate_marker()

    def animate_marker(self):
        if self.marker_level == 1:
            pos = (314, 714) # school
            self.real_level = 1
        elif self.marker_level == 2:
            pos = (588, 410) # city
        elif self.marker_level == 4:
            pos = (114, 144) # Farm2
            self.real_level = 3
        elif self.marker_level == 3:
            pos = (205, 408) # Farm
            self.real_level = 4
        elif self.marker_level == 5:
            pos = (713, 108) # river
            self.real_level = 5
        elif self.marker_level == 6:
            pos = (885, 363) # forest
            self.real_level = 6
        elif self.session["completed"] or self.marker_level >= 7:
            pos = (902, 809) # vidar chapel
            self.real_level = 7
        self.frame += 1
        if self.frame > 9:
            self.frame = 0
        self.screen.blit(self.parrot[str(self.frame//5)], pos)

    def load_worlds(self):
        if not self.session["completed"]:
            if self.slot["stages"]["escuela"]:
                self.screen.blit(self.worlds["1"], (0, 0))
            if self.slot["stages"]["ciudad"]:
                self.screen.blit(self.worlds["2"], (0, 0))
            if self.slot["stages"]["granja2"]:
                self.screen.blit(self.worlds["3"], (0, 0))
            if self.slot["stages"]["granja"]:
                self.screen.blit(self.worlds["4"], (0, 0))
            if self.slot["stages"]["rio"]:
                self.screen.blit(self.worlds["5"], (0, 0))
            if self.slot["stages"]["bosque"]:
                self.screen.blit(self.worlds["6"], (0, 0))
