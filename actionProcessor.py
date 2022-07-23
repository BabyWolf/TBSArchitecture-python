# actionProcessor.py
class ActionProcessor:

    def __init__(self):
        self.__actions = []


    def add_action(self, action):
        self.__actions.append(action)


    def act_first(self):
        self.__actions.pop(0).act()


    def has_actions_in_queue(self):
        return len(self.__actions) > 0
