import pygame as pg
import traceback
from random import random

WIDTH = 800
HEIGHT = 800

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (55, 166, 0)


def clamp(var, lower, upper):
    # restrains a variable's value between two values
    return max(lower, min(var, upper))


def remap(n, start1, stop1, start2, stop2):
    # https://p5js.org/reference/#/p5/map
    newval = (n - start1) / (stop1 - start1) * (stop2 - start2) + start2
    if (start2 < stop2):
        return clamp(newval, start2, stop2)
    else:
        return clamp(newval, stop2, start2)
    


def next_point(x, y):
    r = random()
        
    if r < 0.01:
        # 1
        nextX =  0
        nextY = 0.16 * y
    elif r < 0.86:
        # 2
        nextX =  0.85 * x + 0.04 * y
        nextY = -0.04 * x + 0.85 * y + 1.6
    elif r < 0.93:
        # 3
        nextX =  0.2 * x + -0.26 * y
        nextY = 0.23 * x + 0.22 * y + 1.6
    else:
        # 4
        nextX =  -0.15 * x + 0.28 * y
        nextY = 0.26 * x + 0.24 * y + 0.44
    
    x = nextX
    y = nextY
    
    return x, y
    

# initialize pygame
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

x = 0
y = 0
    
screen.fill(BLACK)

# game loop
running = True
try:
    while running:
        clock.tick(60)
        
        pg.display.set_caption(str(clock.get_fps()))
    
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        for i in range(100):
            px = remap(x, -2.5, 2.7, 0, WIDTH)
            py = remap(y, 0, 10, HEIGHT, 0)
            pg.draw.circle(screen, GREEN, (int(px), int(py)), 1)
            
            x, y = next_point(x, y)

        pg.display.update()
    
    pg.quit()
except Exception:
    traceback.print_exc()
    pg.quit()