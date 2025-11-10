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


#ЦВЕТА ДЛЯ ТЕКСТА
class colorsText:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLANK = '\033[0m' 
    BLACK = '\033[30m'
    GRAY = '\033[37m'
    
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
if __name__ == '__main__': 
    load_animation()



# BREAKPOINT
'''
ЭТО НЕ УЧЕБНАЯ ТРЕВОГА. 
'''
# DANGER, DANGER




'''#============================================='''
        #ВСЕ ПРО UI
'''#============================================='''



OFFSET_X = 5  # количество пробелов слева
OFFSET_Y = 2  # количество пустых строк сверху



'''#============================================='''
        #КАРТА (МОЖНО РИСОВАТЬ РУКАМИ)
'''#============================================='''

''' Легенда:
' ' (пробел) — пустая клетка
'█' — стена
'1' — игрок 1
'2' — игрок 2 '''

#ПЕРВАЯ КАРТА
mapFirstLayout = [
    "███████",
    "█     █",
    "█     █",
    "█ 1 2 █",
    "█     █",
    "█     █",
    "███████",
]

#СОЗДАНИЕ КАРТЫ
def createMap(mapLayout):
    boardSizeY = len(mapLayout)
    boardSizeX = max(len(row) for row in mapLayout)

    #Великолепный код, слава enumerate, слава кортежам о7 о7 о7
    wallsMap = []
    playerOne_x = playerOne_y = None
    playerTwo_x = playerTwo_y = None

    for y, row in enumerate(mapLayout):
        for x, cell in enumerate(row):  
            if cell == '█':
                wallsMap.append((x, y))
            elif cell == '1':
                playerOne_x, playerOne_y = x, y
            elif cell == '2':
                playerTwo_x, playerTwo_y = x, y

    if playerOne_x is None:
        playerOne_x, playerOne_y = 1, 1
    if playerTwo_x is None:
        playerTwo_x, playerTwo_y = 3, 1

    return boardSizeX, boardSizeY, wallsMap, playerOne_x, playerOne_y, playerTwo_x, playerTwo_y

#Обязательное первое уточнение, в процессе буду менять только mapFirstLayout на mapSecondLayout и mapThirdLayout
boardSizeX, boardSizeY, wallsMap, playerOne_x, playerOne_y, playerTwo_x, playerTwo_y = createMap(mapFirstLayout)



'''#============================================='''
                  #МЕЛКИЕ ФУНКЦИИ
'''#============================================='''


#Может ли двигаться в клетку
def can_move(x, y):    
    return (x, y) not in wallsMap and 0 <= x < boardSizeX and 0 <= y < boardSizeY


#РИСУЕТ ПОЛЕ
def drawField(posPlayerOneX, posPlayerOneY, posPlayerTwoX, posPlayerTwoY):
    sys.stdout.write("\033[H")

    # вертикальный сдвиг
    for _ in range(OFFSET_Y):
        print()

    for y in range(boardSizeY):
        cubeInside = " " * OFFSET_X  # горизонтальный сдвиг
        for x in range(boardSizeX):

            if (x, y) in wallsMap:
                cubeInside += colorsText.GRAY + "███" + colorsText.BLANK

            elif x == posPlayerOneX and y == posPlayerOneY and x == posPlayerTwoX and y == posPlayerTwoY:
                cubeInside += colorsText.CYAN+ "[3]" + colorsText.BLANK

            elif x == posPlayerOneX and y == posPlayerOneY:
                cubeInside += colorsText.BLUE + "[1]" + colorsText.BLANK

            elif x == posPlayerTwoX and y == posPlayerTwoY:
                cubeInside += colorsText.GREEN + "[2]" + colorsText.BLANK

            else:
                cubeInside += "[ ]"
        print(cubeInside)
    sys.stdout.flush()


#ЧИСТИТ КОНСОЛЬ + ПО МЕЛОЧИ
os.system("") 
print("\033[2J", end="") 
print("\033[H", end="") 




'''#============================================='''
#==================================================#

        #ЦИКЛ САМОЙ ИГРЫ, ДО ЭТОГО ПОДГОТОВКА

#==================================================#
'''#============================================='''
  

while True: #Считай void Update()


    drawField(playerOne_x, playerOne_y, playerTwo_x, playerTwo_y)



    if msvcrt.kbhit():
        inputKey = msvcrt.getch().decode('latin-1').lower()

        '''
        ВСЕ ЧТО СВЯЗЯННО С ПЕРЕДВИЖЕНИЕМ
        '''

        #ИНПУТЫ


        #ИГРОК 1

        
        if inputKey == 'w' and playerOne_y > 0 and can_move(playerOne_x, playerOne_y-1):
            playerOne_y -= 1
            time.sleep(0.05)
        elif inputKey == 's' and playerOne_y < boardSizeY - 1 and can_move(playerOne_x, playerOne_y+1):
            playerOne_y += 1
            time.sleep(0.05)
        elif inputKey == 'a' and playerOne_x > 0 and can_move(playerOne_x-1, playerOne_y):
            playerOne_x -= 1
            time.sleep(0.05)
        elif inputKey == 'd' and playerOne_x < boardSizeX - 1 and can_move(playerOne_x+1, playerOne_y):
            playerOne_x += 1
            time.sleep(0.05)

        #ИГРОК 2
        if inputKey == 'y' and playerTwo_y > 0 and can_move(playerTwo_x, playerTwo_y-1):
            playerTwo_y -= 1
            time.sleep(0.05)
        elif inputKey == 'h' and playerTwo_y < boardSizeY - 1 and can_move(playerTwo_x, playerTwo_y+1):
            playerTwo_y += 1
            time.sleep(0.05)
        elif inputKey == 'g' and playerTwo_x > 0 and can_move(playerTwo_x-1, playerTwo_y):
            playerTwo_x -= 1
            time.sleep(0.05)
        elif inputKey == 'j' and playerTwo_x < boardSizeX - 1 and can_move(playerTwo_x+1, playerTwo_y):
            playerTwo_x += 1
            time.sleep(0.05)

        
