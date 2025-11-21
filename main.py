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
....522MhMHHHMM::::::::::::,33SGGXX522A2HHHrr::::::::::,XXSSSSSSMMGH..№
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
OFFSET_Y = 3  # количество пустых строк сверху



def drawUITop():
    for _ in range(OFFSET_Y):
            print()
    print(" " * (OFFSET_X - 20) + "╔════════════════════╧═════════════════╧════════════════════╗")
    print()
    print(" " * (OFFSET_X + 3) + colorText.YELLOW + "=== СТАТУС ===" + colorText.BLANK)
    print()
    print(" " * (OFFSET_X - 15) + colorText.ORANGELL + f"Player Ⅰ's HP: {colorText.BLANK}[{colorText.GREEN + (curPlayerOneHP * '▓█') + (maxPlayerOneHP - curPlayerOneHP) * '▁▁' + colorText.BLANK}]{colorText.ORANGELL}  |  Player Ⅱ's HP: {colorText.BLANK}[{colorText.GREEN + (curPlayerTwoHP * '▓█') + (maxPlayerTwoHP - curPlayerTwoHP) * '▁▁' + colorText.BLANK}]")
    print()
    print(" " * (OFFSET_X - 21) + colorText.ORANGEL +"Player Ⅰ inventory: " + colorText.BLANK + formatInventory(playerOneInventory) + colorText.ORANGEL + "  |  " + "Player Ⅱ inventory: " + colorText.BLANK + formatInventory(playerTwoInventory))
    print()
    print(" " * (OFFSET_X - 17) + colorText.ORANGE + f"Player's Ⅰ Loot count : {colorText.YELLOW}{lootCount1}{colorText.ORANGE}" + "  |  " + f"Player's Ⅱ Loot count : {colorText.YELLOW}{lootCount2}{colorText.BLANK}")
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


#И опять, да из ГПТ. Извините
def drawCashScreen(playerOneCash, playerTwoCash, died1, died2, cashed1, cashed2, cashoutOrder, playerOneBombs, playerOneWalls, playerTwoBombs, playerTwoWalls):

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

    # --- Условия бонусов ---
    bonusText = []
    if died1: bonusText.append("Player Ⅰ died → receives 50% of loot")
    if died2: bonusText.append("Player Ⅱ died → receives 50% of loot")
    if cashoutOrder:
        bonusText.append(f"Player who exited first ({cashoutOrder[0]}) receives +25% bonus")
    if not bonusText:
        bonusText.append("No bonuses or penalties applied.")

    # --- Очистка экрана и вывод таблицы ---
    print("\033[2J\033[H", end="")
    print(" " * (OFFSET_X - 20) + "╔════════════════════╧═════════════════╧════════════════════╗\n")
    print(" " * (OFFSET_X + 10) + colorText.ORANGEL + "=== CASH SCREEN ===" + colorText.BLANK + "\n")
    print(" " * (OFFSET_X - 20) + colorText.ORANGE + f"Player Ⅰ: base {colorText.YELLOW}{base1}{colorText.ORANGE} → final {colorText.YELLOW}{final1}{colorText.BLANK}\n")
    print(" " * (OFFSET_X - 20) + colorText.ORANGE + f"Player Ⅱ: base {colorText.YELLOW}{base2}{colorText.ORANGE} → final {colorText.YELLOW}{final2}{colorText.BLANK}\n")
    print(" " * (OFFSET_X - 20) + "╚════════════════════╤═════════════════╤════════════════════╝\n")
    print(" " * (OFFSET_X - 15) + colorText.CYAN + "=== CONDITIONS APPLIED ===" + colorText.BLANK)
    for line in bonusText:
        print(" " * (OFFSET_X - 10) + colorText.YELLOW + "- " + line + colorText.BLANK)
    print("\n")

    # --- Сохраняем финалы для магазина ---
    savedLoot1 = final1
    savedLoot2 = final2
    savedBombs1 = playerOneBombs
    savedWalls1 = playerOneWalls
    savedBombs2 = playerTwoBombs
    savedWalls2 = playerTwoWalls

    # --- Магазин покупок ---
    buying = True
    while buying:
        print("\033[2J\033[H", end="")
        print(" " * (OFFSET_X - 20) + "╔════════════════════╧═════════════════╧════════════════════╗\n")
        print(" " * (OFFSET_X + 10) + colorText.ORANGEL + "=== CASH SCREEN ===" + colorText.BLANK + "\n")
        print(" " * (OFFSET_X - 20) + colorText.ORANGE + f"Player Ⅰ: base {colorText.YELLOW}{base1}{colorText.ORANGE} → final {colorText.YELLOW}{final1}{colorText.BLANK}\n")
        print(" " * (OFFSET_X - 20) + colorText.ORANGE + f"Player Ⅱ: base {colorText.YELLOW}{base2}{colorText.ORANGE} → final {colorText.YELLOW}{final2}{colorText.BLANK}\n")
        print(" " * (OFFSET_X - 20) + "╚════════════════════╤═════════════════╤════════════════════╝\n")
        print(" " * (OFFSET_X - 15) + colorText.CYAN + "=== CONDITIONS APPLIED ===" + colorText.BLANK)
        for line in bonusText:
            print(" " * (OFFSET_X - 10) + colorText.YELLOW + "- " + line + colorText.BLANK)
        print("\n")
        print(" " * (OFFSET_X - 15) + colorText.CYAN + "=== SHOP ===" + colorText.BLANK)
        print(f"Player Ⅰ: Money: {savedLoot1} | Bombs: {savedBombs1} (Cost: 3) | Walls: {savedWalls1} (Cost: 2)")
        print(f"Player Ⅱ: Money: {savedLoot2} | Bombs: {savedBombs2} (Cost: 3) | Walls: {savedWalls2} (Cost: 2)")
        print("Press keys: 1 - Buy P1 Bomb, 2 - Buy P1 Wall, 3 - Buy P2 Bomb, 4 - Buy P2 Wall, 0 - Continue")
        
        key = msvcrt.getch().decode('latin-1').lower()
        
        if key == '1' and savedLoot1 >= 3:
            savedLoot1 -= 3
            savedBombs1 += 1
        elif key == '2' and savedLoot1 >= 2:
            savedLoot1 -= 2
            savedWalls1 += 1
        elif key == '3' and savedLoot2 >= 3:
            savedLoot2 -= 3
            savedBombs2 += 1
        elif key == '4' and savedLoot2 >= 2:
            savedLoot2 -= 2
            savedWalls2 += 1
        elif key == '0':
            buying = False
            levelIndex += 1
            if levelIndex == 2:
                boardSizeX, boardSizeY, playerOneX, playerOneY, playerTwoX, playerTwoY, wallsMap, loot, bigLoot, trap, mine, blink, box, cashout = createMap(mapSecondLayout)
                gameIsActive = True
            if levelIndex == 3:
                boardSizeX, boardSizeY, playerOneX, playerOneY, playerTwoX, playerTwoY, wallsMap, loot, bigLoot, trap, mine, blink, box, cashout = createMap(mapThirdLayout)
                gameIsActive = True
            elif levelIndex > 3:
                print("Конец игры!")
                time.sleep(2)
                sys.exit()

            
            gameIsActive = True
            drawGameUI()


    return savedLoot1, savedLoot2, savedBombs1, savedWalls1, savedBombs2, savedWalls2

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

