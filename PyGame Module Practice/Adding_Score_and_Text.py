import pygame
import random
import math

# Note: Adding Text and Score ( IMPORTANT: Text need to be rendered before being displayed on the screen)
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
enemy_img = []
enemy_img = []
enemyX = []
enemyY = []
dy_enemy = []
dx_enemy = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0, 768))
    enemyY.append(random.randint(25, 200))
    dy_enemy.append(40)
    dx_enemy.append(0.1)

# Bullet
bullet_img = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
dy_bullet = -1
dx_bullet = 0
bullet_state = "ready"  # ready state means you cannot see the bullet on the screen; "fire" bullet is in motion


#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
score_x = 10
score_y = 10


def show_score(x, y):
    score = font.render(f"Score: {score_value}", True, (100, 255, 0))  # We first need to create the image
    screen.blit(score, (x, y))

def player(x, y):
    pygame.draw.circle(screen, (255, 255, 0), (x, y), 32)
    screen.blit(player_img, (x - 16, y - 5))  # Basically draws an image of the player on the screen
    # We added also x and y parameters that tell us where the player is at on the display


def enemy(x, y, i):
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 32)
    screen.blit(enemy_img[i], (x - 16, y - 5))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))


def isCollision(e_X, e_Y, b_X, b_Y):
    distance = math.sqrt(math.pow(e_X - b_X, 2) + math.pow(e_Y - b_Y, 2))
    if distance < 30:
        return True
    else:
        return False


# Game Loop
# Need to add quit option
running = True
while running:
    screen.fill((255, 255, 0))  # fills in the screen with a specific color: Uses RGB
    # Background Image
    screen.blit(bg_image, (0, 0))
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
                if bullet_state == 'ready':
                    bulletX = playerX
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

    for i in range(num_of_enemies):
        enemyX[i] += dx_enemy[i]
        if enemyX[i] <= 0 or enemyX[i] >= 768:
            dx_enemy[i] = -1 * dx_enemy[i]
            enemyY[i] += dy_enemy[i]
        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 768)
            enemyY[i] = random.randint(0, 50)
        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bullet_state = "ready"
        bulletY = 480
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY += dy_bullet

    player(playerX, playerY)
    show_score(score_x, score_y)
    pygame.display.update()  # the display needs to be updated everytime there is a change MUST!!!
