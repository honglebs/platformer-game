import pygame as pg, sys
from settings import *
from tiles import Tile

pg.init()
screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()
test_tile = pg.sprite.Group(Tile((100, 100), 200))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
    screen.fill('black')
    test_tile.draw(screen)

    pg.display.update()
    clock.tick(60)