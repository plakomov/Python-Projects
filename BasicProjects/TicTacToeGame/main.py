# Main file that runs tictactoe game
import pygame
import numpy as np

# We are going to simulate a tic tac toe game in numpy
# Moves 1 is X and -1 is  O ; 0 means the neutral state
ROWS = 3
COLUMNS = 3
BOARD = np.zeros((ROWS, COLUMNS))


def reset_board():
    """Resets all the states to neutral"""
    global BOARD
    BOARD = np.zeros((ROWS, COLUMNS))


def isValid(x, y):
    """Determines if the move is a valid move"""
    return BOARD[x][y] == 0


def make_move(x, y, state):
    """Makes a move at the location x and y and state """
    BOARD[x][y] = state


def isWinner():
    """Checks if there is winner"""
    for i in range(3):
        if np.max(BOARD[i]) == np.min(BOARD[i]) and BOARD[i][0] != 0:
            return [(i, 0), (i, 1), (i, 2)]
        if np.max(BOARD.transpose()[i]) == np.min(BOARD.transpose()[i]) and BOARD[0][i] != 0:
            return [(0, i), (1, i), (2, i)]
    if BOARD[0][0] == BOARD[1][1] == BOARD[2][2] and BOARD[0][0] != 0:
        return [(0, 0), (1, 1), (2, 2)]
    if BOARD[0][2] == BOARD[1][1] == BOARD[2][0] and BOARD[0][2] != 0:
        return [(0, 2), (1, 1), (2, 0)]
    return False


def isFill():
    """Checks if the board is full"""
    return np.all(BOARD)


# Game interface
pygame.init()
pygame.display.set_caption("TIC TAC TOE GAME")
screen = pygame.display.set_mode((600, 600))

# CHOICE VARIABLE
var = 1  # VARIABLE THAT DETERMINES WHOSE MOVE IT IS; 1 is X and -1 is O


# pygame.draw.circle(window, colour, circle_x_&_y, circle_radius, border_width)

class Rectangle:

    def __init__(self, x, y, state, row, col):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 200, 200)
        self.state = state
        self.clicked = False
        self.row = row
        self.col = col

    def draw(self):
        global var
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:  # 0 means the left click
                self.clicked = True
                self.state = var
                make_move(self.row, self.col, var)
                var = -1 * var
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
        if self.state == -1:
            pygame.draw.circle(screen, (255, 0, 0), (self.x + 100, self.y + 100), 100, 3)
        if self.state == 1:
            pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (self.x + 200, self.y + 200), 3)
            pygame.draw.line(screen, (0, 0, 0), (self.x, self.y + 200), (self.x + 200, self.y), 3)


# List of rectangles
rects = []
for i in range(3):
    for j in range(3):
        rects.append(Rectangle(i*200, j*200, BOARD[i][j], i, j))

running = True
while running:
    screen.fill((175, 175, 80))
    for shape in rects:
        shape.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r: # pressing R resets the whole board
                for shape in rects:
                    shape.state = 0
                    shape.clicked = False
                    var = 1
                reset_board()
    if type(isWinner()) != bool:
        coordinates = []
        for shape in rects:
            if shape.row == isWinner()[0][0] and shape.col == isWinner()[0][1]:
                coordinates.append((shape.x + 100, shape.y + 100))
            if shape.row == isWinner()[2][0] and shape.col == isWinner()[2][1]:
                coordinates.append((shape.x + 100, shape.y + 100))
        pygame.draw.line(screen, (0, 255, 0), coordinates[0], coordinates[1])
    pygame.display.update()
