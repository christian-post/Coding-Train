import pygame as pg
import traceback
import math
from random import randint

WIDTH = 800
HEIGHT = 800

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (100, 100, 100)

# initialize pygame
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()


def random_color():
    start = 40
    stop = 240
    return (randint(start, stop), randint(start, stop), randint(start, stop))


class Curve:
    def __init__(self):
        self.path = []
        self.color = random_color()
        
    def addPoint(self, x, y):
        self.path.append((x, y))

    def show(self, screen):
        if len(self.path) > 1:
            pg.draw.lines(screen, self.color, False, self.path, 3)
            
    def reset(self):
        self.path = []
        self.color = random_color()
        
        
# init grid
cellsize = 80
margin = 4
radius = cellsize // 2 - margin

cols = WIDTH // cellsize
rows = HEIGHT // cellsize

angle = 0

curves = [[Curve() for i in range(rows)] for j in range(cols)]


# game loop
running = True
try:
    while running:
        clock.tick(60)
    
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
    
        screen.fill(BLACK)

        for i in range(rows):
            cx1 = cellsize + i * cellsize + cellsize // 2
            cy1 = cellsize // 2
            pg.draw.circle(screen, GREY, (cx1, cy1), radius, 1)
            
            x1 = radius * math.cos(angle * (i + 1) - math.pi / 2)
            y1 = radius * math.sin(angle * (i + 1) - math.pi / 2)           
            pg.draw.circle(screen, WHITE, (int(cx1 + x1), int(cy1 + y1)), 4)
            
            pg.draw.line(screen, GREY, (cx1 + x1, 0), (cx1 + x1, HEIGHT), 1)
            
            for j in range(cols):
                cx2 = cellsize // 2
                cy2 = cellsize + j * cellsize + cellsize // 2
               
                pg.draw.circle(screen, GREY, (cx2, cy2), radius, 1)
                
                x2 = radius * math.cos(angle * (j + 1) - math.pi / 2)
                y2 = radius * math.sin(angle * (j + 1) - math.pi / 2)                 
                pg.draw.circle(screen, WHITE, (int(cx2 + x2), int(cy2 + y2)), 4)
                
                pg.draw.line(screen, GREY, (0, cy2 + y2), (WIDTH, cy2 + y2), 1)
                
                curves[j][i].addPoint(int(cx1 + x1), int(cy2 + y2))
                curves[j][i].show(screen)
                
        angle += 0.01

        if angle >= math.pi * 2:
            angle = 0
            for i in range(rows):
                for j in range(cols):
                    saved_image = screen.copy()
                    curves[j][i].reset()
        
        pg.display.update()
    try:
        pg.image.save(saved_image, 'lissajous.png')
    except Exception:
        traceback.print_exc()
    pg.quit()
except Exception:
    traceback.print_exc()
    pg.quit()