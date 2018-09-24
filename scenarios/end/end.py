import pygame

from gi.repository import Gtk
from scenarios.utils import utils
from scenarios.utils import consts
from scenarios.utils import saves
from scenarios.utils.button import Button

class End:
    """
        Class representing the end comic, recieves
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
        self.background_1 = utils.load_image("background1.png", "end")
        self.background_2 = utils.load_image("background2.png", "end")
        self.background_3 = utils.load_image("background3.png", "end")
        self.background_4 = utils.load_image("background4.png", "end")
        self.current_slide = 1

        self.dialogue = {
            "1": utils.load_image("d1.png", "end/dialogue"), # cesar
            "2": utils.load_image("d2.png", "end/dialogue"), # ena
            "3": utils.load_image("d3.png", "end/dialogue"), # ezer
            "4": utils.load_image("d4.png", "end/dialogue"), # diego
            "5": utils.load_image("d5.png", "end/dialogue"), # vidar
            "6": utils.load_image("d6.png", "end/dialogue"),
            "7": utils.load_image("d7.png", "end/dialogue"), # ena
            "8": utils.load_image("d8.png", "end/dialogue"),
            "9": utils.load_image("d9.png", "end/dialogue"),
            "10": utils.load_image("d10.png", "end/dialogue"), # vidar
            "11": utils.load_image("d11.png", "end/dialogue"),
            "12": utils.load_image("d12.png", "end/dialogue"),
            "13": utils.load_image("d13.png", "end/dialogue")
        }


        self.modal = {
            "modal": utils.load_image("modal.png", "end"),
            "exit": utils.load_image("exit.png", "end"),
            "replay": utils.load_image("replay.png", "end")
        }

        self.icons = {
            "cesar": utils.load_image("cesar_icon.png", "end"),
            "ena": utils.load_image("ena_icon.png", "end"),
            "diego": utils.load_image("diego_icon.png", "end"),
            "ezer": utils.load_image("ezer_icon.png", "end"),
            "vidar": utils.load_image("vidar_icon.png", "end")
        }

        self.replay = False

        self.prev = Button((178, 803),
                           "prev1.png",
                           "prev2.png",
                           48,
                           42,
                           "end")
        self.next = Button((1104, 803),
                           "next1.png",
                           "next2.png",
                           48,
                           42,
                           "end")

    def run(self):
        utils.load_bg("vidar.ogg")
        pygame.mixer.music.set_volume(consts.BG_VOLUME)
        pygame.mixer.music.play(-1, 0.0)
        running = True
        while running:
            self.render_scene(self.current_slide)
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
                        if self.current_slide == 14:
                            pass
                        elif 1 < self.current_slide:
                            self.prev.on_press(self.screen)
                            self.current_slide -= 1
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                        if self.current_slide < 14:
                            self.next.on_press(self.screen)
                            self.current_slide += 1
                    elif event.key == pygame.K_UP or event.key == pygame.K_KP8:
                        self.replay = True
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_KP2:
                        self.replay = False
                    elif event.key == pygame.K_RETURN or event.key == consts.K_CHECK:
                        running = False
                        utils.loading_screen(self.screen)
                        #save here
                        if not self.slot["stages"]["completado"] is True:
                            saves.save(8, "Completado", "completado")
                        if not self.replay:
                            self.next_level = None

    def render_scene(self, number):
        if number == 1:
            self.screen.blit(self.background_1, (0, 0))
            self.screen.blit(self.icons["cesar"], (9, 754))
            self.screen.blit(self.dialogue[str(number)], (139, 753))
            self.screen.blit(self.next.base, (1104, 803))
        elif number == 2:
            self.screen.blit(self.background_1, (0, 0))
            self.screen.blit(self.icons["ena"], (9, 754))
            self.screen.blit(self.dialogue[str(number)], (139, 753))
            self.screen.blit(self.prev.base, (178, 803))
            self.screen.blit(self.next.base, (1104, 803))
        elif number == 3:
            self.screen.blit(self.background_2, (0, 0))
            self.screen.blit(self.icons["ezer"], (9, 754))
            self.screen.blit(self.dialogue[str(number)], (139, 753))
            self.screen.blit(self.prev.base, (178, 803))
            self.screen.blit(self.next.base, (1104, 803))
        elif number == 4:
            self.screen.blit(self.background_2, (0, 0))
            self.screen.blit(self.icons["diego"], (9, 754))
            self.screen.blit(self.dialogue[str(number)], (139, 753))
            self.screen.blit(self.prev.base, (178, 803))
            self.screen.blit(self.next.base, (1104, 803))
        elif number in (5, 6, 10, 11, 12):
            self.screen.blit(self.background_3, (0, 0))
            self.screen.blit(self.icons["vidar"], (9, 754))
            self.screen.blit(self.dialogue[str(number)], (139, 753))
            self.screen.blit(self.prev.base, (178, 803))
            self.screen.blit(self.next.base, (1104, 803))
        elif number in (7, 8, 9):
            self.screen.blit(self.background_3, (0, 0))
            self.screen.blit(self.icons["ena"], (9, 754))
            self.screen.blit(self.dialogue[str(number)], (139, 753))
            self.screen.blit(self.prev.base, (178, 803))
            self.screen.blit(self.next.base, (1104, 803))
        elif number == 13:
            self.screen.blit(self.background_4, (0, 0))
            self.screen.blit(self.icons["vidar"], (9, 754))
            self.screen.blit(self.dialogue[str(number)], (139, 753))
            self.screen.blit(self.prev.base, (178, 803))
            self.screen.blit(self.next.base, (1104, 803))
        elif number == 14:
            self.screen.blit(self.background_4, (0, 0))
            self.screen.blit(self.modal["modal"], (0, 0))
            if self.replay:
                self.screen.blit(self.modal["replay"], (357, 425))
            else:
                self.screen.blit(self.modal["exit"], (357, 545))

