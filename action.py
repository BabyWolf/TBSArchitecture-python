class Action:

    def __init__(self, function, args:list, done_trigger=None, non_actual_trigger=None):
        self.__function = function
        self.__args = args.copy()
        self.__done_trigger = done_trigger
        self.__non_actual_trigger = non_actual_trigger

    
    def actual(self):
        return self.__non_actual_trigger == None or not self.__non_actual_trigger.triggered()
      

    def act(self):
        if not self.actual():
            return

        return self.__function(*self.__args)

        
    def completed(self):
        return self.__done_trigger == None or self.__done_trigger.triggered()

    def __str__(self):
        if not self.actual():
            return "NOT ACTUAL"
        
        return "Action: " + self.__function.__name__ + " " + str(self.__args) + " " + str(self.__done_trigger)
