def macht3(getal):
    return getal*getal*getal

def faculteit(getal):
    waarde = 1
    
    for i in range(1, getal + 1):
        waarde *= i
        
    return waarde
    
def formule(x, y, z):
    return (macht3(x) * macht3(y) * macht3(z) + faculteit(x)) / faculteit(y)

print(formule(2, 4, 5))
