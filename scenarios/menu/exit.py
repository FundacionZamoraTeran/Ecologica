import sys
import pygame

from gi.repository import Gtk
from scenarios.utils import utils, consts
from scenarios.utils.button import Button

class Exit:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.background = utils.load_image("exit/background.png", "menu")
        self.yes = Button((503, 441),
                          "yes1.png",
                          "yes2.png",
                          83,
                          56,
                          "menu/exit",
                          flag=True)
        self.no = Button((611, 441),
                         "no1.png",
                         "no2.png",
                         83,
                         56,
                         "menu/exit")

    def run(self):
        """ control the actions happening on the exit modal"""

        running = True
        while running:
            while Gtk.events_pending():
                Gtk.main_iteration()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == consts.K_CIRCLE:
                        running = False
                    elif  event.key == pygame.K_RETURN or event.key == consts.K_CHECK:
                        if self.yes.flag is True:
                            sys.exit(0)
                        elif self.no.flag is True:
                            running = False
                    if event.key == pygame.K_LEFT or event.key == pygame.K_KP4:
                        if self.no.flag is True:
                            self.no.flag = False
                            self.yes.flag = True
                            self.no.on_focus(self.screen)
                            self.yes.on_focus(self.screen)
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                        if self.yes.flag is True:
                            self.yes.flag = False
                            self.no.flag = True
                            self.yes.on_focus(self.screen)
                            self.no.on_focus(self.screen)

            self.screen.blit(self.background, (390, 200))
            self.screen.blit(self.yes.end, (503, 441))
            self.screen.blit(self.no.base, (611, 441))
            pygame.display.flip()
            self.clock.tick(consts.FPS)
