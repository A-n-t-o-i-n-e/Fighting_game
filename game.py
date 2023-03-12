import pygame
from player import Player

class Game:

    def __init__(self) -> None:
        self.player1 = Player(250)
        self.player2 = Player(775)
        self.pressed = {}  # contient les touches préssés
        self.clock = pygame.time.Clock()  # gere las fps
        self.v_g = 0  # stocke successivement la v en y des joueur (accélération)

    def gravity(self):
        self.v_g *= 1.1
        self.player1.rect.y += self.player1.v * 20
        self.player2.rect.y += self.player2.v * 10