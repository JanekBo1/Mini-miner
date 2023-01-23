import random
punkty = 0



while True :

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

    for g in range(7):
        gem = random.randint(2, 28)
        if (gem % 2) == 0:
            maxg = maxg + 1
            mapa_1[random.randint(6, 10)][gem] = "O"



        



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
        
        elif mapa_1[x][y] == "X":
            return "kamień2"

        elif mapa_1[x][y] == "O":
            return "punkt"

        else:
            return "niedozwolony"






    plansza()


    while win == False:

        ruch = input()

        if ruch == "w":
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
            walidacja = walidacja_ruchu(x+1, y, mapa_1)
            if walidacja == "dozwolony":
                mapa_1[x][y] = " "
                x = x + 1
                mapa_1[x][y] = "I"

            elif walidacja == "kamień":
                mapa_1[x+1][y] = "X"

            elif walidacja == "kamień2":
                mapa_1[x+1][y] = " "

            elif walidacja == "punkt":
                mapa_1[x+1][y] = " "
                punkty = punkty + 1
                puk = puk + 1

        if ruch == "a":

            walidacja = walidacja_ruchu(x, y-2, mapa_1)
            if walidacja == "dozwolony":

                mapa_1[x][y] = " "
                y = y - 2
                if mapa_1[x+1][y] == " ":
                    x = x + 1 

                mapa_1[x][y] = "I"
            elif walidacja == "kamień":
                mapa_1[x][y-2] = "X"
            elif walidacja == "kamień2":
                mapa_1[x][y-2] = " "

            elif walidacja == "punkt":
                mapa_1[x][y-2] = " "
                punkty = punkty + 1
                puk = puk + 1


            

        if ruch == "d":
            walidacja = walidacja_ruchu(x, y+2, mapa_1)
            if walidacja == "dozwolony":

                mapa_1[x][y] = " "
                y = y + 2
                if mapa_1[x+1][y] == " ":
                    x = x + 1 

                mapa_1[x][y] = "I"
            elif walidacja == "kamień":
                mapa_1[x][y+2] = "X"
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

