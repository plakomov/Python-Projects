# This is the main file where the game will be ran
import pygame
import random
import time

# Initialize the game
pygame.init()

# Screen
screen = pygame.display.set_mode((600, 800))

# Background Image
bg = pygame.image.load("background.jpg")

# Game Over Text
game_over_font = pygame.font.Font('freesansbold.ttf', 64)
score_font = pygame.font.Font('freesansbold.ttf', 20)

# Constants
grv = 5
grv_acc = 75
initial_y_speed = 15
hover_n = 10
hover = 0
N_acc = 0
over = False
pipe_speed = 1
score = 0


# Moving Objects Class (Super Class)
class Img_Objs:
    """Objects which have a position; requires an img_file name"""

    def __init__(self, posx, posy, img_file):
        self.posx = posx
        self.posy = posy
        self.img = pygame.image.load(img_file)

    # Also need a method that places them on the screen

    def upload_screen(self, scr):
        """Places an image on the screen at the specified position
        scr is a pygame surface object"""
        scr.blit(self.img, (self.posx, self.posy))

    def update_x(self, x):
        self.posx = x

    def update_y(self, y):
        self.posy = y


class Player(Img_Objs):
    """This class is the player class"""

    def __init__(self, posx, posy, img_file, dx, dy, jump_st=False):
        super().__init__(posx, posy, img_file)
        self.dx = dx
        self.dy = dy
        self.jump_state = jump_st


# Functions

def game_over_text():
    game_over = game_over_font.render("GAME OVER!", True, (255, 255, 0))
    screen.blit(game_over, (100, 300))


def isCollision(ply1: Img_Objs, obst1: Img_Objs, obst2: Img_Objs):
    if ply1.posy + 16 <= obst1.posy + 600 or ply1.posy + 16 >= obst2.posy:
        if obst1.posx <= ply1.posx + 16 <= obst1.posx + 75:
            return True
    else:
        return False


def score_text():
    score_ = score_font.render(f"Score: {score}", True, (255, 255, 0))
    screen.blit(score_, (0, 30))


# Instance of a player and obstacles
player_1 = Player(300, 300, "mushroom.png", 0, initial_y_speed)
pipes_up = []  # Only a limit of 4 pipes up and down
pipes_down = []

# Range for the gap 200, 700
gap = 150
for i in range(4):
    randy = random.randint(200, 600) - 600
    pipes_down.append(Img_Objs(gap * i + 630, randy, "pipe_down_600.png"))
    pipes_up.append(Img_Objs(gap * i + 630, randy + 800, "pipe_up_600.png"))

# Game Loop
running = True
while running:
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_1.jump_state = True
                hover = hover_n
                N_acc = 0
    # Flight mechanics
    if hover == 0:
        player_1.jump_state = False
        player_1.dy = initial_y_speed

    else:
        player_1.dy = player_1.dy - (initial_y_speed / hover_n)
        hover -= 1

    if player_1.jump_state:
        player_1.update_y(player_1.posy - player_1.dy)
    else:
        if N_acc == grv_acc:  # Simulates the acceleration of an object when its falling
            player_1.update_y(player_1.posy + grv)
        else:
            player_1.update_y(player_1.posy + (grv / grv_acc) * N_acc)
            N_acc += 1

    # Placing the obstacles and moving the obstacles and checking for collisions
    for i in range(4):
        if pipes_up[i].posx + 75 <= 0:
            randy = random.randint(200, 600) - 600
            pipes_down[i].posx, pipes_down[i].posy = 610, randy
            pipes_up[i].posx, pipes_up[i].posy = 610, randy + 800
        else:
            pipes_up[i].posx = pipes_up[i].posx - pipe_speed
            pipes_down[i].posx = pipes_up[i].posx - pipe_speed
        pipes_up[i].upload_screen(screen)
        pipes_down[i].upload_screen(screen)
        if isCollision(player_1, pipes_down[i], pipes_up[i]):
            over = True
        if pipes_down[i].posx + 75 == player_1.posx:
            score += 1
    # Boundaries Conditions
    if player_1.posy >= 768:
        over = True
    if over:
        game_over_text()
    # Display
    score_text()
    player_1.upload_screen(screen)
    pygame.display.update()

    # Check if the game is over
    if over:
        time.sleep(3)
        break
