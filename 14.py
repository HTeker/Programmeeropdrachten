class CijferCollector:
    vakcode = ""
    cijfers = []

    def __init__(self, vakcode, cijfers):
        self.vakcode = vakcode
        self.cijfers = cijfers

    def eindcijfer(self):
        totaal = 0

        for i in range(0, len(self.cijfers)):
            totaal += self.cijfers[i]

        return round(totaal/len(self.cijfers))

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
cijferCollector = CijferCollector(vakcode, cijfers)

print("Gemiddelde is: " + str(cijferCollector.eindcijfer()))