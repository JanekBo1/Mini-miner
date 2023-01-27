import random
punkty = 0
die = False


while die == False :

    mapa_1 = [
        ["+","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","+"],
        ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
        ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
        ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
        ["|"," "," "," "," "," "," "," "," "," "," "," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","|"],
        ["|"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","|"],
        ["|"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","|"],
        ["|"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","|"],
        ["|"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","|"],
        ["|"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","|"],
        ["|"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","■"," ","|"],
        ["+","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","+"]
    ]

    maxg = 0
    puk = 0

    x = 4
    y = 8
    mapa_1[x][y] = "I"

    win = False

    cave = False

    while cave == False:
        l = random.randint(2,22)
        if (l % 2) == 0:
            cave = True
            if random.randint(1,2) == 1:
                mapa_1[8][l] = "X"
                mapa_1[8][l+2] = "X"
                mapa_1[8][l+4] = "X"
                mapa_1[8][l+6] = "X"
                mapa_1[9][l+2] = "X"
                mapa_1[9][l+4] = "X"   
                mapa_1[7][l] = " "
                mapa_1[7][l+2] = " "
                mapa_1[7][l+4] = " "
                mapa_1[7][l+6] = " "
            else:
                mapa_1[8][l] = "X"
                mapa_1[8][l+2] = "X"
                mapa_1[8][l+4] = "X"
                mapa_1[8][l+6] = "X"
                mapa_1[9][l+2] = "X"
                mapa_1[9][l+4] = "X"  


    for g in range(10):
        gem = random.randint(2, 28)
        if (gem % 2) == 0:
            gem2 = random.randint(6, 10)
            if not mapa_1[gem2][gem] == "X":
                maxg = maxg + 1
                mapa_1[gem2][gem] = "O"



    def plansza():
        print("points:", punkty)

        for i in range(len(mapa_1)):
            print("")
            for j in range(len(mapa_1[0])):
                print(mapa_1[i][j], end="")
        print("\n")


    def walidacja_ruchu(x, y, mapa_1):
        if mapa_1[x][y] == " ":
            return "dozwolony"
        
        elif mapa_1[x][y] == "■":
            return "kamień"
        
        elif mapa_1[x][y] == "□":
            return "kamień2"

        elif mapa_1[x][y] == "O":
            return "punkt"
        

        else:
            return "niedozwolony"


    def smierd(x, y, mapa_1):
        if mapa_1[x+1][y] == "X":
            return "die"



    plansza()


    while win == False:

        ruch = input()

        if ruch == "w":
            smierdd = smierd(x,y,mapa_1)
            if smierdd == "die":
                print("you died")
                die = True
                win = True
            else:
                walidacja = walidacja_ruchu(x-1, y, mapa_1)
                if walidacja == "dozwolony":
                    mapa_1[x][y] = " "
                    x = x - 1
                    mapa_1[x][y] = "I"
                elif walidacja == "punkt":
                    mapa_1[x-1][y] = " "
                    punkty = punkty + 1
                    puk = puk + 1

        if ruch == "s":
            smierdd = smierd(x,y,mapa_1)
            if smierdd == "die":
                print("you died")
                die = True
                win = True
            else:                
                walidacja = walidacja_ruchu(x+1, y, mapa_1)
                if walidacja == "dozwolony":
                    mapa_1[x][y] = " "
                    x = x + 1
                    mapa_1[x][y] = "I"

                elif walidacja == "kamień":
                    mapa_1[x+1][y] = "□"

                elif walidacja == "kamień2":
                    mapa_1[x+1][y] = " "

                elif walidacja == "punkt":
                    mapa_1[x+1][y] = " "
                    punkty = punkty + 1
                    puk = puk + 1

        if ruch == "a":
            smierdd = smierd(x,y,mapa_1)
            if smierdd == "die":
                print("you died")
                die = True
                win = True
            else:
                walidacja = walidacja_ruchu(x, y-2, mapa_1)
                if walidacja == "dozwolony":

                    mapa_1[x][y] = " "
                    y = y - 2
                    if mapa_1[x+1][y] == " ":
                        x = x + 1 

                    mapa_1[x][y] = "I"
                elif walidacja == "kamień":
                    mapa_1[x][y-2] = "□"
                elif walidacja == "kamień2":
                    mapa_1[x][y-2] = " "

                elif walidacja == "punkt":
                    mapa_1[x][y-2] = " "
                    punkty = punkty + 1
                    puk = puk + 1


            

        if ruch == "d":
            smierdd = smierd(x,y,mapa_1)
            if smierdd == "die":
                print("you died")
                die = True
                win = True
            else:                
                walidacja = walidacja_ruchu(x, y+2, mapa_1)
                if walidacja == "dozwolony":

                    mapa_1[x][y] = " "
                    y = y + 2
                    if mapa_1[x+1][y] == " ":
                        x = x + 1 

                    mapa_1[x][y] = "I"
                elif walidacja == "kamień":
                    mapa_1[x][y+2] = "□"
                elif walidacja == "kamień2":
                    mapa_1[x][y+2] = " "

                elif walidacja == "punkt":
                    mapa_1[x][y+2] = " "
                    punkty = punkty + 1
                    puk = puk + 1

        plansza()

        if maxg == puk:
            print("you win")
            win = True

