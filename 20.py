def transform(list, f):
    newList =[]

    for x in list:
        newList.append(f(x))

    return newList

list = [
    {
        "naam" : "Halil Teker",
        "woonplaats" : "Den Haag",
        "leeftijd" : 22
    },
    {
        "naam" : "Faouzi",
        "woonplaats" : "Diemen",
        "leeftijd" : 24
    },
    {
        "naam" : "Matthijs",
        "woonplaats" : "Amsterdam",
        "leeftijd" : 23
    },
    {
        "naam" : "Anthony",
        "woonplaats" : "Rotterdam",
        "leeftijd" : 20
    }]

transform(list, lambda x: x["woonplaats"])