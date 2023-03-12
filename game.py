import pygame
from player import Player

class Game:

    def __init__(self) -> None:
        self.player1 = Player(250)
        self.player2 = Player(775)
        self.pressed = {}  # contient les touches préssés
