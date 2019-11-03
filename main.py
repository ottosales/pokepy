import pygame as pg
import window as wdw 
import player as plr
import attack as atk
import pokemon as pkm 
    
def display_name_in_menu(name, text, color, pos):
    textSurf, textRect = text_objects(name, text, color)
    textRect.center = ((w.returnWinSize()[0]/2), (pos))

    win.blit(textSurf, textRect)

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def show_pkm_names():
    pg.font.init()
    text = pg.font.Font('fonts/joystix monospace.ttf', 35)

    display_name_in_menu("Choose Your Pokémon", text, (255, 255, 255), 40)

    for i in range(0, len(pokelist)):
        display_name_in_menu(pokelist[i].returnName(), text, pokelist[i].returnColor(), 125 + (i * 75))


def text_animation(string):
    text = ''
    font = pg.font.Font("fonts/joystix monospace.ttf", 26)
    win.blit(txt_bar, (0, 568))
    pg.display.update()


    for i in range(len(string)):
        text += string[i]
        textSurf, textRect = text_objects(text, font, (255, 255, 255))
        textRect.x = 50
        textRect.y = 610
        win.blit(textSurf, textRect)
        pg.display.update()
        pg.time.delay(40)

def what_will_pokemon_do(pkm_name):
    font = pg.font.Font("fonts/joystix monospace.ttf", 26)

    textSurf, textRect = text_objects("What will", font, (255, 255, 255))
    textSurf2, textRect2 = text_objects(pkm_name + " do?", font, (255, 255, 255))
    textRect.x = 50
    textRect.y = 620
    textRect2.x = 50
    textRect2.y = 680
    win.blit(textSurf, textRect)
    win.blit(textSurf2, textRect2)

    pg.display.update()

def show_moves(pkm):
    font = pg.font.Font("fonts/joystix monospace.ttf", 25)

    textSurf, textRect = text_objects(pkm.returnAtks()[0].returnAttackName(), font, (0, 0, 0))
    textSurf1, textRect1 = text_objects(pkm.returnAtks()[1].returnAttackName(), font, (0, 0, 0))
    textSurf2, textRect2 = text_objects(pkm.returnAtks()[2].returnAttackName(), font, (0, 0, 0))
    textSurf3, textRect3 = text_objects(pkm.returnAtks()[3].returnAttackName(), font, (0, 0, 0))

    

    textRect.x, textRect.y = 70, 620
    textRect1.x, textRect1.y = 370, 620
    textRect2.x, textRect2.y = 70, 685
    textRect3.x, textRect3.y = 370, 685
    
    win.blit(textSurf, textRect)
    win.blit(textSurf1, textRect1)
    win.blit(textSurf2, textRect2)
    win.blit(textSurf3, textRect3)



    pg.display.update()


pg.init()

w = wdw.Window(1024, 768)

win = pg.display.set_mode(w.returnWinSize())
pg.display.set_caption('PokePy')

run = True

rect = pg.Rect(312, 84, 400, 600)
rect2 = pg.Rect(322, 94, 380, 580)



atks = [atk.Attack("Thunderwave", 75, 10), atk.Attack("Tackle", 30, 20), atk.Attack("Flamethrower", 80, 10), atk.Attack("KEK MOVE", 200, 2)]

pikachu = pkm.Pokemon("Pikachu", 100, 60, pg.Color(250, 214, 29),  60, atks, pg.transform.scale(pg.image.load("sprites/pikachu.png"), (256, 256)), pg.transform.scale(pg.image.load("sprites/pikachu_costas.png"), (256, 256)), (640, 110), (130, 340))
charmander = pkm.Pokemon("Charmander", 100, 60, pg.Color(240, 120, 0),  60, atks, pg.transform.scale(pg.image.load("sprites/charmander.png"), (256, 256)), pg.transform.scale(pg.image.load("sprites/charmander_costas.png"), (256, 256)), (643, 121), (126, 352))
bulbasaur = pkm.Pokemon("Bulbasaur", 100, 60, pg.Color(39, 166, 50),  60, atks, pg.transform.scale(pg.image.load("sprites/bulbasaur.png"), (256, 256)), pg.transform.scale(pg.image.load("sprites/bulbasaur_costas.png"), (256, 256)), (622, 133), (120, 376))
squirtle = pkm.Pokemon("Squirtle", 100, 60, pg.Color(147, 200, 208),  60, atks, pg.transform.scale(pg.image.load("sprites/squirtle.png"), (256, 256)), pg.transform.scale(pg.image.load("sprites/squirtle_costas.png"), (256, 256)), (600, 118), (131, 372))
rhydon = pkm.Pokemon("Rhydon", 100, 60, pg.Color(198, 220, 219),  60, atks, pg.transform.scale(pg.image.load("sprites/rhydon.png"), (256, 256)), pg.transform.scale(pg.image.load("sprites/rhydon_costas.png"), (256, 256)), (598, 97), (138, 324))
gengar = pkm.Pokemon("Gengar", 100, 60, pg.Color(68, 51, 119),  60, atks, pg.transform.scale(pg.image.load("sprites/gengar.png"), (256, 256)), pg.transform.scale(pg.image.load("sprites/gengar_costas.png"), (256, 256)), (626, 113), (130, 352))
dragonite = pkm.Pokemon("Dragonite", 100, 60, pg.Color(241, 180, 109),  60, atks, pg.transform.scale(pg.image.load("sprites/dragonite.png"), (256, 256)), pg.transform.scale(pg.image.load("sprites/dragonite_costas.png"), (256, 256)), (633, 99), (130, 336))
mewtwo = pkm.Pokemon("Mewtwo", 100, 60, pg.Color(201, 168, 199),  60, atks, pg.transform.scale(pg.image.load("sprites/mewtwo.png"), (256, 256)), pg.transform.scale(pg.image.load("sprites/mewtwo_costas.png"), (256, 256)), (597, 93), (138, 316))

