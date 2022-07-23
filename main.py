# main.py

import pygame
import sys

from action import *
from actionProcessor import *

pygame.init()

screen = pygame.display.set_mode((700, 700))

action_processor = ActionProcessor()

hand_mode = True
allow_next = False

for i in range(1, 11):
    a = Action(lambda x: print(x*x), [i])
    action_processor.add_action(a)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                allow_next = True


    if action_processor.has_actions_in_queue():
        if not(hand_mode) or allow_next:
            action_processor.act_first()
            allow_next = False


    pygame.display.flip()
