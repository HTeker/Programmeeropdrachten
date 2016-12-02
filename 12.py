def printMatrix(cells):
    for i in range(0, len(cells)):
        row = ""
        for x in range(0, len(cells[i])):
            row += "["

            if(cells[i][x] == 0):
                row += " "
            elif(cells[i][x] == 1):
                row += "X"
            else:
                row += "O"

            row += "]"

        print(row)

def askUserInput(user):
    selectedEmpty = False

    while(selectedEmpty == False):
        x = int(input("Speler " + str(user) + ": voer de X-waarde in voor je volgende zet: "))
        y = int(input("Speler " + str(user) + ": voer de Y-waarde in voor je volgende zet: "))

        if((1 <= x <= (len(cells[0]))) and (1 <= y <= (len(cells[0])))):
            x -= 1
            y -= 1

            if (cells[x][y] == 0):
                selectedEmpty = True
                cells[x][y] = user
            else:
                print("U heeft geen lege veld geselecteerd.")
        else:
            print("U heeft een ongeldige invoer gegeven")

def checkGameNotOver():
    for i in range(0, len(cells)):
        for x in range(0, len(cells[i])):
            if(cells[i][x] == 0):
                return True

    return False

cells = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
lastPlayer = 2

while(checkGameNotOver()):
    printMatrix(cells)

    if (lastPlayer == 1):
        user = 2
    else:
        user = 1
    lastPlayer = user

    askUserInput(user)

print("Spel is voorbij.")
printMatrix(cells)