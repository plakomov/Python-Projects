import pygame
import random

# Note: We are creating a bullet for the ship; We also created some primitive movements for it as well
# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))  # Create the screen and specify the width and height

# Background Image
bg_image = pygame.image.load("space_background_800_600.jpg")


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
dy_enemy = 40
dx_enemy = 0.1

# Bullet
bullet_img = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
dy_bullet = -10
dx_bullet = 0
bullet_state = "ready" # ready state means you cannot see the bullet on the screen; "fire" bullet is in motion


def player(x, y):
    pygame.draw.circle(screen, (255, 255, 0), (x, y), 32)
    screen.blit(player_img, (x-16, y-5))  # Basically draws an image of the player on the screen
    # We added also x and y parameters that tell us where the player is at on the display


def enemy(x, y):
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 32)
    screen.blit(enemy_img, (x-16, y-5))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x+16, y+10))

# Game Loop
# Need to add quit option
running = True
while running:
    screen.fill((255, 255, 0))  # fills in the screen with a specific color: Uses RGB
    # Background Image
    screen.blit(bg_image, (0,0))
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
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:  # when the keystroke is up, we stop the
                # moving
                print("Keystroke has been released")
                dx = 0
    playerX += dx
    if playerX <= 0:  # Border restrictions (I think I can make a function out of this based on border of the display)
        playerX = 0
    elif playerX >= 768:
        playerX = 768

    enemyX += dx_enemy
    # enemyY += dy_enemy

    if enemyX <= 0 or enemyX >= 768:
        dx_enemy = -1 * dx_enemy
        enemyY += dy_enemy
    # if enemyY <= 0 or enemyY >= 600:  <- my code; allows it move down
    #    dy_enemy = -1 * dy_enemy

    # Bullet Movement
    if bullet_state == "fire":
        fire_bullet(playerX, bulletY)
        bulletY += dy_bullet
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()  # the display needs to be updated everytime there is a change MUST!!!
