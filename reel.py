from config import *
import pygame, random

class Reel:
    def __init__(self, pos) -> None:
        self.symbol_list = pygame.sprite.Group()
        self.shuffled_keys = list(symbols.keys())
        random.shuffle(self.shuffled_keys)
        self.shuffled_keys = self.shuffled_keys[:5]

        self.reel_is_spinning = False

        #self.stop_sound = pygame.mixer.Sound()
        #self.stop_sound.set_volume(0.5)

        for idx, item in enumerate(self.shuffled_keys):
            self.symbol_list.add(Symbol(symbols[item],pos,idx))
            pos = list(pos)
            pos[1] += 300
            pos = tuple(pos)

class Symbol(pygame.sprite.Sprite):
    def __init__(self, pathToFile,pos,idx):
        super().__init__()

        self.sym_type = pathToFile.split('/')[3].split('.')[0]
        self.pos = pos
        self.idx = idx
        self.image = pygame.image.load(pathToFile).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.x_val = self.rect.left

    def update(self):
        pass