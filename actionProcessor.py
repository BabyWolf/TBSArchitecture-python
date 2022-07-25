# actionProcessor.py
from actionList import *

class ActionProcessor:

    def __init__(self):
        self.__actions = []
        self.__current_action = None


    def add_action(self, action, urgent=False):
        if urgent: # добавление в начало очереди
            self.__actions.insert(0, action)
        else:
            self.__actions.append(action)


    def act_first(self):
        self.__current_action = self.__actions.pop(0)

        result = self.__current_action.act()
				
        if isinstance(result, ActionList):
            for i in range(len(result)):
                self.add_action(result[len(result) - 1 - i], True)


    def has_actions_in_queue(self):
        return len(self.__actions) > 0

    
    def current_in_process(self):
        return self.__current_action != None and not self.__current_action.completed()


    def get_actions(self):
        return self.__actions.copy()


    def get_current_action(self):
        return self.__current_action
