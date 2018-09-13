import sys
import pygame

from gi.repository import Gtk
from scenarios.utils import utils, consts

class Credit:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.background = utils.load_image("credits/background.png", "menu")
        self.exit = utils.load_image("credits/exit.png", "menu")

    def run(self):
        """ control the actions happening on the credit modal"""

        running = True
        while running:
            while Gtk.events_pending():
                Gtk.main_iteration()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == consts.K_CIRCLE:
                        pygame.display.update(self.screen.blit(self.exit, (855, 123)))
                        pygame.time.delay(150)
                        running = False
                    elif  event.key == pygame.K_RETURN or event.key == consts.K_CHECK:
                        pygame.display.update(self.screen.blit(self.exit, (855, 123)))
                        pygame.time.delay(150)
                        running = False

            self.screen.blit(self.background, (0, 0))
            pygame.display.flip()
            self.clock.tick(consts.FPS)
