import pygame

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))  # Create the screen and specify the width and height

#Title and Icon
pygame.display.set_caption("Title, Icon Display")
icon = pygame.image.load("octopus_2.png")
pygame.display.set_icon(icon)

# Game Loop
# Need to add quit option
running = True
while running:
    for event in pygame.event.get():  # Loops through all the events inside the screen
        if event.type == pygame.QUIT:  # pygame.Quit checks if the exit button has been clicked
            running = False
    screen.fill((255, 255, 0)) # fills in the screen with a specific color
    pygame.display.update() # the display needs to be updated everytime there is a change MUST!!!
