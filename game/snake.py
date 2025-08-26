import pygame
from .utils import C, snake_img, screen

class Snake:
    def __init__(self):
        self.body = [(100, 100)]
        self.direction = (C, 0)  # start moving right
        self.grow_pending = False

    def turn(self, dir):
        """Change direction (avoid reversing into itself)."""
        # Prevent reversing directly
        if (dir[0] * -1, dir[1] * -1) != self.direction:
            self.direction = dir

    def move(self):
        """Move snake forward."""
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body.insert(0, new_head)

        if self.grow_pending:
            self.grow_pending = False
        else:
            self.body.pop()

    def grow(self):
        """Increase snake length by 1."""
        self.grow_pending = True

    def get_head(self):
        """Return the current head position."""
        return self.body[0]

    def draw(self, surface):
        """Draw snake on screen."""
        for part in self.body:
            surface.blit(snake_img, part)
