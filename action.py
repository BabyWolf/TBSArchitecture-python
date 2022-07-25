# action.py
class Action:

    def __init__(self, function, args:list, done_trigger=None):
        self.__function = function
        self.__args = args.copy()
        self.__done_trigger = done_trigger


    def act(self):
        return self.__function(*self.__args)

        
    def completed(self):
        return self.__done_trigger == None or self.__done_trigger.triggered()

    def __str__(self):
        return "Action: " + self.__function.__name__ + " " + str(self.__args) + " " + str(self.__done_trigger)
