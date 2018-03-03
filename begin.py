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

GPS = 40

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
    fps_clock = pygame.time.Clock()
    # akward comment
    pause = True
    # gen time state, 0 at start
    gen = 0

    #event window interaction
    while True:
        fps_clock.tick(GPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pause = not pause
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                x //= SIZE
                y //= SIZE
                board[y][x] = not board[y][x]

        if not pause :
            board, gen = update(board, gen)
        render(screen, board)


def update(board, gen):
    n_board = new_board()
    for y in range(NY):
        for x in range(NX):
            voisins = process_cell(board, x, y)
            if voisins == 3:
                n_board[y][x] = True
            elif voisins == 2:
                n_board[y][x] = board[y][x]
            else:
                #cell is dead
                pass
    gen += 1
    #print("Generation{}".format(gen))
    return n_board, gen

# get current alive cell
def process_cell(board, x, y):
    voisins = 0
    for i in range(9):
        if i == 4: continue
        #left
        xx = (i % 3) - 1
        #right
        yy = (i // 3) - 1

        # checks cell neighbours
        cx = (x + xx + NX) % NX
        cy = (y + yy + NY) % NY
        # recover cell state
        if board[cy][cx]:
            voisins += 1
    return voisins


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

def new_board():
    #create 2D board of two lists size 32 with rand rect
    board = [[False for x in range(NX)] for y in range(NY)]
    #print(board)
    return board

if __name__ == '__main__':
    main()
