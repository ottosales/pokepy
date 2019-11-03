class Player:
    __name = None
    __pkm = None

    def __init__(self, name):
        self.__name = name

    def setPkm(self, pkm):
        self.__pkm = pkm 

    def hasPkm(self):
        return True if self.__pkm != None else False

    def returnPkm(self):
        return self.__pkm

    def returnPkmName(self):
        return self.__pkm.returnName()
