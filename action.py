# action.py
class Action:

    def __init__(self, function, args:list):
        self.__function = function
        self.__args = args.copy()

    def act(self):
        self.__function(*self.__args)
