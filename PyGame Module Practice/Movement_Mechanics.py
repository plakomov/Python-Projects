import pygame

# Note: Adding moving mechanics to the player's spaceship
# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))  # Create the screen and specify the width and height

# Title and Icon
pygame.display.set_caption("Title, Icon Display")
icon = pygame.image.load("octopus_2.png")
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load("player_ship.png")
playerX = 370
playerY = 480


def player(x,y):
    screen.blit(player_img, (x, y))  # Basically draws an image of the player on the screen
    # We added also x and y parameters that tell us where the player is at on the display


# Game Loop
# Need to add quit option
running = True
while running:
    screen.fill((255, 255, 0))  # fills in the screen with a specific color: Uses RGB
    playerX += 0.1  # moves the player left and right
    playerY -= 0.1  # moves the player up or down
    for event in pygame.event.get():  # Loops through all the events inside the screen
        if event.type == pygame.QUIT:  # pygame.Quit checks if the exit button has been clicked
            running = False
    player(playerX, playerY)
    pygame.display.update()  # the display needs to be updated everytime there is a change MUST!!!
