'''...................................................................
......................................................................
.................::;;;irrXX...................;;iiirrXX...............
...............::;:::::::;:..................::::::::iiX..............
.............::;:,:,...............................,,,,:XXX...........
............:;:,:.......................................::X...........
..........:::.............................................:XX.........
.........::::............HHHHHHHHHHHHHHHHHHHHH.............::XX.......
.........:::........hhhhMMMMMMMMHHHHHHHHHMMMMHHHHHH..........ii.......
.......:::.......hhhhhhhhhhhhhMMMMMMMHMMMHMMHHMMMMMMMMM......,:i......
.............MMhhhhhhhhhhhhMhMMMMMMMMMMMMMMMMMMMMMMMMHHH..............
............MhhhhMHHHHHhh33hhhhMMMMMMMMMMHMMMMhhHHHGHHHMHHG...........
..........MMMGGSSSSSSSSSSSSM33hhMMMMMMMMMMMhhGSSSSSSSSSSSSGGG.........
..........MMMGGSSSSSSSSSSSGM33hhMMMMMMMMMMMhhGSSSSSSSSSSSSGGG.........
.........HMMGSSSSSSSSSSSSSSSGG55hMMMMMMMMhhSSSSSSSSSSSSSSSSGGGG.......
.......HHMGGGSSGSSSGGGGGGSSSSSGG5hhMMMhh3SSGSSSSGGGGSSSSSSSSSSS.......
.......MMHGGSSGGGM;;:::::XXGSSSG333hhh35HSSSSM;;::;;;22SSSSSSSSG......
.....MMhhHGGGGG22:::::::::;2GGSSG5533322GGG33:::::;sX##GGSSSSSSSGG....
.....33MMHGGGMM,,:::::::::;SMMSSSAA55555GGH,,:::;:;rrMhHA2SSSSSSGH....
....h55MMHHGG33::::::::::;;;riSSSAA55233HMM:::::;;;;;iir;;SSSSSSGH....
....322MMHHHH33::::;::;::::::;GSSAA55255HMM:::;:::::::;;::GSGSSSHHGG..
....522MhMHHHMM::::::::::::,33SGGXX522A2HHHrr::::::::::,XXSSSSSSMMGH..
..552A233MHHHHG22::::::::::AGGSGHAA222XXMHHHHi:::::,,,,:GGSSSSSSMMHH..
..55AAA22MHHHHHHGhss::;AAMMGGGGS5225522A3HHGGHhhXs::;22GSGSSSSSGMhHH..
..22AAAXXhMMHHHHHGGGGGGGGGGGGGHHA2255522AMMHHGGGGGSGGGGSSSSSSSSMMMHH..
..222A2AAAMMMMHHHHHGHGHGGHGGGHAA25555555222HMHGGGGGGGGGGGGGGSMHhhMHH..
..22AAAAAAXX3MHHHHHHHHHHHGHMAA22555555522AAAAMHHHHHGGGGGGGGMM33MhMHH..
..55AAAAAAAAXAA33hMMMMM33AAX225255555555552A2X22hMMHMMHMhhA55hhhMMHH..
....2AAAAA2222AXXssssssXX222225555555555555552A2XXsAXXXX;;iAA33hhMHH..
....2AAAAA2222222222A22222225555555555555555525555555552;;iii55hhhGH..
....2AAAAAAA2222222222222222222252552555555555555555555srrX2233MMMGG..
....5A2AAAAAA2222222222222222525255555555555555555522ssr2A55333hHH....
.....22AAAAXAAAXXA22222222222222222222222225222222Xiisr25553553MHG....
.....5522AAAXXAss;rrssAAA2AAAAAAAAXAAXAAAA2AAXssii;ss2555555333H......
.......22AAAAAXAAsii::;;irrrssssssrrrriiiii;;;;;ssA2555555533MM.......
.........2AAXXXXXAAAXssii;;:;::::;;;;;;;iiissXAA22222222255hhHH.......
..........22AAXXXXXXAAAAAAXXXXXAXXAXXXXXXAAAAAAAA2A2AAA2553MM.........
............2AAXXXXXXXXXXXXAAXAXAXAAAAXAAAAAAAAA2AAAAA2533M...........
.............22AAXXXXsXXXXXXXXAAAXXXXAAXXXXXXAXXXX2AA553MM............
...............222AAXXXXsXsXXsXssXsXXsXsXXXssXXXA225533...............
..................2222AAXXXXsXXsXXssssssXXsXXXAA223...................
.......................2222AAAXXXsXssXXXXXA22555......................
..............................22AAAAAAAA2..........................'''

import time
import sys
import os
import msvcrt
import pygame
import threading

pygame.mixer.init()

