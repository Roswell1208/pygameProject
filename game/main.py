import pygame
pygame.init()

# Create the screen
pygame.display.set_caption("Space Invaders")
screen = pygame.display.set_mode((1080, 720))

# Background
background = pygame.image.load('game/assets/bg.jpg')
background = pygame.transform.scale(background, (1080, 720))
screen.blit(background, (0, 0))

# Screen update
pygame.display.flip()

running = True


# Game loop
while running:

    # Close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False