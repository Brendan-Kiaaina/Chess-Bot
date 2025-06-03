'''
Name: Brendan Kiaaina
Date: 6/2/25
Description: 

'''
import pygame

white = (240, 217, 181)
brown = (181, 136, 99)
rows = 8
cols = 8
square_size = 640 // cols

class Board:
    def __init__(self):
        self.board = [[None for _ in range(cols)] for _ in range(rows)]

    def draw(self, screen):
        for row in range(rows):
            for col in range(cols):
                color = brown if (row + col) % 2 else white
                pygame.draw.rect(screen, color, (col * square_size, row * square_size, square_size, square_size))