def metoda(floorWidth, floorLength, panelWidth, panelLength, number):
    licznik = 1
    floorSize = floorWidth * floorLength * 1.1
    panelsSize = panelWidth * panelLength * number
    while floorSize > panelsSize:
        floorSize = floorSize - panelsSize
        licznik = licznik + 1
    return licznik

print(metoda(10, 12, 5, 2, 5))
