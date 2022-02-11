import pygame

# Setting it up
screen = pygame.display.set_mode((500, 800))
pygame.display.set_caption("Demo Button")

# Initialize the game
pygame.init()
start_img = pygame.image.load("bullet.png").convert_alpha()
exit_img = pygame.image.load("player_ship.png").convert_alpha()


# Button Class
class Button:
    def __init__(self, posx, posy, img, scale):
        width = img.get_width()
        height = img.get_height()
        self.image = pygame.transform.scale(img, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (posx, posy)
        self.clicked = False

    def draw(self):
        action = False
        # Get mouse position
        pos = pygame.mouse.get_pos()  # Gives you the coordinates of the mouse
        # Check mouse over and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:  # 0 means the left click
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action


# Creating instances of the buttons
start_button = Button(150, 400, start_img, 3)
exit_button = Button(250, 400, exit_img, 3)

# Game loop
running = True
while running:
    screen.fill((255, 255, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if start_button.draw():
        print("START")
    if exit_button.draw():
        print("EXIT")
        running = False
    pygame.display.update()
