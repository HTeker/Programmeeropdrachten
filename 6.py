def printen(x, y):
    if(x <= y):
        print(x)
        printen(x + 1, y)
    else:
        return

printen(2, 8)