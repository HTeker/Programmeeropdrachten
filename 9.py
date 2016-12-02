def geefGrootsteGetal(lijst):
    grootste = 0

    for i in range(0, len(lijst)):
        if(lijst[i] > grootste):
            grootste = lijst[i]

    return grootste

print(geefGrootsteGetal([23423,24,12,2,34,3425,1234,241300]))