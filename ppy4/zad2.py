def metoda(list):
    for number in list:
        licznik = 0
        for i in range(1, number+1):
            if number % i == 0:
                licznik = licznik + 1
        if licznik <= 2 and number > 1:
            print("Liczba " + str(number) + " jest liczba pierwsza")


metoda([2, 5, 6, 7,11,13,25,8, 4 , 1, 78, 91, 53])
