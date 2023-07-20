import pygame


# Class player
class Player (pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 2
        self.image = pygame.image.load('game/assets/Robot/PNG/Poses HD/character_robot_idle.png')
        self.rect = self.image.get_rect()
        self.rect.x = 700
        self.rect.y = 650

    
    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity