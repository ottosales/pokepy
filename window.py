class Window:
    __width = 0
    __height = 0
    __color = (0, 0, 0)

    def __init__(self, largura, altura):
        self.__width = largura
        self.__height = altura

    def returnWinSize(self):
        return (self.__width, self.__height)

    def returnColor(self):
        return self.__color