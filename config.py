import pygame

# COLORS AND BOOLEANS
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (255, 200, 200)
YELLOW = (255, 255, 0)
BACKGROUND_COLOR = (255, 246, 191)
PROGRAM_END = False
PAUSED = False

# PYGAME DRAWING VALUES
screen_width = 240
screen_height = 280
framerate = 60
point_radius = 20
points_number = 10


main_screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Maciej Łacwik || simple neural networks visualization")
main_screen.fill(BACKGROUND_COLOR)
