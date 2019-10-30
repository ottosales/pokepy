import pygame, random
 
class Player:
    

    def __init__(self):
        self.x = []
        self.y = []
        self.height = 30
        self.width = 30
        self.speed = 2
        self.direction = 1
        self.directionMemory = 1
        self.turnASAP = False
        self.length = 51  
        
        self.x.append(600)
        self.y.append(600)

        for i in range(1, self.length):
            self.x.append(600)
            self.y.append(self.y[i - 1] - self.speed)       

    def increaseSize(self):
        self.length += 15
        for i in range(self.length - 1, self.length - 16, -1):
            self.x.append(self.x[1])
            self.y.append(self.y[1])
        

    def update(self):
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
    
        if(self.turnASAP == True and self.x[0] % 30 == 0 and self.y[0] % 30 == 0):
            self.direction = self.directionMemory
            self.turnASAP = False

        if self.direction == 0:
            self.y[0] -= self.speed
        elif self.direction == 1:
            self.y[0] += self.speed
        elif self.direction == 2:
            self.x[0] += self.speed
        else:
            self.x[0] -= self.speed

    def draw(self):
        for i in range(0, self.length):
            pygame.draw.rect(win, (0, 255, 0), (self.x[i], self.y[i], self.height, self.width))

    def moveUp(self):
        if self.direction != 1:
            if self.x[0] % 30 == 0 and self.y[0] % 30 == 0:
                self.direction = 0
            else:
                self.directionMemory = 0
                self.turnASAP = True
    def moveDown(self):
        if self.direction != 0:
            if self.x[0] % 30 == 0 and self.y[0] % 30 == 0:
                self.direction = 1
            else:
                self.directionMemory = 1
                self.turnASAP = True    
    def moveRight(self):
        if self.direction != 3:
            if self.x[0] % 30 == 0 and self.y[0] % 30 == 0:
                self.direction = 2
            else:
                self.directionMemory = 2
                self.turnASAP = True
    def moveLeft(self):
        if self.direction != 2:
            if self.x[0] % 30 == 0 and self.y[0] % 30 == 0:
                self.direction = 3
            else:
                self.directionMemory = 3
                self.turnASAP = True

    def checkBoundaries(self, win_size):
        if self.x[0] < 0:
            return True
        if self.x[0] >= win_size[0]:
            return True
        if self.y[0] < 0:
            return True
        if self.y[0] >= win_size[1]:
            return True
        
        return False
    
    def canEat(self, apple):
        if self.x[0] == apple[0] and self.y[0] == apple[1]:
            return True
        else:
            return False

    def shouldDie(self):
        for i in range(1, self.length - 1, 1):
            if self.x[0] == self.x[i] and self.y[0] == self.y[i]:
                return True
        
        return False      

class Apple:
    
    def __init__(self):
        self.heigth = 30
        self.width = 30
        self.randX = 300
        self.randY = 300

    def update(self):
        self.randX = ((random.randint(0, 1501 - self.width)//30) * 30)
        self.randY = ((random.randint(0, 901 - self.heigth)//30) * 30)

    def draw(self):
        pygame.draw.rect(win, (255, 0, 0), (self.randX, self.randY, self.heigth, self.width))

    def returnPosition(self):
        return (self.randX, self.randY)

pygame.init()

win_x = 1500
win_y = 900

win_size = (win_x, win_y)

win = pygame.display.set_mode(win_size)

def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

def game_intro():

        pygame.font.init()
        win.fill((0,0,0))
        largeText = pygame.font.Font('joystix monospace.ttf',50)
        smallText = pygame.font.Font('joystix monospace.ttf', 25)
        pressKey = pygame.font.Font('joystix monospace.ttf', 25)

        TextSurf, TextRect = text_objects("ULTIMATE LOW QUALITY SNEK", largeText)
        TextSurf2, TextRect2 = text_objects("não é snake, é snek mesmo", smallText)
        TextSurf3, TextRect3 = text_objects("press any key to start", pressKey)

        TextRect.center = ((win_size[0]/2),(300))
        TextRect2.center = ((win_size[0]/2), (400))
        TextRect3.center = ((win_size[0]/2), (600))

        runIntro = True
        thirdTextShouldAppear = True
        thirdTextCounter = 0

        while runIntro:
            if thirdTextShouldAppear and thirdTextCounter == 120:
                thirdTextShouldAppear = False
                thirdTextCounter = 0
            elif thirdTextShouldAppear == False and thirdTextCounter == 80:
                thirdTextShouldAppear = True
                thirdTextCounter = 0
            win.fill((0,0,0))
            thirdTextCounter += 1
            win.blit(TextSurf, TextRect)
            win.blit(TextSurf2, TextRect2)
            if thirdTextShouldAppear:
                win.blit(TextSurf3, TextRect3)
            pygame.time.delay(1)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    runIntro = False
            pygame.display.update()
          

def game_die():
    win.fill(((0,0,0)))
    largeText = pygame.font.Font('joystix monospace.ttf',50)
    TextSurf, TextRect = text_objects("YOU DIED", largeText)
    TextRect.center = ((win_size[0]/2), win_size[1]/2)
    win.blit(TextSurf, TextRect)
    pygame.display.update()

    pygame.time.delay(2000)

pygame.display.set_caption("The Game")


run = True

player = Player()

appleCount = 1
apple = Apple()

game_intro()

clock = pygame.time.Clock()

pygame.key.set_repeat(100)

txt = pygame.font.Font('joystix monospace.ttf', 50)

while run:
    clock.tick(144)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.moveLeft()
                print("jfwopeirjweoirjoi")
            elif event.key == pygame.K_RIGHT:
                player.moveRight()
            elif event.key == pygame.K_UP:
                player.moveUp()
            elif event.key == pygame.K_DOWN:
                player.moveDown()
            elif event.key == pygame.K_ESCAPE:
                run = False
                
    player.update()
    if player.checkBoundaries(win_size):
        run = False

    win.fill((0, 0, 0))

    spawner = random.randint(0, 100)
    if spawner == 23 and appleCount == 0:
        apple.update()
        appleCount = 1
        
    if player.canEat(apple.returnPosition()):
        player.increaseSize()
        appleCount = 0

    if appleCount == 1:
        apple.draw()

    player.draw()
    a = txt.render("PENIS", True, (255, 0, 0))
    win.blit(a, a.get_rect())
    pygame.display.update()

    if player.shouldDie():
        run = False


    
game_die()

pygame.quit()
