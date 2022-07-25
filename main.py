# main.py

import pygame
import sys

from action import *
from actionProcessor import *
from actor import *
from redKiller import *

pygame.init()

screen = pygame.display.set_mode((700, 700))

action_processor = ActionProcessor()

hand_mode = True
allow_next = False

player = SkittishGreen((137, 541))

RedKiller((200, 200))

def opers(a, b):
    a1 = Action(lambda x, y: print(x+y), [a, b])
    a2 = Action(lambda x, y: print(x-y), [a, b])
    a3 = Action(lambda x, y: print(x/y), [a, b])
    a4 = Action(lambda x, y: print(x*y), [a, b])

    return ActionList(a1, a2, a3, a4)

action_processor.add_action(Action(opers, [3463, 675]))

font = pygame.font.Font("kenney-pixel.ttf", 32)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                allow_next = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                a = player.get_move_action(event.pos)

                action_processor.add_action(a)


    if action_processor.has_actions_in_queue():
        if not(hand_mode) or allow_next:
            if not action_processor.current_in_process():
                action_processor.act_first()
                allow_next = False

    screen.fill((0, 0, 0, 255))
    
    # Drawing action queue
    if action_processor.current_in_process():
        surf = font.render(str(action_processor.get_current_action()), False, (255, 255, 255))
        screen.blit(surf, (0, 0, 0, 0))

    n = 2
    for i in action_processor.get_actions():

        surf = font.render(str(i), False, (255, 255, 255))

        screen.blit(surf, (0, 20*n, 0, 0))

        n += 1
    # End drawing aciton queue
    
    Actor.group.update()
    Actor.group.draw(screen)

    RedKiller.group.update()
    RedKiller.group.draw(screen)
    
    pygame.display.flip()
