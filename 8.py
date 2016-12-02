def printLijst(lijst):
    som = 0
    product = 1
    midden = 0

    for i in range(0, len(lijst)):
        som += lijst[i]
        product *= lijst[i]

    gemiddelde = som / len(lijst)

    if(len(lijst) % 2 == 0):
        midden = int((lijst[int(len(lijst) / 2)] + lijst[int(len(lijst) / 2 - 1)]) / 2)
    else:
        midden = lijst[int(len(lijst) / 2)]

    print("Som: " + str(som))
    print("Product: " + str(product))
    print("Gemiddelde: " + str(gemiddelde))
    print("Midden: " + str(midden))

printLijst([4,6,34,3,23,1234,2, 4])