import sys
import os
import pygame

from gi.repository import Gtk
from scenarios.utils import utils, consts
from scenarios.utils.button import Button
from scenarios.menu.slider import Slider

MAIN_DIR = os.path.split(os.path.abspath(__file__))[0]

class Option:
    def __init__(self, screen, clock):
        self.screen = screen
        self.opts = ()
        self.path = os.path.join(MAIN_DIR, "../../config.ini")
        with open(self.path, "r+") as f:
            from ast import literal_eval
            self.opts = literal_eval(f.read()) # tuple (vx,bg,fx)
        self.clock = clock
        self.background = utils.load_image("background.jpg", "menu/options")
        self.fx_slider = Slider((310, 591),
                            "menu/options",
                            level=self.opts[2],
                            flag=True)
        self.music_slider = Slider((380, 480),
                                   "menu/options",
                                   level=self.opts[1])

        self.exit = utils.load_image("credits/exit.png", "menu")

    def save(self):
        opts = (1.0, self.music_slider.level, self.fx_slider.level)
        with open(self.path, "w") as f:
            f.write(str(opts))

    def run(self):
        """ control the actions happening on the Help modal """
        running = True
        while running:
            while Gtk.events_pending():
                Gtk.main_iteration()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == consts.K_CIRCLE:
                        pygame.display.update(self.screen.blit(self.exit, (602, 447)))
                        pygame.time.delay(150)
                        running = False
                        self.save()
                        pygame.mixer.music.set_volume(self.opts[1])
                    elif event.key == pygame.K_RETURN or event.key == consts.K_CHECK:
                        pygame.display.update(self.screen.blit(self.exit, (602, 447)))
                        pygame.time.delay(150)
                        running = False
                        self.save()
                        pygame.mixer.music.set_volume(self.opts[1])
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_KP2:
                        if self.fx_slider.flag is True:
                            self.fx_slider.flag = False
                            self.music_slider.flag = True
                    elif event.key == pygame.K_UP or event.key == pygame.K_KP8:
                        if self.music_slider.flag is True:
                            self.music_slider.flag = False
                            self.fx_slider.flag = True
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                        if self.music_slider.flag is True:
                            self.music_slider.increase_level(self.screen)
                        elif self.fx_slider.flag is True:
                            self.fx_slider.increase_level(self.screen)
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_KP4:
                        if self.music_slider.flag is True:
                            self.music_slider.decrease_level(self.screen)
                        elif self.fx_slider.flag is True:
                            self.fx_slider.decrease_level(self.screen)

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.fx_slider.get_current_level_image(), (300, 531))
            self.screen.blit(self.music_slider.get_current_level_image(), (300, 663))
            pygame.display.flip()
            self.clock.tick(consts.FPS)