#ЦВЕТА ДЛЯ ТЕКСТА
class colorText:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    DARKGREEN = '\033[38;5;22m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLANK = '\033[0m' 
    BLACK = '\033[30m'
    GRAY = '\033[37m'
    BETTERGRAY = '\033[90m'
    DARKRED = '\033[38;5;52m' 
    BROWN = '\033[38;5;94m'
    ORANGE = '\033[38;5;208m'
    ORANGEL = '\033[38;5;214m'
    ORANGELL = '\033[38;5;220m'

    REDBACK = '\033[48;5;52m'
    YELLOWBACK = '\033[48;5;220m'
    

#ЗВУКИ
soundTrap = pygame.mixer.Sound("D:/UniverProjects/VvedenieVProgrammirovanie/ProjectGame/GameVvedenieVProgrammirovanie/audio/trap.wav")
soundLoot  = pygame.mixer.Sound("D:/UniverProjects/VvedenieVProgrammirovanie/ProjectGame/GameVvedenieVProgrammirovanie/audio/takeLoot.wav")
soundBoom = pygame.mixer.Sound("D:/UniverProjects/VvedenieVProgrammirovanie/ProjectGame/GameVvedenieVProgrammirovanie/audio/boom.wav")
soundBox = pygame.mixer.Sound("D:/UniverProjects/VvedenieVProgrammirovanie/ProjectGame/GameVvedenieVProgrammirovanie/audio/box.wav")
soundDeath = pygame.mixer.Sound("D:/UniverProjects/VvedenieVProgrammirovanie/ProjectGame/GameVvedenieVProgrammirovanie/audio/death.wav")
soundCashout = pygame.mixer.Sound("D:/UniverProjects/VvedenieVProgrammirovanie/ProjectGame/GameVvedenieVProgrammirovanie/audio/cashout.mp3")
soundMine = pygame.mixer.Sound("D:/UniverProjects/VvedenieVProgrammirovanie/ProjectGame/GameVvedenieVProgrammirovanie/audio/mine.wav")
soundExit = pygame.mixer.Sound("D:/UniverProjects/VvedenieVProgrammirovanie/ProjectGame/GameVvedenieVProgrammirovanie/audio/exitCash.wav")

pygame.mixer.music.load("D:/UniverProjects/VvedenieVProgrammirovanie/ProjectGame/GameVvedenieVProgrammirovanie/audio/Laseraxe.ogg")
    
#Прикольная анимация
def load_animation():

    load_str = "starting your console application..."
    ls_len = len(load_str)



    animation = "|/-\\"
    anicount = 0
    

    counttime = 0        

    i = 0                     

    while (counttime != 100):

        time.sleep(0.075) 

        load_str_list = list(load_str) 
        
        x = ord(load_str_list[i])
        
        y = 0                             

        if x != 32 and x != 46:             
            if x>90:
                y = x-32
            else:
                y = x + 32
            load_str_list[i]= chr(y)
        
        res =''             
        for j in range(ls_len):
            res = res + load_str_list[j]
            
        sys.stdout.write("\r"+res + animation[anicount])
        sys.stdout.flush()
        load_str = res

        
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len
        counttime = counttime + 1
    
    if os.name =="nt":
        os.system("cls")
    

# BREAKPOINT
'''
ЭТО НЕ УЧЕБНАЯ ТРЕВОГА. 
'''
# DANGER, DANGER




'''#============================================='''
        #ВСЕ ПРО UI
'''#============================================='''



OFFSET_X = 110  # количество пробелов слева
OFFSET_Y = 2  # количество пустых строк сверху

#Таймер
gameTime = 60
timerBarLength = 30



def drawUITop():

    global gameTime, startTime, remT

    elapsed = int(time.time() - startTime)
    remT = max(0, gameTime - elapsed)
    minT = remT // 60
    secT = remT % 60

    filledLength = int(timerBarLength * remT / gameTime)
    bar = colorText.RED + "█" * filledLength + colorText.BLANK
    bar += colorText.DARKRED + "░" * (timerBarLength - filledLength) + colorText.BLANK

    for _ in range(OFFSET_Y):
            print()
    print(" " * (OFFSET_X - 20) + "╔════════════════════╧═════════════════╧════════════════════╗")
    print()
    print(" " * (OFFSET_X + 3) + colorText.YELLOW + "=== СТАТУС ===" + colorText.BLANK)
    print()

    print(" " * (OFFSET_X - 14) + colorText.ORANGELL + f"Игрок Ⅰ - HP: {colorText.BLANK}[{colorText.GREEN + (curPlayerOneHP * '▓█') + (maxPlayerOneHP - curPlayerOneHP) * '▁▁' + colorText.BLANK}]{colorText.ORANGELL}  |  Игрок Ⅱ - HP: {colorText.BLANK}[{colorText.GREEN + (curPlayerTwoHP * '▓█') + (maxPlayerTwoHP - curPlayerTwoHP) * '▁▁' + colorText.BLANK}]")
    print()

    inventoryUI1 = formatInventory(playerOneInventory)
    if cashoutTimerP1 is not None:
        progress = min(1.0, (time.time() - cashoutTimerP1) / cashoutRequired)
        filled = int(7 * progress)
        inventoryUI1 = "[" + colorText.GREEN + "█" * filled  + "░" * (7 - filled) + colorText.BLANK + "]"

    inventoryUI2 = formatInventory(playerTwoInventory)
    if cashoutTimerP2 is not None:
        progress = min(1.0, (time.time() - cashoutTimerP2) / cashoutRequired)
        filled = int(7 * progress)
        inventoryUI2 = "[" + colorText.GREEN + "█" * filled  + "░" * (7 - filled) + colorText.BLANK + "]"
    print(" " * (OFFSET_X - 22) + colorText.ORANGEL +
          f"Игрок Ⅰ - Инвентарь: {colorText.BLANK}{inventoryUI1}" + colorText.ORANGEL + "  |  " + f"Игрок Ⅱ - Инвентарь: {colorText.BLANK}{inventoryUI2}")
    
    print()
    print(" " * (OFFSET_X - 17) + colorText.ORANGE + f"Игрок Ⅰ - Награбленное: {colorText.YELLOW}{lootCount1}{colorText.ORANGE}" + "  |  " + f"Игрок Ⅱ - Награбленное: {colorText.YELLOW}{lootCount2}{colorText.BLANK}")
    print()

    print(" " * (OFFSET_X - 13) + colorText.RED + f"ОСТАЛОСЬ: {minT:01}:{secT:02} [{bar}]" + colorText.BLANK)
    print()

    print(" " * (OFFSET_X - 20) + "╚════════════════════╤═════════════════╤════════════════════╝")
    print()
    print()

def drawUIBottom():
    print()
    print()
    print(" " * (OFFSET_X - 25) + "╔═════════════════════════╧═════════════════╧═════════════════════════╗")
    print()
    print(" " * (OFFSET_X + 3) + colorText.CYAN + "=== ПОМОЩЬ ===" + colorText.BLANK)
    print(" " * (OFFSET_X - 7) + "WASD — Игрок 1   |   OKL; — Игрок 2")
    print()
    print(" " * (OFFSET_X - 24) + colorText.DARKGREEN + "[₡]" + colorText.BLANK + " - Кэшаут  |  Деньги - " + colorText.YELLOW + "[$] / [₿]" + colorText.BLANK + " - Тоже Деньги  |  Опасность - " + colorText.RED + "[‼]" + colorText.BLANK)
    print() 
    print() 
    print(" " * (OFFSET_X - 5) + "Неси " + colorText.YELLOW + "ДЕНЬГИ [$] " + colorText.BLANK + "на " + colorText.DARKGREEN + "КЭШАУТ [₡]" + colorText.BLANK)
    print()
    print(" " * (OFFSET_X - 26) + "Готовы уходить? Вставай на " + colorText.DARKGREEN + "КЭШАУТ [₡]" + colorText.BLANK + " и ЖДИ. Бонусный лут " + colorText.BLUE + "САМОМУ ПЕРВОМУ!" + colorText.BLANK)
    print()
    print(" " * (OFFSET_X - 25) + "╚══════════════════════════╤═════════════════╤══════════════════════════╝")

def drawShopScreen():
    for _ in range(OFFSET_Y+4):
        print()
    print("\033[H", end="")  # Очистка экрана
    print()
    print()
    print()
    print(" " * (OFFSET_X - 6) + colorText.YELLOW + "=== ЭКРАН МАГАЗИНА ===" + colorText.BLANK)
    print()
    print(" " * (OFFSET_X - 17) + colorText.ORANGE + f"Игрок Ⅰ - Деньги: {colorText.YELLOW}{lootCount1}{colorText.ORANGE}" + "  |  " + f"Игрок Ⅱ - Деньги: {colorText.YELLOW}{lootCount2}{colorText.BLANK}")
    print()
    print(" " * (OFFSET_X - 17) + colorText.ORANGEL + f"Бомбы Ⅰ - {colorText.BLUE}{playerOneBombs}{colorText.ORANGEL}" + "       |--|--|       " + f"{colorText.BLUE}{playerTwoBombs}{colorText.ORANGEL} - Ⅱ Бомбы")
    print()
    print(" " * (OFFSET_X - 17) + colorText.ORANGELL + f"Стены Ⅰ - {colorText.CYAN}{playerOneWalls}{colorText.ORANGELL}" + "     |----|----|     " + f"{colorText.CYAN}{playerTwoWalls}{colorText.ORANGELL} - Ⅱ Стены" + colorText.BLANK)
    print()
    print(" " * (OFFSET_X - 25) + colorText.YELLOW + "╟─────────────────────── ПРЕДМЕТЫ ───────────────────────╢" + colorText.BLANK)
    print()
    print(" " * (OFFSET_X - 10) + colorText.GREEN + "[1] Купить БОМБУ (3 лута)")
    print()
    print(" " * (OFFSET_X - 10) + "[2] Купить СТЕНУ (4 лута)" + colorText.BLANK)
    print()
    print(" " * (OFFSET_X - 14) + colorText.BLUE + "[ENTER] — продолжить к следующему уровню" + colorText.BLANK)
    print()
    print()
    print(" " * (OFFSET_X - 5) + colorText.RED + "=== ПОДСКАЗКА ===" + colorText.BLANK)
    print()
    print(" " * (OFFSET_X - 58) + colorText.DARKRED + f"'Q' = Игрок 1 купил бомбу. {colorText.BLACK}|-|{colorText.DARKRED} 'E' = Игрок 1 купил стену.{colorText.BLUE} |---|---| {colorText.DARKRED}'I' = Игрок 2 купил бомбу. {colorText.BLACK}|-|{colorText.DARKRED} 'P' = Игрок 2 купил стену." + colorText.BLANK)


    sys.stdout.flush()

#РИСУЕТ ПОЛЕ
def drawField(posPlayerOneX, posPlayerOneY, posPlayerTwoX, posPlayerTwoY):
    for y in range(boardSizeY):
        cubeInside = " " * (OFFSET_X - 18)  # горизонтальный сдвиг
        for x in range(boardSizeX):


            #Визибилити для игроков с округлением
            distX1, distY1 = abs(x - posPlayerOneX), abs(y - posPlayerOneY)
            distX2, distY2 = abs(x - posPlayerTwoX), abs(y - posPlayerTwoY)

            dist1 = max(distX1, distY1) + min(distX1, distY1) //2
            dist2 = max(distX2, distY2) + min(distX2, distY2) //2

            #Скрытие клеток если игрок слишком далеко
            if dist1 > 6 and dist2 > 6:
                cubeInside += '\033[38;5;232m' + '[░]' + colorText.BLANK  # темно-серый фон
                continue
            elif dist1 > 3 and dist2 > 3:
                cubeInside += colorText.BETTERGRAY + '[░]' + colorText.BLANK  # темно-серый фон
                continue

            cell = ""

            if (x, y) in wallsMap:
                cell += colorText.GRAY + "███" + colorText.BLANK

            elif x == posPlayerOneX and y == posPlayerOneY and x == posPlayerTwoX and y == posPlayerTwoY:
                cell += colorText.CYAN+ "[3]" + colorText.BLANK

            elif x == posPlayerOneX and y == posPlayerOneY:
                cell += colorText.BLUE + "[1]" + colorText.BLANK

            elif x == posPlayerTwoX and y == posPlayerTwoY:
                cell += colorText.GREEN + "[2]" + colorText.BLANK

            elif (x, y) in loot:
                cell += colorText.YELLOW + "[$]" + colorText.BLANK

            elif (x, y) in bigLoot:
                cell += colorText.YELLOW + "[₿]" + colorText.BLANK

            elif (x, y) in trap:
                cell += colorText.RED + "[‼]" + colorText.BLANK

            elif (x, y) in mine:
                cell += colorText.DARKRED + "[⚠]" + colorText.BLANK     

            elif (x, y) in box:
                cell += colorText.BROWN + "[-]" + colorText.BLANK     

            elif (x, y) in cashout:
                cell += colorText.DARKGREEN + "[₡]" + colorText.BLANK  

            else:
                cell += "[ ]"


            if (x, y) in dmgZone:
                cell = colorText.REDBACK + cell + colorText.BLANK
            elif (x, y) in blink:
                cell = colorText.YELLOWBACK + cell + colorText.BLANK
            


            cubeInside += cell
            

        print(cubeInside)

def drawGameUI():
    print("\033[H", end="") 
    drawUITop()
    drawField(playerOneX, playerOneY, playerTwoX, playerTwoY)
    drawUIBottom()

    # Это вроде надо, но я хз почему без него оно начинает работать
    sys.stdout.flush()

def tutorialScreen():
    for _ in range(OFFSET_Y):
            print()
    print(" " * (OFFSET_X - 20) + "╔════════════════════╧═════════════════╧════════════════════╗")
    print()
    print(" " * (OFFSET_X + 3) + colorText.YELLOW + "=== Туториал ===" + colorText.BLANK)
    print()

    print(" " * (OFFSET_X - 14) + colorText.ORANGELL + f"Ваша задача - собрать {colorText.GREEN}ДЕНЬГИ{colorText.YELLOW} - [$]/[₿]" + colorText.BLANK)
    print()
    print(" " * (OFFSET_X - 14) + colorText.ORANGEL + f"Вы управляете кубиками с номерами {colorText.BLUE}[1]{colorText.ORANGEL} и {colorText.GREEN}[2]" + colorText.BLANK)
    print()
    print(" " * (OFFSET_X - 20) + colorText.ORANGEL + f"Сверху находятся ваши параметры - ивентарь, здоровье и собранный ЛУТ.")
    print()
    print(" " * (OFFSET_X - 45) + colorText.ORANGEL + f"Чтобы СОХРАНИТЬ свой лут, вы должны перейти на клетку {colorText.DARKGREEN}[₡]{colorText.ORANGEL}. Если долго на ней стоять - вы сбежите и не потеряете свой ЛУТ." + colorText.BLANK)
    print()
    print(" " * (OFFSET_X - 28) + colorText.ORANGEL + f"Избегайте ловушек {colorText.RED}[!!]{colorText.ORANGEL} и мин {colorText.DARKRED}[⚠]{colorText.ORANGEL}. Я слышал, что коробки {colorText.BROWN}[-]{colorText.ORANGEL} можно сломать минами!")    
    print()
    print(" " * (OFFSET_X - 6) + colorText.BLUE + "Нажмите ENTER для продолжения" + colorText.BLANK)
    print()
    print(" " * (OFFSET_X - 20) + "╚════════════════════╤═════════════════╤════════════════════╝")
    print()
    print()

    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\r' or key == b'\n':  # Enter
                sys.stdout.flush()
                clear()
                print("\033[2J\033[H", end="")
                break
                


#И опять, да из ГПТ. Извините
def drawCashScreen(playerOneCash, playerTwoCash, died1, died2, cashed1, cashed2, cashoutOrder):
    global gameIsActive
    global levelIndex, gameIsActive
    global boardSizeX, boardSizeY
    global playerOneX, playerOneY, playerTwoX, playerTwoY
    global wallsMap, loot, bigLoot, trap, mine, blink, box, cashout

    # --- Рассчёт финальных сумм ---
    base1 = playerOneCash
    base2 = playerTwoCash

    final1 = base1 * (0.5 if died1 else 1.0)
    final2 = base2 * (0.5 if died2 else 1.0)

    if cashoutOrder:
        firstOut = cashoutOrder[0]
        if firstOut == "P1" and not died1:
            final1 *= 1.25
        elif firstOut == "P2" and not died2:
            final2 *= 1.25

    final1 = int(final1)
    final2 = int(final2)

    print("\033[2J\033[H", end="")
    # --- Условия бонусов ---
    bonusText = []
    if died1: bonusText.append("Игрок Ⅰ умер → получает 50% лута")
    if died2: bonusText.append("Игрок Ⅱ умер → получает 50% лута")
    if cashoutOrder:
        bonusText.append(f"Игрок, который вышел первым ({cashoutOrder[0]}) получает +25% бонус")
    if not bonusText:
        bonusText.append("Нету бонусов!")
    #for _ in range(OFFSET_Y):
            #print()
    print(" " * (OFFSET_X - 20) + "╔════════════════════╧═════════════════╧════════════════════╗\n")
    print(" " * (OFFSET_X) + colorText.ORANGEL + "=== НАГРАБЛЕННОЕ ===" + colorText.BLANK + "\n")
    print(" " * (OFFSET_X - 5) + colorText.ORANGE + f"Игрок Ⅰ: изначально {colorText.YELLOW}{base1}{colorText.ORANGE} → всего {colorText.YELLOW}{final1}{colorText.BLANK}\n")
    print(" " * (OFFSET_X - 5) + colorText.ORANGE + f"Игрок Ⅱ: изначально {colorText.YELLOW}{base2}{colorText.ORANGE} → всего {colorText.YELLOW}{final2}{colorText.BLANK}\n")
    print(" " * (OFFSET_X - 20) + "╚════════════════════╤═════════════════╤════════════════════╝\n")
    print(" " * (OFFSET_X) + colorText.CYAN + "=== Доп. Условия ===" + colorText.BLANK)
    for line in bonusText:
        print(" " * (OFFSET_X - 20) + colorText.YELLOW + "- " + line + colorText.BLANK)
    print("\n")
    sys.stdout.flush()

    return playerOneCash, playerTwoCash

'''#============================================='''
        #ИГРОВАЯ ЛОГИКА И ВСЕ ПРИСУЩЕЕ
'''#============================================='''

gameIsActive = True
levelIndex = 1

curPlayerOneHP = maxPlayerOneHP = maxPlayerTwoHP = curPlayerTwoHP = 3
invTime = 0.5
gotHitPlOne = gotHitPlTwo = 0

playerOneInventory = [None, None, None]
playerTwoInventory = [None, None, None]
lootCount1 = lootCount2 = 0

dmgZone = []
blink = []

cashoutTimerP1 = None
cashoutTimerP2 = None
cashoutRequired = 3
cashoutOrder = []

playerOneDied = False
playerTwoDied = False
playerOneCashedOut = False
playerTwoCashedOut = False

playerOneBombs = playerTwoBombs = 0
playerOneWalls = playerTwoWalls = 0




def formatInventory(inventory):
    result = ""
    for item in inventory:
        if item == "$":
            result += colorText.YELLOW + "[$]" + colorText.BLANK
        elif item == "₿":
            result += colorText.YELLOW + "[₿]" + colorText.BLANK
        else:  
            result += "[ ]"
    
    while len(result) < 3 * 3:
        result += "[ ]"
    return result
    
def checkPlayer(posX, posY):
        
    # Берет ОБЩИЙ lootCount, а не создает новый внутри функции. Запомнить
    global lootCount1, lootCount2

    playerInventory = playerOneInventory if (posX == playerOneX and posY == playerOneY) else playerTwoInventory


    if (posX, posY) in loot and addToInventory(playerInventory, "$"):
        loot.remove((posX, posY))
        soundLoot.play()

    elif (posX, posY) in bigLoot and addToInventory(playerInventory, "₿"):
        bigLoot.remove((posX, posY))
        soundLoot.play()

    elif (posX, posY) in trap:
        trap.remove((posX, posY))
        damagePlayer(posX, posY, 1)
        soundTrap.play()

    elif (posX, posY) in dmgZone:
        damagePlayer(posX, posY, 1)

    elif (posX, posY) in mine:
        mine.remove((posX, posY))
        soundMine.play()
        threading.Thread(target=createDmgZone, args=(posX-1, posY-1, posX+1, posY+1, 1), daemon=True).start()
    
    elif (posX, posY) in cashout:
        if (playerInventory == playerOneInventory): 
            lootCount1 = cashoutInv(playerInventory, lootCount1)
        else: 
            lootCount2 = cashoutInv(playerInventory, lootCount2)

def checkBox(posX, posY):
    if (posX, posY) in box:
        box.remove((posX, posY))
        soundBox.play()

def addToInventory(inventory, item):
    for i in range(3):
        if inventory[i] is None:
            inventory[i] = item
            return True
    return False

def damagePlayer(posX, posY, dmg):
    global curPlayerOneHP, curPlayerTwoHP, gameIsActive, gotHitPlOne, gotHitPlTwo

    curTime = time.time()

    if posX == playerOneX and posY == playerOneY:

        if curTime - gotHitPlOne >= invTime:
            curPlayerOneHP -= dmg
            gotHitPlOne = curTime
            

    elif posX == playerTwoX and posY == playerTwoY:

        if curTime - gotHitPlTwo >= invTime:        
            curPlayerTwoHP -= dmg
            gotHitPlTwo = curTime

    checkPlayerDeath()

def createDmgZone(posX1, posY1, posX2, posY2, timeSleep):
    global dmgZone, blink   

    i = 2
    while i > 0:
        for x in range(posX1, posX2+1):
            for y in range(posY1, posY2+1):
                blink.append((x, y))
        time.sleep(0.15)

        for x in range(posX1, posX2+1):
            for y in range(posY1, posY2+1):
                blink.remove((x, y))
        time.sleep(0.15)
        i -= 1

    for x in range(posX1, posX2+1):
        for y in range(posY1, posY2+1):
            dmgZone.append((x, y))
            if (x, y) == (playerOneX, playerOneY):
                damagePlayer(playerOneX, playerOneY, 1)
            if (x, y) == (playerTwoX, playerTwoY):
                damagePlayer(playerTwoX, playerTwoY, 1)
            checkBox(x, y)
            soundBoom.play()

    time.sleep(timeSleep)

    for x in range(posX1, posX2+1):
        for y in range(posY1, posY2+1):
            dmgZone.remove((x, y))

def cashoutInv(playerInventory, playerLootCount):

    addedLoot = 0

    for item in playerInventory:
        if item == "$":
            playerLootCount += 1
            addedLoot += 1
        elif item == "₿":
            playerLootCount += 3
            addedLoot += 1

    for i in range(3):
        playerInventory[i] = None

    if addedLoot != 0:
        soundCashout.play()
    return playerLootCount

def checkPlayerDeath():
    global curPlayerOneHP, curPlayerTwoHP, playerOneX, playerOneY, playerTwoX, playerTwoY, playerOneInventory, playerTwoInventory, playerOneDied, playerTwoDied

    if curPlayerOneHP <= 0:
        playerOneX = playerOneY = -999
        playerOneInventory = [None, None, None]
        soundDeath.play()
        playerOneDied = True

    if curPlayerTwoHP <= 0:
        playerTwoX = playerOneY = -999
        playerTwoInventory = [None, None, None]
        soundDeath.play()
        playerTwoDied = True

# Украл код из ГПТ, мало времени было
def checkCashoutStanding():
    global cashoutTimerP1, cashoutTimerP2
    global playerOneX, playerOneY, playerTwoX, playerTwoY
    global playerOneCashedOut, playerTwoCashedOut
    global cashoutOrder

    current_time = time.time()

    # --- PLAYER 1 ---
    if (playerOneX, playerOneY) in cashout:
        if cashoutTimerP1 is None:
            cashoutTimerP1 = current_time
        elif current_time - cashoutTimerP1 >= cashoutRequired:
            playerOneX = -999
            playerOneY = -999
            if not playerOneCashedOut:
                playerOneCashedOut = True
                cashoutOrder.append("P1")
            soundExit.play()
    else:
        cashoutTimerP1 = None

    # --- PLAYER 2 ---
    if (playerTwoX, playerTwoY) in cashout:
        if cashoutTimerP2 is None:  
            cashoutTimerP2 = current_time
        elif current_time - cashoutTimerP2 >= cashoutRequired:
            playerTwoX = -999
            playerTwoY = -999
            if not playerTwoCashedOut:
                playerTwoCashedOut = True
                cashoutOrder.append("P2")
            soundExit.play()
    else:
        cashoutTimerP2 = None


'''#============================================='''
        #КАРТА (МОЖНО РИСОВАТЬ РУКАМИ)
'''#============================================='''

''' Легенда:
' ' (пробел) — пустая клетка
'█' — стена
'1' — игрок 1
'2' — игрок 2 
'$' - Лут(1) 
'₿' - Лут(3)
'!' - Ловушка
'*' - Мина
'-' - Коробка
'₡' - Кэшаут
'''

#ПЕРВАЯ КАРТА
mapFirstLayout = [
    "███████████████████",
    "█₡1     $█   ██$ *█",
    "█2    !  █*█$██*█ █",
    "█ █      - █  ₿-█$█",
    "█ $      █ █₿$*₿█ █",
    "███  $ ██████████!█",
    "█        █$   !-*$█",
    "█$██████ █  $  --*█",
    "█  █ ₿█ $█₿ ! ██* █",
    "██ *  * !█!$  ** *█",
    "█        *█████  ██",
    "█ *  $* *- !    ! █",
    "█--! █--!  █$  ██₿█",
    "█ $   !   !     ███",
    "█   █    *   $  !₡█",
    "█*  *  $  █     ███",
    "█ ! -     -  *  * █",
    "██*█*█*█*█*█ !-*-*█",
    "█₿ ! ₿ !   $   $*₿█",
    "███████████████████",
]

mapSecondLayout = [
    "███████████████████",
    "█₡1     -$-   ₿   █",
    "█   $   █₿█     * █",
    "█       █ █ ₿   $ █",
    "██!██-█ ██████!█*██",
    "█ * - █$   $ █ █  █",
    "█ !  $██████ █ █*██",
    "█ *  $ !     - █ !█",
    "█-   -   $ ███ * *█",
    "█$ ! ₿  *   *  - ₿█",
    "█* $      !  ██████",
    "█  -  * ██  ██  $ █",
    "██*█! $ █ !  █ █  █",
    "██ * ██ ███-!█ █  █",
    "█₿ █ █   $  $  █* █",
    "██!███████████!█ ██",
    "█   $   $ █₿█   * █",
    "█         █ █     █",
    "█ ₿    ₿  -$-   2₡█",
    "███████████████████",
]

mapThirdLayout = [
    "███████████████████",
    "█₡1  *   $   *  2₡█",
    "█   !   $$$  *  ! █",
    "█!   *   *   !    █",
    "██-█████ █ █████-██",
    "█ *     $*$     * █",
    "█   !$  *  $!  *  █",
    "█$ █████████████ $█",
    "█!  *   $ $  *   !█",
    "█████████ █████████",
    "█$ ₿  !*!$!*  ₿  $█",
    "█      *! !*    ! █",
    "█ ₿! ₿ *!$!* ₿ !₿ █",
    "█*███████*███████ █",
    "█   * $  $  $ *  *█",
    "████ █████████ ████",
    "█₿  *  ₿!-!₿  *! ₿█",
    "█! ! ██--*--██   !█",
    "█₿*  *$-!₡!-$* !*₿█",
    "███████████████████",
]

#СОЗДАНИЕ КАРТЫ
def createMap(mapLayout):
    boardSizeY = len(mapLayout)
    boardSizeX = max(len(row) for row in mapLayout)


    '''---------------------------------------------------------'''
    # ПРОПИСЬ ВСЕХ ТИПОВ РАЗЛИЧНЫХ ВЕЩЕЙ НА КАРТЕ (Стены, лут и тд)
    '''---------------------------------------------------------'''

    #Великолепный код, слава enumerate, слава кортежам о7 о7 о7
    wallsMap = []
    loot = []
    bigLoot = []
    trap = []
    mine = []
    box = []
    cashout = []

    playerOneX = playerOneY = None
    playerTwoX = playerTwoY = None

    for y, row in enumerate(mapLayout):
        for x, cell in enumerate(row):  
            if cell == '█':
                wallsMap.append((x, y))
            elif cell == '1':
                playerOneX, playerOneY = x, y
            elif cell == '2':
                playerTwoX, playerTwoY = x, y

            # Дальше идет все вещи
            elif cell == '$':
                loot.append((x, y))
            elif cell == '₿':
                bigLoot.append((x, y))
            elif cell == '!':
                trap.append((x, y))
            elif cell == '*':
                mine.append((x, y))
            elif cell == '-':
                box.append((x, y))
            elif cell == '₡':
                cashout.append((x, y))
            


    if playerOneX is None:
        playerOneX, playerOneY = 1, 1
    if playerTwoX is None:
        playerTwoX, playerTwoY = 3, 1

    #ДОБАВЛЯЙ ВСЕ НОВЫЕ ВЕЩИ СЮДА
    return boardSizeX, boardSizeY, playerOneX, playerOneY, playerTwoX, playerTwoY, wallsMap, loot, bigLoot, trap, mine, blink, box, cashout

#И СЮДА
#Обязательное первое уточнение, в процессе буду менять только mapFirstLayout на mapSecondLayout и mapThirdLayout 
boardSizeX, boardSizeY, playerOneX, playerOneY, playerTwoX, playerTwoY, wallsMap, loot, bigLoot, trap, mine, blink, box, cashout = createMap(mapFirstLayout)



'''#============================================='''
                  #МЕЛКИЕ ФУНКЦИИ
'''#============================================='''


#Может ли двигаться в клетку
def can_move(x, y):    
    return (x, y) not in wallsMap and 0 <= x < boardSizeX and 0 <= y < boardSizeY and (x, y) not in box

#ЧИСТИТ КОНСОЛЬ + ПО МЕЛОЧИ
def clear():
    os.system("") 
    print("\033[2J", end="") 
    print("\033[H", end="")

clear()

'''#============================================='''
#==================================================#

        #ЦИКЛ САМОЙ ИГРЫ, ДО ЭТОГО ПОДГОТОВКА

#==================================================#
'''#============================================='''

if __name__ == '__main__': 
    load_animation()
    
endScreenStart = None
isInEndScreen = False 
isInShop = False     

tutorialScreen()

startTime = time.time()

pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.8)

