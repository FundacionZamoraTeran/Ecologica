import sys
import pygame

from gi.repository import Gtk
from scenarios.utils import utils, consts, saves

class Load:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.background = utils.load_image("load/background.png", "menu")
        self.save = saves.load()
        if self.save == None or self.save == {}:
            self.slot1 = utils.load_image("load/new.png", "menu")
        else:
            self.last_level_code = self.save["last_level_passed"]["code"]
            self.slot1 = utils.load_image("load/"+str(self.last_level_code)+".png", "menu")

        self.level_selected = None
        self.fx_channel = pygame.mixer.Channel(0)
        self.exit = utils.load_image("load/exit.png", "menu")

    def run(self):
        """
            control the actions happening on the load modal
        """
        running = True
        while running:
            while Gtk.events_pending():
                Gtk.main_iteration()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == consts.K_CIRCLE:
                        pygame.display.update(self.screen.blit(self.exit, (907, 223)))
                        pygame.time.delay(150)
                        running = False
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_END:
                        if self.save is None or self.save == {}:
                            self.fx_channel.play(utils.load_fx("denied.ogg"))
                        else:
                            self.level_selected = "m"
                            running = False

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.slot1, (292, 474))
            pygame.display.flip()
            self.clock.tick(consts.FPS)
