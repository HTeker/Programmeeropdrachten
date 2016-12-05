# Student: naam, vakcode, cijfer
# 2d list

def askUserInput(msg):
    global invoer
    invoer = input(msg);
    return invoer

invoer = ""
cijfers = []

while(invoer != "stop"):
    try:
        cijfer = int(askUserInput("Voer een cijfer in: "))
    except ValueError:
        print("U heeft geen cijfer ingevoerd.")

    cijfers.append(cijfer)

vakcode = askUserInput("Voer een vakcode in: ")

cijfersMetVakcode = {vakcode: {}}
totaal = 0

for i in range(0, len(cijfers)):
    cijfersMetVakcode[vakcode][i] = cijfers[i]
    totaal += cijfers[i]

print("Gemiddelde is: " + str(totaal/len(cijfers)))