while True:

    if gameIsActive: #Считай void Update()

        allDead = (playerOneX == -999 and playerTwoX == -999)
        

        if allDead or (playerOneCashedOut and playerTwoCashedOut) or (playerOneCashedOut and playerTwoX == -999) or (playerOneX == -999 and playerTwoCashedOut):
            gameIsActive = False
            endScreenStart = time.time() 
            isInEndScreen = True
            levelIndex += 1
            
                   
        checkCashoutStanding()

        drawGameUI()

        keys = []
        if msvcrt.kbhit():
            
            #Делает очередь для инпутов. Должно пофиксить пару багов
            keys.append(msvcrt.getch().decode('latin-1').lower())

            time.sleep(0.01) #- чтоб консоль успевала прогрузиться

	
            for inputKey in keys:
                
                '''
                ВСЕ ЧТО СВЯЗЯННО С ПЕРЕДВИЖЕНИЕМ
                '''
                #ИНПУТЫ
    
                #ИГРОК 1
                if inputKey == 'w' and playerOneY > 0 and can_move(playerOneX, playerOneY-1):
                    playerOneY -= 1
                    checkPlayer(playerOneX, playerOneY)
                elif inputKey == 's' and playerOneY < boardSizeY - 1 and can_move(playerOneX, playerOneY+1):
                    playerOneY += 1
                    checkPlayer(playerOneX, playerOneY)
                elif inputKey == 'a' and playerOneX > 0 and can_move(playerOneX-1, playerOneY):
                    playerOneX -= 1
                    checkPlayer(playerOneX, playerOneY)
                elif inputKey == 'd' and playerOneX < boardSizeX - 1 and can_move(playerOneX+1, playerOneY):
                    playerOneX += 1
                    checkPlayer(playerOneX, playerOneY)
                elif inputKey == 'q' and playerOneBombs > 0:
                    mine.append((playerOneX, playerOneY))
                    playerOneBombs -= 1
                elif inputKey == 'e' and playerOneWalls > 0:
                    box.append((playerOneX, playerOneY))
                    playerOneWalls -= 1
    
                #ИГРОК 2
                if inputKey == 'o' and playerTwoY > 0 and can_move(playerTwoX, playerTwoY-1):
                    playerTwoY -= 1
                    checkPlayer(playerTwoX, playerTwoY)
                elif inputKey == 'l' and playerTwoY < boardSizeY - 1 and can_move(playerTwoX, playerTwoY+1):
                    playerTwoY += 1
                    checkPlayer(playerTwoX, playerTwoY)
                elif inputKey == 'k' and playerTwoX > 0 and can_move(playerTwoX-1, playerTwoY):
                    playerTwoX -= 1
                    checkPlayer(playerTwoX, playerTwoY)
                elif inputKey == ';' and playerTwoX < boardSizeX - 1 and can_move(playerTwoX+1, playerTwoY):
                    playerTwoX += 1
                    checkPlayer(playerTwoX, playerTwoY)
                elif inputKey == 'i' and playerTwoBombs > 0:
                    mine.append((playerTwoX, playerTwoY))
                    playerTwoBombs -= 1
                elif inputKey == 'p' and playerTwoWalls > 0:
                    box.append((playerTwoX, playerTwoY))
                    playerTwoWalls -= 1

    elif not gameIsActive:
        if isInEndScreen:
            drawCashScreen(lootCount1, lootCount2, playerOneDied, playerTwoDied, playerOneCashedOut, playerTwoCashedOut, cashoutOrder)
            time.sleep(10)
            print("\033[H\033[2J", end="")
            if levelIndex == 4:
                drawCashScreen(lootCount1, lootCount2, playerOneDied, playerTwoDied, playerOneCashedOut, playerTwoCashedOut, cashoutOrder)
                for _ in range(10):
                    print()
                print(f"Конец. Прям совсем.                                                                                              {colorText.GREEN}Спасибо за игру!{colorText.BLANK}")
                for _ in range(20):
                    print()
                exit()
            isInShop = True
            isInEndScreen = False
        elif isInShop:
            drawShopScreen()

            if msvcrt.kbhit():
                key = msvcrt.getch()

                if key == b'q': #bomb1
                    if lootCount1 >= 3:
                        lootCount1 -= 3
                        playerOneBombs += 1

                if key == b'e': #wall1
                    if lootCount1 >= 4:
                        lootCount1 -= 4
                        playerOneWalls += 1

                if key == b'i': #bomb2
                    if lootCount2 >= 3:
                        lootCount2 -= 3
                        playerTwoBombs += 1

                if key == b'p': #wall2
                    if lootCount2 >= 4:
                        lootCount2 -= 4
                        playerTwoWalls += 1


                elif key == b'\r' or key == b'\n':  # Enter
                    # загружаем следующий уровень
                    clear()
                    if levelIndex == 2:
                        (boardSizeX, boardSizeY, playerOneX, playerOneY, playerTwoX, playerTwoY, wallsMap, loot, bigLoot, trap, mine, blink, box, cashout) = createMap(mapSecondLayout)
                    elif levelIndex ==3:
                        (boardSizeX, boardSizeY, playerOneX, playerOneY, playerTwoX, playerTwoY, wallsMap, loot, bigLoot, trap, mine, blink, box, cashout) = createMap(mapThirdLayout)
                    else:
                        drawCashScreen(lootCount1, lootCount2, playerOneDied, playerTwoDied, playerOneCashedOut, playerTwoCashedOut, cashoutOrder)
                        for _ in range(10):
                            print()
                        print(f"Конец. Прям совсем.                                      {colorText.GREEN}Спасибо за игру!{colorText.BLANK}")
                        for _ in range(10):
                            print()
                        exit()
                    # сброс временного
                    playerOneDied = False
                    playerTwoDied = False   
                    curPlayerOneHP = maxPlayerOneHP
                    curPlayerTwoHP = maxPlayerTwoHP
                    playerOneCashedOut = False
                    playerTwoCashedOut = False
                    cashoutOrder = []

                    gameIsActive = True
                    inShop = False
                    startTime = time.time()

