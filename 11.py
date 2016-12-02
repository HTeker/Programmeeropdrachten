def vermenigdvuldigLijsten(lijst1, lijst2):
    lijst = {}

    if(len(lijst1) == len(lijst2)):
        for i in range(0, len(lijst1)):
            lijst[i] = int(lijst1[i])

        for i in range(0, len(lijst2)):
            lijst[i] *= int(lijst2[i])
    else:
        lijst = "Geef twee lijsten met dezelfde lengte."

    return lijst

print(vermenigdvuldigLijsten([123,234,6,12,56,12], [123, 34, 12, 423, 53425, 65]))