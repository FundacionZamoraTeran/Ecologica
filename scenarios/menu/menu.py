import pygame

from gi.repository import Gtk
from scenarios.utils import utils
from scenarios.utils import consts
from scenarios.utils.button import Button
from scenarios.menu import credits, options, help, exit, load


class Menu:
    """
       Class representing the start menu for the game, receives
       a Surface as screen, and a Clock as clock.
    """
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.background = utils.load_image("background.jpg", "menu")
        self.start = Button((23, 413),
                            "s1.jpg",
                            "s2.jpg",
                            156,
                            51,
                            "menu/start",
                            flag=True)
        self.load_but = Button((23, 413),
                               "l1.jpg",
                               "l2.jpg",
                               156,
                               51,
                               "menu/load")
        self.exit = Button((23, 413),
                           "e1.jpg",
                           "e2.jpg",
                           156,
                           51,
                           "menu/exit")
        self.options = Button((23, 413),
                              "o1.jpg",
                              "o2.jpg",
                              156,
                              51,
                              "menu/options")
        self.credits_but = Button((23, 413),
                                  "c1.jpg",
                                  "c2.jpg",
                                  156,
                                  51,
                                  "menu/credits")
        self.help_but = Button((23, 413),
                               "h1.jpg",
                               "h2.jpg",
                               156,
                               51,
                               "menu/help")
        self.level_selected = None
        self.slot_selected = None

    def run(self):
        """
           The main loop event for the menu
        """

        # Channels

        FX_CHANNEL = pygame.mixer.Channel(0)
        FX_CHANNEL.set_volume(consts.FX_VOLUME)
        VOICE_CHANNEL = pygame.mixer.Channel(1)
        VOICE_CHANNEL.set_volume(consts.VX_VOLUME)

        utils.load_bg("meny.ogg")
        pygame.mixer.music.set_volume(consts.BG_VOLUME)
        pygame.mixer.music.play(-1, 0.0)

        running = True
        while running:
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.credits_but.base, (168, 760))
            self.screen.blit(self.options.base, (345, 760))
            self.screen.blit(self.start.end, (524, 760))
            self.screen.blit(self.load_but.base, (701, 760))
            self.screen.blit(self.help_but.base, (877, 760))
            self.screen.blit(self.exit.base, (985, 46))
            pygame.display.flip()
            self.clock.tick(consts.FPS)
            while Gtk.events_pending():
                Gtk.main_iteration()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == consts.K_CHECK:
                        if self.start.flag is True:
                            self.level_selected = 0
                            utils.loading_screen(self.screen)
                        elif self.load_but.flag is True:
                            load_state = load.Load(self.screen, self.clock)
                            load_state.run()
                            if load_state.level_selected is not None:
                                self.level_selected = "m"
                                running = False
                            del load_state
                            utils.loading_screen(self.screen)
                        elif self.credits_but.flag is True:
                            credit = credits.Credit(self.screen, self.clock)
                            credit.run()
                            del credit
                        elif self.options.flag is True:
                            option = options.Option(self.screen, self.clock)
                            option.run()
                            del option
                        elif self.exit.flag is True:
                            ext = exit.Exit(self.screen, self.clock)
                            ext.run()
                            del ext
                            #running = False
                        elif self.help_but.flag is True:
                            hjelp = help.Help(self.screen, self.clock)
                            hjelp.run()
                            del hjelp
                    if event.key == pygame.K_LEFT or event.key == pygame.K_KP4:
                        if self.start.flag is True:
                            self.start.flag = False
                            self.options.flag = True
                            self.start.on_focus(self.screen)
                            self.options.on_focus(self.screen)
                        elif self.options.flag is True:
                            self.options.flag = False
                            self.credits_but.flag = True
                            self.options.on_focus(self.screen)
                            self.credits_but.on_focus(self.screen)
                        elif self.load_but.flag is True:
                            self.load_but.flag = False
                            self.start.flag = True
                            self.load_but.on_focus(self.screen)
                            self.start.on_focus(self.screen)
                        elif self.help_but.flag is True:
                            self.help_but.flag = False
                            self.load_but.flag = True
                            self.help_but.on_focus(self.screen)
                            self.load_but.on_focus(self.screen)
                        elif self.exit.flag is True:
                            self.exit.flag = False
                            self.help_but.flag = True
                            self.exit.on_focus(self.screen)
                            self.help_but.on_focus(self.screen)
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                        if self.start.flag is True:
                            self.start.flag = False
                            self.load_but.flag = True
                            self.start.on_focus(self.screen)
                            self.load_but.on_focus(self.screen)
                        elif self.load_but.flag is True:
                            self.load_but.flag = False
                            self.help_but.flag = True
                            self.load_but.on_focus(self.screen)
                            self.help_but.on_focus(self.screen)
                        elif self.help_but.flag is True:
                            self.help_but.flag = False
                            self.exit.flag = True
                            self.help_but.on_focus(self.screen)
                            self.exit.on_focus(self.screen)
                        elif self.options.flag is True:
                            self.options.flag = False
                            self.start.flag = True
                            self.options.on_focus(self.screen)
                            self.start.on_focus(self.screen)
                        elif self.credits_but.flag is True:
                            self.credits_but.flag = False
                            self.options.flag = True
                            self.credits_but.on_focus(self.screen)
                            self.options.on_focus(self.screen)
