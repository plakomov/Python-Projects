import pygame
import random

# Note: In this script, we are going to create the enemies against the player
# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))  # Create the screen and specify the width and height

# Title and Icon
pygame.display.set_caption("Keystroke is pressed")
icon = pygame.image.load("octopus_2.png")
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load("player_ship.png")
playerX = 370
playerY = 480
dx = 0  # rate of movement

# Enemy
enemy_img = pygame.image.load("enemy.png")
enemyX = random.randint(0, 768)
enemyY = random.randint(0, 50)
dy_enemy = 0


def player(x, y):
    screen.blit(player_img, (x, y))  # Basically draws an image of the player on the screen
    # We added also x and y parameters that tell us where the player is at on the display


def enemy(x, y):
    screen.blit(enemy_img, (x, y))


# Game Loop
# Need to add quit option
running = True
while running:
    screen.fill((255, 255, 0))  # fills in the screen with a specific color: Uses RGB
    # Checks for Keystroke events
    for event in pygame.event.get():  # Loops through all the events inside the screen
        if event.type == pygame.QUIT:  # pygame.Quit checks if the exit button has been clicked
            running = False
        # Checks if the left, right, up or down keys were pressed
        if event.type == pygame.KEYDOWN:  # Check if the type of the event is keystroke
            print("A keystroke is pressed")  # Now, we need to check which keystroke was pressed
            if event.key == pygame.K_LEFT:
                print("Left key is pressed")
                dx = -0.3
            if event.key == pygame.K_RIGHT:
                print("Right keys is pressed")
                dx = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:  # when the keystroke is up, we stop the
                # moving
                print("Keystroke has been released")
                dx = 0
    playerX += dx
    if playerX <= 0:  # Border restrictions (I think I can make a function out of this based on border of the display)
        playerX = 0
    if playerX >= 768:
        playerX = 768
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()  # the display needs to be updated everytime there is a change MUST!!!
