import pygame
from game import Game
pygame.init()


# Create the screen
pygame.display.set_caption("Space Invaders")
screen = pygame.display.set_mode((1620, 1080))

# Background
background = pygame.image.load('game/assets/bg.jpg')
background = pygame.transform.scale(background, (1620, 1080))

# Load the game
game = Game()

running = True


# Game loop
while running:

    # Background
    screen.blit(background, (0, 0))

    # Player
    screen.blit(game.player.image, game.player.rect)

    # Player movement
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < screen.get_width() - game.player.rect.width:
        game.player.move_right()

    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
    
    print(game.player.rect.x, game.player.rect.y)

    # Screen update
    pygame.display.flip()


    # Close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detect if a key is pressed
        elif event.type == pygame.KEYDOWN:

            # Detect if the space key is pressed
            game.pressed[event.key] = True
        
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False