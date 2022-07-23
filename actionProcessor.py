# actionProcessor.py
class ActionProcessor:

    def __init__(self):
        self.__actions = []
        self.__current_action = None


    def add_action(self, action):
        self.__actions.append(action)


    def act_first(self):
        self.__current_action = self.__actions.pop(0) # запоминаем последнее выполненное

        self.__current_action.act()


    def has_actions_in_queue(self):
        return len(self.__actions) > 0

    
    def current_in_process(self):
        return self.__current_action != None and not self.__current_action.completed()


    def get_actions(self):
        return self.__actions.copy()


    def get_current_action(self):
        return self.__current_action
