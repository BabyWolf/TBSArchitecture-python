# actor.py
import pygame

from action import *
from trigger import *
from actionList import *
from redKiller import *

class Actor(pygame.sprite.Sprite):

    group = pygame.sprite.Group()

    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)

        Actor.group.add(self)

        self.image = pygame.Surface([32, 32])
        self.image.fill((0, 255, 0, 255))

        self.rect = self.image.get_rect()
        self.rect.move_ip(*position)

        self.__target = pygame.math.Vector2(0, 0)
        self.__in_moving = False
        self.__progress = 0.0
        self.__move_start_point = pygame.math.Vector2(0, 0)

        self.__move_completed_trigger = Trigger()
        
        self.__deleted_trigger = Trigger()
        self.__deleted_trigger.refresh() # изначально триггер поднят


    def kill(self):
      	# Этот метод от pygame.sprite.Sprite и он просто убирает объект из всех групп
        super().kill()

        self.__deleted_trigger.trigger()
        

    def init_moving(self, to):
        self.__target = pygame.math.Vector2(to)
        self.__in_moving = True
        self.__progress = 0.0
        self.__move_start_point = pygame.math.Vector2(self.rect.center)
        self.__move_completed_trigger.refresh()


    def get_init_move_action(self, to):
        a1 = Action(self.init_moving, [to], self.__move_completed_trigger, self.__deleted_trigger)

        return a1


    def update(self):
        if self.__in_moving:
            if self.__progress > 1.0:
                self.__in_moving = False
                self.__move_completed_trigger.trigger()
                return

            self.rect.center = self.__move_start_point.lerp(self.__target, self.__progress)

            self.__progress += 0.001

class SkittishGreen(Actor):

    def __init__(self, pos):
        Actor.__init__(self, pos)


    def check_collision(self):
        for i in RedKiller.group.sprites():
            if i.rect.colliderect(self.rect):
                self.kill()
                return


    def get_move_action(self, to):
        return Action(self.get_actions, [to])


    def get_actions(self, to):
        a1 = self.get_init_move_action(to)
        a2 = Action(self.check_collision, [])
        a3 = self.get_init_move_action(self.rect.center)

        return ActionList(a1, a2, a3)
