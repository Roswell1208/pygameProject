import pygame
from player import Player


# Class game
class Game:

    def __init__(self):
        # Player generation
        self.player = Player()
        self.pressed = {}