class Pokemon:
    __name = None
    __attack = 0
    __defense = 0
    __color = None
    __maxHP = 0
    __currentHP = 0
    __atkList = None
    __canBePicked = True
    __frontPNG = None
    __frontPos = None
    __backPNG = None
    __backPos = None
    

    def __init__(self, name, attack, defense, color, hp, atkList, frontPNG, backPNG, frontPos, backPos):
        self.__name = name
        self.__atk = attack
        self.__def = defense
        self.__color = color
        self.__maxHP = self.__currentHP = hp
        self.__atkList = atkList
        self.__frontPNG = frontPNG
        self.__backPNG = backPNG
        self.__frontPos = frontPos
        self.__backPos = backPos
        
    def returnAtks(self):
        return self.__atkList

    def attack(self, pos):
        aux = self.__atkList[pos].attack()

        if aux[0]:
            return self.__name + " used " + aux[1]
        else:
            return "There's no PP left for this movement!"
    
    def returnName(self):
        return self.__name

    def returnColor(self):
        return self.__color
    
    def Pick(self):
        self.__color.r -= 70 if self.__color.r - 70 >= 0 else 0
        self.__color.g -= 70 if self.__color.g - 70 >= 0 else 0
        self.__color.b -= 70 if self.__color.b - 70 >= 0 else 0
        self.__canBePicked = False

    def canBePicked(self):
        return self.__canBePicked

    def returnFPNG(self):
        return self.__frontPNG

    def returnBPNG(self):
        return self.__backPNG

    def returnFPos(self):
        return self.__frontPos
    
    def returnBPos(self):
        return self.__backPos

    def returnMaxHP(self):
        return self.__maxHP

    def returnCurrentHP(self):
        return self.__currentHP