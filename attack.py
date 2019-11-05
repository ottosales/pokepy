class Attack:
    __name = None
    __power = 0
    __maxPP = 0
    __PPleft = 0
    __element = None

    def __init__(self, name, power, maxPP):
        self.__name = name
        self.__power = power
        self.__maxPP = self.__PPleft = maxPP
        
    def attack(self):
        if self.__PPleft > 0:
            self.__PPleft -= 1
            return True, self.__name, self.__power
        else: 
            return False, None, None
    
    def returnAttackName(self):
        return self.__name

    def returnAttackMaxPP(self):
        return self.__maxPP

    def returnAttackPPLeft(self):
        return self.__PPleft
