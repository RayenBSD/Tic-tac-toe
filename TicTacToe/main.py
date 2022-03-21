import pygame as pg
import time as tm
import os

pg.init()
screenX, screenY = 420, 420
screen = pg.display.set_mode((screenX, screenY))
pg.display.set_caption("Tic Tac Toe")
icon = pg.image.load(os.path.join("images", "xo.png"))
pg.display.set_icon(icon)

counter = 0
char, pos = [], []

xo = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

winner = [['a', 'b', 'c'],
          ['d', 'f', 'j'],
          ['h', 'k', 'l']]

xoPos = [[(20, 20), (160, 20), (300, 20)],
         [(20, 160), (160, 160), (300, 160)],
         [(20, 290), (160, 290), (300, 290)]]

def restart():
    global xo, winner, char, pos, counter
    counter = 0
    xo = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

    winner = [['a', 'b', 'c'],
              ['d', 'f', 'j'],
              ['h', 'k', 'l']]
    char.clear()
    pos.clear()
    tm.sleep(1)
    menu()

def Oappend():
    global char
    char.append(pg.transform.scale(pg.image.load(
        os.path.join("images", "O.jpg")
    ), (100, 100)))

def Xappend():
    global char
    char.append(pg.transform.scale(pg.image.load(
        os.path.join("images", "X.png")
    ), (100, 100)))

def jPressed():
    global winner, xo, pos, counter
    x, y = pg.mouse.get_pos()
    if (0 < x < 140 and 0 < y < 140) and xo[0][0]:
        counter += 1
        Oappend()
        pos.append(xoPos[0][0])
        winner[0][0] = 'O'
        xo[0][0] = 0
    elif (140 < x < 280 and 0 < y < 140) and xo[0][1]:
        counter += 1
        Oappend()
        pos.append(xoPos[0][1])
        winner[0][1] = 'O'
        xo[0][1] = 0
    elif (280 < x < 420 and 0 < y < 140) and xo[0][2]:
        counter += 1
        Oappend()
        pos.append(xoPos[0][2])
        winner[0][2] = 'O'
        xo[0][2] = 0
    elif (0 < x < 140 and 140 < y < 280) and xo[1][0]:
        counter += 1
        Oappend()
        pos.append(xoPos[1][0])
        winner[1][0] = 'O'
        xo[1][0] = 0
    elif (140 < x < 280 and 140 < y < 280) and xo[1][1]:
        counter += 1
        Oappend()
        pos.append(xoPos[1][1])
        winner[1][1] = 'O'
        xo[1][1] = 0
    elif (280 < x < 420 and 140 < y < 280) and xo[1][2]:
        counter += 1
        Oappend()
        pos.append(xoPos[1][2])
        winner[1][2] = 'O'
        xo[1][2] = 0
    elif (0 < x < 140 and 280 < y < 420) and xo[2][0]:
        counter += 1
        Oappend()
        pos.append(xoPos[2][0])
        winner[2][0] = 'O'
        xo[2][0] = 0
    elif (140 < x < 280 and 280 < y < 420) and xo[2][1]:
        counter += 1
        Oappend()
        pos.append(xoPos[2][1])
        winner[2][1] = 'O'
        xo[2][1] = 0
    elif (280 < x < 420 and 280 < y < 420) and xo[2][2]:
        counter += 1
        Oappend()
        pos.append(xoPos[2][2])
        winner[2][2] = 'O'
        xo[2][2] = 0

