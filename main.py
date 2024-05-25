import pygame
from machine import Machine
from config import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Sigma Slot Machine")
        self.clock = pygame.time.Clock()
        self.bg_image = pygame.image.load(BG_IMAGE_PATH).convert_alpha()
        self.machine = Machine()
        self.delta_time = 0
        self.grid_image = pygame.image.load(GRID_IMAGE_PATH).convert_alpha()
        main_sound = pygame.mixer.Sound(SOUND_TRACK_PATH)
        main_sound.play(loops=-1)

    def run(self):
        self.start_time = pygame.time.get_ticks()

        while True:
            # Quit operation - winners never quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            current_time = pygame.time.get_ticks()
            self.delta_time = (current_time -self.start_time)/1000.0
            self.start_time = current_time
            self.screen.fill((0,0,0))
            self.screen.blit(self.bg_image,(0,0))
            
            self.machine.update(self.delta_time)
            self.screen.blit(self.grid_image,(0,0))

            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()