import pygame as pg
from sys import exit
import gol_engine as gol

pg.init()
size = tuple(eval(input()))
screen = pg.display.set_mode((size[0] * 10, size[1] * 10))
canvas = gol.create_canvas(size)


while True:
    try:
        coordinates: tuple = tuple(eval(input()))
    except:
        break
    canvas[coordinates[0]][coordinates[1]] = 1

alivecell = pg.Surface((10, 10))
alivecell.fill("white")

pg.display.set_caption("Game of Life")

clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    canvas = gol.getnextgen(canvas)
    screen.fill("black")
    for row in enumerate(canvas):
        for cell in enumerate(row[1]):
            if cell[1] == 1:
                screen.blit(alivecell, (row[0] * 10, cell[0] * 10))
    pg.display.update()
    # clock.tick(10000000)
