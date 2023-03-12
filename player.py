import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x) -> None:
        super().__init__()
        self.hp = 100
        self.hp_max = 100
        self.dmg = 10
        self.v = 1
        self.img = pygame.image.load('assets/player.png')
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = 430

        '''# Sauter
        self.a_jump = 0
        self.jump_up = 0
        self.jump_down = 5 
        self.nb_jump = 0
        self.isjumping = False

    def jump(self):
        if self.isjumping:

            if self.jump_up>= 10:
                self.jump_down -= 1
                self.a_jump = self.jump_down
            else:
                self.jump_up += 1
                self.a_jump = self.jump_up
            
        self.rect.y = self.rect.y - (10*(self.a_jump / 2))'''


    def move_right(self):
        self.rect.x += self.v
    
    def move_left(self):
        self.rect.x -= self.v