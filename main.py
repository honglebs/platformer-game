import pygame as pg, sys
import settings

pg.init()
screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
    screen.fill('black')

    pg.display.update()
    clock.tick(60)