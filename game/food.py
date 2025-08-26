import pygame
import random
from .utils import rand_pos, foods, C

class Food:
    def __init__(self):
        self.image = random.choice(list(foods.values()))
        self.pos = rand_pos()
        self.rect = pygame.Rect(self.pos[0], self.pos[1], C, C)

    def relocate(self):
        """Move food to new random position and possibly change type."""
        self.image = random.choice(list(foods.values()))
        self.pos = rand_pos()
        self.rect.topleft = self.pos

    def draw(self, surface):
        """Draw food on the given surface."""
        surface.blit(self.image, self.pos)