def fPressed():
    global winner, xo, pos, counter
    x, y = pg.mouse.get_pos()
    if (0 < x < 140 and 0 < y < 140) and xo[0][0]:
        counter += 1
        Xappend()
        pos.append(xoPos[0][0])
        winner[0][0] = 'X'
        xo[0][0] = 0
    elif (140 < x < 280 and 0 < y < 140) and xo[0][1]:
        counter += 1
        Xappend()
        pos.append(xoPos[0][1])
        winner[0][1] = 'X'
        xo[0][1] = 0
    elif (280 < x < 420 and 0 < y < 140) and xo[0][2]:
        counter += 1
        Xappend()
        pos.append(xoPos[0][2])
        winner[0][2] = 'X'
        xo[0][2] = 0
    elif (0 < x < 140 and 140 < y < 280) and xo[1][0]:
        counter += 1
        Xappend()
        pos.append(xoPos[1][0])
        winner[1][0] = 'X'
        xo[1][0] = 0
    elif (140 < x < 280 and 140 < y < 280) and xo[1][1]:
        counter += 1
        Xappend()
        pos.append(xoPos[1][1])
        winner[1][1] = 'X'
        xo[1][1] = 0
    elif (280 < x < 420 and 140 < y < 280) and xo[1][2]:
        counter += 1
        Xappend()
        pos.append(xoPos[1][2])
        winner[1][2] = 'X'
        xo[1][2] = 0
    elif (0 < x < 140 and 280 < y < 420) and xo[2][0]:
        counter += 1
        Xappend()
        pos.append(xoPos[2][0])
        winner[2][0] = 'X'
        xo[2][0] = 0
    elif (140 < x < 280 and 280 < y < 420) and xo[2][1]:
        counter += 1
        Xappend()
        pos.append(xoPos[2][1])
        winner[2][1] = 'X'
        xo[2][1] = 0
    elif (280 < x < 420 and 280 < y < 420) and xo[2][2]:
        counter += 1
        Xappend()
        pos.append(xoPos[2][2])
        winner[2][2] = 'X'
        xo[2][2] = 0

def checkWinner():
    global winner, xo

    for i in range(0, 3):
        if (winner[i][0] == winner[i][1] == winner[i][2]):
            restart()
    for i in range(0, 3):
        if (winner[0][i] == winner[1][i] == winner[2][i]):
            restart()
    if winner[0][0] == winner [1][1] == winner[2][2]:
        restart()
    if winner[0][2] == winner [1][1] == winner[2][0]:
        restart()

    sum = 0
    for i in range(0, 3):
        for j in range(0, 3):
            sum += xo[i][j]
    if sum == 0:
        restart()

def redraw():
    global screen, char, pos, xo, counter

    board = pg.image.load(os.path.join("images", "tictactoe board.png"))
    screen.blit(board, (0, 0))

    if counter % 2 == 0:
        if pg.key.get_pressed()[pg.K_f]:
            fPressed()
    else:
        if pg.key.get_pressed()[pg.K_j]:
            jPressed()

    if (len(char) != 0 and len(pos) != 0):
        for i in range(len(char)):
            screen.blit(char[i], pos[i])

def main():
    while True:
        pg.time.delay(50)
        for events in pg.event.get():
            if events.type == pg.QUIT:
                quit()
        checkWinner()
        redraw()
        pg.display.update()

def menu():
    while True:
        global screen, screenY, screenY

        background = pg.transform.scale(pg.image.load(os.path.join("images", "Black.jpg")), (480, 480))
        screen.blit(background, (0, 0))

        menufont = pg.font.SysFont("arial", 36, True, (255, 255, 255)).render("Press Space to begin!", True, (255, 255, 255))
        Xfont = pg.font.SysFont("arial", 36, True, (255, 255, 255)).render("j => \'O\'", True,(255, 255, 255))
        Ofont = pg.font.SysFont("arial", 36, True, (255, 255, 255)).render("f => \'X\'", True,(255, 255, 255))

        pg.time.delay(50)

        screen.blit(menufont, (screenX - menufont.get_width() - 30, screenY/2.5))
        screen.blit(Xfont, (screenX - menufont.get_width() - 30, screenY / 1.7))
        screen.blit(Ofont, (screenX - menufont.get_width() - 30, screenY / 2))

        for events in pg.event.get():
            if events.type == pg.QUIT:
                quit()
            if pg.key.get_pressed()[pg.K_SPACE]:
                main()
        pg.display.update()

if __name__ == '__main__':
    menu()