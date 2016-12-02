invoer = ""
woorden = []

while(invoer.lower() != "stop"):
    invoer = input("Voer een woord in: ")
    woorden.append(invoer)

for i in range(0, len(woorden)):
    print(woorden[len(woorden) - i - 1])