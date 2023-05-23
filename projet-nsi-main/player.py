import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, game) -> None:
        super().__init__()
        self.hp = 100
        self.hp_max = 100
        self.dmg = 10
        self.v = 1
        self.img = pygame.image.load('assets/player.png')
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = 430
        self.game = game



    def move_right(self):
        if pygame.sprite.groupcollide(self.game.team1, self.game.team2, False, False) == {}:
            self.rect.x += 2
        else:
            self.rect.x -= self.v
    
    def move_left(self):
        if pygame.sprite.groupcollide(self.game.team1, self.game.team2, False, False) == {}:
            self.rect.x -= 2
        else:
            self.rect.x += self.v