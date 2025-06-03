'''
Name: Brendan Kiaaina
Date: 6/2/25
Description:

'''

import pygame as pg
import sys
from board import Board

pg.init()
screen = pg.display.set_mode((640,640))
pg.display.set_caption('Chess Bot')

board = Board()

def main():
    clock = pg.time.Clock()
    running = True

    while running:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        board.draw(screen)
        pg.display.flip()
    
    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()

