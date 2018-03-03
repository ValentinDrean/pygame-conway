# 2 cells : dead or aline

# if (cell on currentgen has 3 neighburs)
# {cell will be alive nextgen}

# if (cell on currentgen has exactly 2 neighburs)
# {identical state on nextgen}

# if (cell on currentgen has less than 2 neighburs
# OR has more than 3)
# {cell die or stay dead}

import pygame
from pygame.locals import *
from random import randint

# cell number
NX = 32
NY = 32

# size of cell
SIZE = 20

# window size
WIDTH = NX * SIZE
HEIGHT = NY * SIZE

# color background
WHITE = (255,255,255) #can use pygame.color too
# do I need to comment that? :>
CELL_COLOR = (77,0,0)

def main():
    #pygame init conf
        pygame.init()
        pygame.display.set_caption("Conway 70's game")
        # 2D size of window
        screen = pygame.display.set_mode((WIDTH, HEIGHT))

        #keep window opened
        mainloop(screen)

def mainloop(screen):
    # game board
    board = new_board()
    # akward comment
    pause = True
    # gen time state, 0 at start
    gen = 0

    #event window interaction
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
        render(screen, board)

def new_board():
    #create 2D board of two lists size 32 with rand rect
    board = [[randint(0, 1) for x in range(NX)] for y in range(NY)]
    #print(board)
    return board

# draw board
def render(screen, board):
    # empty screen
    screen.fill(WHITE)
    # alive cell game area size 32
    for y in range(NY):
        for x in range(NX):
            # if board[y][x] = 0 so it's false
            if board[y][x]:
                pygame.draw.rect(screen, CELL_COLOR, (x * SIZE, y * SIZE, SIZE, SIZE))
    pygame.display.update()

if __name__ == '__main__':
    main()
