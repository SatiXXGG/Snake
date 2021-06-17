import readchar
import os
import random

POS_Y = 1
POS_X = 1

Pos = [0, 0]

Pos[0] = POS_X
Pos[1] = POS_Y

MAP_WIDTH = 20
MAP_HEIGHT = 20

NumeroDeObjetos = 10
ObjetosDelMapa = []

tailsize = 0
tailpos = []
while len(ObjetosDelMapa) < NumeroDeObjetos:
    RandomPos = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]

    if not RandomPos in ObjetosDelMapa and RandomPos != Pos:
        ObjetosDelMapa.append(RandomPos)

while True:
    print("+" + "-" * (MAP_WIDTH * 3) + "+")
    for PosY in range(MAP_HEIGHT):
        print("!", end="")
        ObjectInCell = None
        for PosX in range(MAP_WIDTH):
            CharToDraw = " "
            for Object in ObjetosDelMapa:
                if Object[0] == PosX and Object[1] == PosY:
                    CharToDraw = "*"
                    ObjectInCell = Object

            for ColaPos in tailpos:
                if ColaPos[0] == PosX and ColaPos[1] == PosY:
                    CharToDraw = "."

            if PosX == Pos[0] and PosY == Pos[1]:
                CharToDraw = "@"

                if ObjectInCell:
                    ObjetosDelMapa.remove(ObjectInCell)
                    tailsize += 1

            print(" {} ".format(CharToDraw), end="")
        print("!")

    print("+" + "-" * (MAP_WIDTH * 3) + "+")

    TeclaPresionada = readchar.readchar().decode()

    if TeclaPresionada == "w":
        tailpos.insert(0, Pos.copy())
        tailpos = tailpos[:tailsize]
        Pos[1] -= 1
        Pos[1] %= MAP_HEIGHT
    elif TeclaPresionada == "a":
        tailpos.insert(0, Pos.copy())
        tailpos = tailpos[:tailsize]
        Pos[0] -= 1
        Pos[0] %= MAP_WIDTH
    elif TeclaPresionada == "s":
        tailpos.insert(0, Pos.copy())
        tailpos = tailpos[:tailsize]
        Pos[1] += 1
        Pos[1] %= MAP_HEIGHT

    elif TeclaPresionada == "d":
        tailpos.insert(0, Pos.copy())
        tailpos = tailpos[:tailsize]
        Pos[0] += 1
        Pos[0] %= MAP_WIDTH

    print(Pos)
    os.system("cls")
