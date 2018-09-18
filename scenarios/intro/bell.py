import sys
import pygame

from gi.repository import Gtk
from scenarios.utils import utils
from scenarios.utils import consts
from scenarios.utils.button import Button
from scenarios.intro import book

class Bell:
    """
        Class representing the bell transition of the intro comic,
        recieves a Surface as a screen, and a Clock as clock
    """
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.fx_channel = pygame.mixer.Channel(0)
        self.fx_channel.set_volume(consts.FX_VOLUME)
        self.vx_channel = pygame.mixer.Channel(1)
        self.vx_channel.set_volume(consts.VX_VOLUME)
        self.frame = 0

        self.bell = (
            utils.load_image("1.png", "intro/screen_6"),
            utils.load_image("2.png", "intro/screen_6"),
            utils.load_image("3.png", "intro/screen_6")
        )
        self.ring = utils.load_fx("bell.ogg")
        self.text = utils.load_image("d1.png", "intro/screen_6")

        self.next = Button((908, 747),
                           "next1.png",
                           "next2.png",
                           48,
                           42,
                           "intro")

    def run(self):
        utils.load_bg("khachaturian.ogg")
        pygame.mixer.music.set_volume(consts.BG_VOLUME)
        pygame.mixer.music.play(-1, 0.0)
        running = True

        while running:
            if not self.fx_channel.get_busy():
                self.fx_channel.play(self.ring)
            self.frame += 1
            if self.frame > 5:
                self.frame = 0
            self.screen.blit(self.bell[self.frame//2], (0, 0))
            self.screen.blit(self.text, (240, 700))
            self.screen.blit(self.next.base, (908, 747))

            pygame.display.flip()
            self.clock.tick(consts.FPS)

            while Gtk.events_pending():
                Gtk.main_iteration()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                        self.next.on_press(self.screen)
                        utils.loading_screen(self.screen)
                        boo = book.Book(self.screen, self.clock)
                        boo.run()
                        del boo
                        running = False
