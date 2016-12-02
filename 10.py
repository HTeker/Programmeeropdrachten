def geefHoevaak(lijst1, lijst2):
    lijst = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}

    for i in range(0, len(lijst1)):
        lijst[int(lijst1[i])] += 1

    for i in range(0, len(lijst2)):
        lijst[int(lijst2[i])] += 1

    return lijst

print(geefHoevaak([1,1,2,5,6,3,6,9,10], [2,5,7,9,4,1,0,6,0]))