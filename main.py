''' Script principale '''

import pygame
from game import Game

pygame.init()


# init la fenetre
pygame.display.set_caption('Projet NSI')
screen = pygame.display.set_mode((1080, 720))

# charge le bg et le jeu
bg = pygame.image.load('assets/bg.jpg')
game = Game()

running = True

# boucle du jeu
while running:

    screen.blit(bg, (0, 0))  # dessine le bg
    screen.blit(game.player1.img, game.player1.rect)  # dessine le joueur1
    screen.blit(game.player2.img, game.player2.rect)  # dessine le joueur2

    # si la touche dans le dictionnaire est = a True  alors faire l'action qui lui est assigné (p1)
    if game.pressed.get(pygame.K_d) and game.player1.rect.x < screen.get_width()- game.player1.rect.width:
        game.player1.move_right()
    elif game.pressed.get(pygame.K_q) and game.player1.rect.x > 0:
        game.player1.move_left()

    # si la touche dans le dictionnaire est = a True  alors faire l'action qui lui est assigné (p2)
    if game.pressed.get(pygame.K_RIGHT) and game.player2.rect.x < screen.get_width()- game.player2.rect.width:
        game.player2.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player2.rect.x > 0:
        game.player2.move_left()

    pygame.display.flip()  # maj

   # vérifie si le joueur fait une action
    for event in pygame.event.get():
        # pour fermer la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # si une touche es pressée ou non, son statut est specifiée dans le dico game.pressed
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False


