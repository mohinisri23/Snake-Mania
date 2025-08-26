import pygame
import random
import os

# Initialize pygame modules
pygame.init()

# Grid and screen settings
GRID_SIZE = 20
C = GRID_SIZE   # 👈 alias for compatibility
W, H = 600, 400  # Width and Height of window

# Setup screen
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("🐍 Snake Game")

# Clock
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont("Arial", 24)

# Helper: load an image safely
def load_image(path, fallback_color=None, size=None):
    if os.path.exists(path):
        img = pygame.image.load(path).convert_alpha()
        if size:
            img = pygame.transform.scale(img, size)
        return img
    else:
        print(f"⚠️ {os.path.basename(path)} not found in assets, using fallback.")
        if fallback_color:
            surf = pygame.Surface(size if size else (GRID_SIZE, GRID_SIZE))
            surf.fill(fallback_color)
            return surf
        return None

# Load assets
print(f"🔍 Looking for background: {os.path.join(os.getcwd(), 'assets', 'snakebg.jpg')}")
bg = load_image(os.path.join("assets", "snakebg.jpg"), fallback_color=(0, 0, 0), size=(W, H))

print(f"🔍 Looking for snake.png: {os.path.join(os.getcwd(), 'assets', 'snake.png')}")
snake_img = load_image(os.path.join("assets", "snake.png"), fallback_color=(0, 255, 0), size=(GRID_SIZE, GRID_SIZE))

foods = {}
for name, color in [("applef.webp", (255, 0, 0)), ("avacadof.webp", (0, 255, 0)), ("melonf.webp", (0, 0, 255))]:
    print(f"🔍 Looking for {name}: {os.path.join(os.getcwd(), 'assets', name)}")
    foods[name] = load_image(os.path.join("assets", name), fallback_color=color, size=(GRID_SIZE, GRID_SIZE))

# Random grid-aligned position
def rand_pos():
    """Return a random (x, y) position aligned to the grid."""
    x = random.randrange(0, W, GRID_SIZE)
    y = random.randrange(0, H, GRID_SIZE)
    return x, y
