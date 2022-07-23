# trigger.py
class Trigger:
    def __init__(self):
        self.__triggered = True


    def trigger(self):
        self.__triggered = True


    def refresh(self):
        self.__triggered = False


    def triggered(self):
        return self.__triggered

    def __str__(self):
        return str(self.__triggered)
