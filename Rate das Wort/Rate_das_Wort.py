wort = input("Bitte gib dein Wort ein: ")
print("Das Wort hat", len(wort), "Buchstaben!")
x = 9
while x > 0:
    print("Du hast noch", x, "Versuch(e) übrig!")
    x -= 1
    versuch = input("Rate einen Buchstaben oder gib das gesamte Wort ein: ")
    if versuch == wort:
        print("Glückwunsch! Du hast das Wort richtig geraten")
        break
    elif versuch in wort:
        print("Der Buchstabe", versuch, "befindet sich an folgenden Positionen:")
        for i in range(len(wort)):
            if versuch == wort[i]:
                print(i+1)
    else:
        print("Falsch")
    if x == 0:
        print("Du hast das Spiel verloren")
        break
