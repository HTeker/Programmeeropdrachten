def setName(list, name):
    list['name'] = name

def setSurname(list, surname):
    list['surname'] = surname

def setClass(list, sclass):
    list['class'] = sclass


students = {}

while(True):
    snr = input("Voer een studentnummer in om de gegevens van de leerling te wijzigen: ")

    if(snr == 'exit'):
        break
    else:
        if snr not in students:
            students[snr] = {
                'name': '',
                'surname': '',
                'class': ''
            }
            print('Student bestond niet, er is een aangemaakt')
        while(True):
            opt = input("Wilt u de naam [n], achternaam [s] of klas [c] van " + students[snr]['name'] + " veranderen?")

            if(opt == 'n'):
                name = input("Voer een naam in: ")
                setName(students[snr], name)
                break
            if(opt == 's'):
                surname = input("Voer een achternaam in: ")
                setSurname(students[snr], surname)
                break
            if(opt == 'c'):
                sclass = input("Voer een klas in: ")
                setClass(students[snr], sclass)
                break
            else:
                print("U heeft geen geldige invoer gedaan.")