pokelist = [pikachu, charmander, bulbasaur, squirtle, rhydon, gengar, dragonite, mewtwo]


arrowYValue = 125
p1 = plr.Player("Red")

p2 = plr.Player("Blue")

pg.key.set_repeat(100)

clk = pg.time.Clock()

# menu de selecao de pokemons
while run and (p1.hasPkm() == False or p2.hasPkm() == False):
    clk.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False
            elif event.key == pg.K_UP and arrowYValue > 125:
                arrowYValue -= 75
                if pokelist[(arrowYValue - 125) // 75].canBePicked() == False:
                    arrowYValue -= 75
            elif event.key == pg.K_DOWN and arrowYValue < 650:
                arrowYValue += 75
                if pokelist[(arrowYValue - 125) // 75].canBePicked() == False:
                    arrowYValue += 75
            elif event.key == pg.K_RETURN:
                pokelist[(arrowYValue - 125) // 75].Pick()
                if p1.hasPkm():
                    p2.setPkm(pokelist[(arrowYValue - 125) // 75])
                else:
                    p1.setPkm(pokelist[(arrowYValue - 125) // 75])


    win.fill(w.returnColor())
    pg.draw.rect(win, (255, 255, 255), rect)
    pg.draw.rect(win, (0, 0, 0), rect2)
    show_pkm_names()
    pg.draw.polygon(win, (255, 0, 0), ((350, arrowYValue), (340, arrowYValue - 10), (340, arrowYValue + 10)))
    pg.display.update()



if p1.hasPkm():
    print(p1.returnPkmName())
if p2.hasPkm():
    print(p2.returnPkmName())


bg = pg.image.load("sprites/FundoPokemon.png")
bg = pg.transform.scale(bg, (1024, 568))
txt_bar = pg.image.load("sprites/text_bar.png")
txt_bar = pg.transform.scale(txt_bar, (1024, 200))
fgt_options = pg.image.load("sprites/fgt_options.png")
fgt_options = pg.transform.scale(fgt_options, (474, 200))
seletor = pg.image.load("sprites/le_setinha.png")
seletor = pg.transform.scale(seletor, (26, 35))
pp_bar = pg.image.load("sprites/pp_bar.png")
pp_bar = pg.transform.scale(pp_bar, (1024, 200))

win.blit(bg, (0, 0))
win.blit(txt_bar, (0, 568))
win.blit(p1.returnPkm().returnBPNG(), p1.returnPkm().returnBPos())
win.blit(p2.returnPkm().returnFPNG(), p2.returnPkm().returnFPos())
text_animation("A wild " + p2.returnPkmName() +  " appears!")
pg.display.update()
pg.time.delay(2000)

def fight(player, otherPlayer):
    run = True
    posicaoSeletor = [40, 620]

    while run:
        clk.tick(60)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False
                if event.key == pg.K_DOWN and posicaoSeletor[1] < 685:
                    posicaoSeletor[1] += 65
                elif event.key == pg.K_UP and posicaoSeletor[1] > 620:
                    posicaoSeletor[1] -= 65
                elif event.key == pg.K_RIGHT and posicaoSeletor[0] < 340:
                    posicaoSeletor[0] += 300
                elif event.key == pg.K_LEFT and posicaoSeletor[0] > 40:
                    posicaoSeletor[0] -= 300
                elif event.key == pg.K_x:
                    return

        win.blit(bg, (0, 0))
        win.blit(pp_bar, (0, 568))
        win.blit(player.returnPkm().returnBPNG(), player.returnPkm().returnBPos())
        win.blit(otherPlayer.returnPkm().returnFPNG(), otherPlayer.returnPkm().returnFPos())
        win.blit(seletor, posicaoSeletor)
        show_moves(player.returnPkm())
        pg.display.update()



def standard_p1_options():
    run = True
    posicaoSeletor = [580, 625]

    while run:

        clk.tick(60)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False
                if event.key == pg.K_DOWN and posicaoSeletor[1] < 690:
                    posicaoSeletor[1] += 65
                elif event.key == pg.K_UP and posicaoSeletor[1] > 625:
                    posicaoSeletor[1] -= 65
                elif event.key == pg.K_RIGHT and posicaoSeletor[0] < 700:
                    posicaoSeletor[0] += 220
                elif event.key == pg.K_LEFT and posicaoSeletor[0] > 580:
                    posicaoSeletor[0] -= 220
                elif event.key == pg.K_z:
                    if posicaoSeletor[0] == 580 and posicaoSeletor[1] == 625:
                        fight(p1, p2)
                    elif posicaoSeletor[0] == 800 and posicaoSeletor[1] == 690:
                        text_animation("Pokémon " + p1.returnPkmName() +  " fleed from the battle!")
                        exit()
                        
                

        win.blit(bg, (0, 0))
        win.blit(txt_bar, (0, 568))
        win.blit(fgt_options, (550, 568))
        win.blit(seletor, posicaoSeletor)
        win.blit(p1.returnPkm().returnBPNG(), p1.returnPkm().returnBPos())
        win.blit(p2.returnPkm().returnFPNG(), p2.returnPkm().returnFPos())
        what_will_pokemon_do(p1.returnPkmName())
        pg.display.update()


        
standard_p1_options()





