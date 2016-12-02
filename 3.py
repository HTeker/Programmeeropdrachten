def geefGrootste(a, b, c):
    if(a > b and a > c):
        return(a)
    elif(b > a and b > c):
        return(b)
    else:
        return(c)

print(geefGrootste(23, 2345, 12) * 2)
print(geefGrootste(23, 2345, 12) * 3)
