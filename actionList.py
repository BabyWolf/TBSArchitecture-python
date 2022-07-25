# actionList.py
class ActionList(list):
    
    def __init__(self, *items):
        for i in items:
            self.append(i)
