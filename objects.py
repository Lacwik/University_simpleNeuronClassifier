from config import *


class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.x_display = (x+3)*(point_radius*2)
        self.y_display = (y+3)*(point_radius*2)
        self.color = color

    def draw(self):
        pygame.draw.circle(main_screen, self.color, (self.x_display, self.y_display), point_radius)
        pygame.draw.circle(main_screen, BLACK, (self.x_display, self.y_display), point_radius, 1)


def init_points():
    points = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            point = Point(i, j, BLACK)
            points.append(point)
    return points

def function_text(string):
   font = pygame.font.Font(None,30)
   text = font.render(string, 1, BLACK)
   main_screen.blit(text, (80, 230))