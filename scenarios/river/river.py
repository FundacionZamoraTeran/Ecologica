import pygame

from gi.repository import Gtk
from scenarios.utils import utils
from scenarios.utils import consts
from scenarios.utils import saves
from scenarios.utils.button import Button
from actors.player import Player
from actors.prompt import Prompt


class River:
    """
        Class representing the River level, recieves
        a Surface as a screen, and a Clock as clock
    """
    #251x356
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.slot = saves.load()
        self.fx_channel = pygame.mixer.Channel(0)
        self.fx_channel.set_volume(consts.FX_VOLUME)
        self.vx_channel = pygame.mixer.Channel(1)
        self.vx_channel.set_volume(consts.VX_VOLUME)
        self.next_level = 1
        self.character = "ezer"
        self.background = utils.load_image("background.png", "river")
        self.background_width = self.background.get_size()[0]
        self.interact = Prompt(self.screen,
                               self.clock,
                               (635, 480),
                               "prompt.png",
                               "",
                               (400, 600))
        self.money = utils.load_image("money.png", "river")
        self.net = utils.load_image("net.png", "river")
        self.stumps = utils.load_image("stumps.png", "river")
        self.logger = utils.load_image("logger1.png", "river")
        self.cabin = utils.load_image("open.png", "river/cabin")
        self.bridge = utils.load_image("base.png", "river/bridge")
        self.handrail = utils.load_image("handrail.png", "river/bridge")
        self.trash = utils.load_image("trash.png", "river")
        self.canoe = utils.load_image("canoe.png", "river")
        self.tree_1 = utils.load_image("tree_1.png", "river")
        self.fish = utils.load_image("0.png", "river/fish")
        self.tree_2 = utils.load_image("tree_2.png", "river")
        self.purifier = utils.load_image("open.png", "river/purifier")
        self.tree_3 = utils.load_image("tree_3.png", "river")
        self.fence = utils.load_image("closed.png", "river/fence")
        self.special = utils.load_image("key_item.png", "river")
        self.guard = utils.load_image("guard.png", "river")

        self.player = Player(self.screen,
                              self.clock,
                             (150, 620),
                             self.character,
                             9600,
                             True)
        self.visited = [False, False]

    def run(self):
        utils.load_bg("hungarian.ogg")
        pygame.mixer.music.set_volume(consts.BG_VOLUME)
        pygame.mixer.music.play(-1, 0.0)
        running = True

        while running:
            rel_x = self.player.stage["x"]
            if rel_x < consts.WIDTH_SCREEN:
                self.screen.blit(self.background, (rel_x, -100))
                self.screen.blit(self.money, (523-abs(rel_x), 617))
                self.screen.blit(self.net, (565-abs(rel_x), 528))
                self.screen.blit(self.stumps, (992-abs(rel_x), 432))
                self.screen.blit(self.logger, (2415-abs(rel_x), 405))
                self.screen.blit(self.cabin, (3240-abs(rel_x), 220))
                self.screen.blit(self.bridge, (4104-abs(rel_x), 482))
                self.screen.blit(self.trash, (4333-abs(rel_x), 678))
                self.screen.blit(self.canoe, (4678-abs(rel_x), 650))
                self.screen.blit(self.tree_1, (4673-abs(rel_x), -100))
                self.screen.blit(self.fish, (5539-abs(rel_x), 690))
                self.screen.blit(self.tree_2, (5863-abs(rel_x), -100))
                self.screen.blit(self.purifier, (6079-abs(rel_x), 183))
                self.screen.blit(self.tree_3, (7347-abs(rel_x), -100))
                self.screen.blit(self.fence, (8209-abs(rel_x), 398))
                self.screen.blit(self.special, (8815-abs(rel_x), 326))
                self.screen.blit(self.guard, (8920-abs(rel_x), 501))
                self.actors_load(abs(rel_x))
                self.screen.blit(self.handrail, (4236-abs(rel_x), 548))
            pygame.display.flip()
            self.clock.tick(consts.FPS)
            while Gtk.events_pending():
                Gtk.main_iteration()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.next_level = None
                if event.type == pygame.KEYDOWN:
                    pass
                    if event.key == pygame.K_LEFT or event.key == pygame.K_KP4:
                        self.player.direction = "left"
                        self.player.running_velocity = -abs(self.player.running_velocity)
                        self.player.velocity = -abs(self.player.velocity)
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                        self.player.direction = "right"
                        self.player.running_velocity = abs(self.player.running_velocity)
                        self.player.velocity = abs(self.player.velocity)
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_KP2:
                        self.player.direction = "down"
                        self.player.y_velocity = abs(self.player.y_velocity)
                    elif event.key == pygame.K_UP or event.key == pygame.K_KP8:
                        self.player.direction = "up"
                        self.player.y_velocity = -abs(self.player.y_velocity)
                    elif event.key == pygame.K_RETURN or event.key == consts.K_CHECK:
                        self.player.running = True
                    elif event.key == pygame.K_SPACE or event.key == consts.K_CROSS:
                        pass
                        # move the focus to the contextual menu if present.
                    elif event.key == pygame.K_ESCAPE or event.key == consts.K_CIRCLE:
                        pass
                        # move focus to upper menu bar

                    #     if (self.player.real_x+self.player.rect.width > 620
                    #             and self.player.real_x+self.player.rect.width < 745):
                    #         utils.loading_screen(self.screen)
                    #         mid = middle.Middle(self.screen, self.clock, self.character)
                    #         mid.run()
                    #         del mid
                    #         running = False
                    #         utils.loading_screen(self.screen)
                    #         #save here
                    #         if not self.slot["stages"]["aldea_1"] is True:
                    #             saves.save(self.slotname, 2, "Aldea Saar", "aldea_1")
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

    def actors_load(self, rel_x):
        # if (self.player.real_x+self.player.rect.width > 620
        #         and self.player.real_x+self.player.rect.width < 745):
        #     self.interact.float(rel_x)
        print self.player.real_x
        self.player.update()
