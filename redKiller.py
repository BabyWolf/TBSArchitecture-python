# redKiller.py
import pygame

class RedKiller(pygame.sprite.Sprite):

    group = pygame.sprite.Group()

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        RedKiller.group.add(self)

        self.image = pygame.Surface([128, 128])
        self.image.fill((255, 0, 0, 255))

        self.rect = self.image.get_rect()

        self.rect.move_ip(*pos)