playerOneBombs = 0
playerOneWalls = 0
playerTwoBombs = 0
playerTwoWalls = 0

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
    for item in playerInventory:
        if item == "$":
            playerLootCount += 1
        elif item == "₿":
            playerLootCount += 3

    for i in range(3):
        playerInventory[i] = None

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
    "█₡1               $█   ██$ *█",
    "█2    !                █*█$██*█ █",
    "█ █      - █  ₿-█$█",
    "█ $      █ █₿$*₿█ █",
    "███          $ ██████████!█",
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

mapThirdLayout = [
    "███████████████████",
    "█₡1              $█   ██$ *█",
    "█2               !  █*█$██*█ █",
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
os.system("") 
print("\033[2J", end="") 
print("\033[H", end="")


'''#============================================='''
#==================================================#

        #ЦИКЛ САМОЙ ИГРЫ, ДО ЭТОГО ПОДГОТОВКА

#==================================================#
'''#============================================='''

#if __name__ == '__main__': 
    #load_animation()
shopShown = False  # Флаг, чтобы магазин не вызывался повторно

while gameIsActive:  # Считай void Update()
    allDead = (playerOneX == -999 and playerTwoX == -999)

    # Проверка, нужно ли открывать магазин
    if (allDead or (playerOneCashedOut and playerTwoCashedOut)) and not shopShown:
        shopShown = True  # предотвращаем повторный вызов
        lootCount1, lootCount2, playerOneBombs, playerOneWalls, playerTwoBombs, playerTwoWalls = \
            drawCashScreen(
                lootCount1, lootCount2,
                playerOneDied, playerTwoDied,
                playerOneCashedOut, playerTwoCashedOut,
                cashoutOrder,
                playerOneBombs, playerOneWalls,
                playerTwoBombs, playerTwoWalls
            )

        # Если после магазина создаётся новая карта
        if levelIndex > 1:  # или условие перехода на следующую карту
            shopShown = False  # можно снова показывать магазин на новом уровне

    checkCashoutStanding()
    drawGameUI()

    keys = []
    if msvcrt.kbhit():
        keys.append(msvcrt.getch().decode('latin-1').lower())
        time.sleep(0.01)

        for inputKey in keys:
            # Игрок 1
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

            # Игрок 2
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
