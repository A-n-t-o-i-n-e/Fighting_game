import pygame
from player import Player

class Game:

    def __init__(self) -> None:
        self.player1 = Player(250, self)
        self.player2 = Player(775, self)
        self.pressed = {}  # contient les touches préssés
        self.floor = pygame.sprite.Group()
        self.team1 = pygame.sprite.Group()
        self.team1.add(self.player1)
        self.team2 = pygame.sprite.Group()
        self.team2.add(self.player2)

    def Check_Collision(self):
        return pygame.sprite.groupcollide(self.team1, self.team2, False, False)

