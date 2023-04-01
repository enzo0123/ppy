imie = input("Podaj swoje imie i nazwisko : ")


pulapytan = {"1. Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie": [
    "A. ogladanie telewizji/filmow/seriali",
    "B. czytanie książek/czasopism",
    "C. słuchanie muzyki",
    "D. spotkania z rodziną/przyjaciółmi"
], "2. W jakich okolicznościach czytasz książki najczęściej?": [
    "A. podczas podróży",
    "B. w czasie wolnym (po pracy, na urlopie)",
    "C. podczas pracy/nauki (to ich element)",
    "D. w ogóle nie czytam"
],
    "3. Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?": [
        "A. czytanie mnie relaksuje/odpręża",
        "B. odczuwam presję rodziny/środowiska, żeby czytać",
        "C. czytanie to moje hobby",
        "D. inny, jaki?"
    ],
    "4. Po książki w jakiej formie sięgasz najczęściej?": [
        "A. papierowej (tradycyjnej)",
        "B. e-booki (książki elektroniczne) na komputerze",
        "C. e-booki na tablecie/telefonie",
        "D. e-booki na specjalnym czytniku (np. Kindle)"
    ],
    "5. Ile książek czytasz średnio w ciągu roku?": [
        "A. 0",
        "B. 1-5",
        "C. 5-10",
        "D. powyzej 10"
    ],
    "6. Jak często średnio czytasz książki?": [
        "A. codziennie",
        "B. raz w tygodniu",
        "C. raz na kilka miesięcy",
        "D. wcale"
    ],
    "7. Po jakie gatunki książek sięgasz najczęściej?": [
        "A. naukowe",
        "B. romanse",
        "C. podróżnicze",
        "D. inne, jakie?"
    ]}

licznik=0
list=[]
listaWynikowa=[]

for klucz, lista in pulapytan.items():
    print(klucz)
    licznik=licznik+1
    for element in lista:
        print(element)
    odp = input("Podaj odpowiedz : ")
    if odp.__contains__("D") and (licznik==3 or licznik==7):
        odp=input("Odpowiedz : ")
    list.append(odp)

licznik=0

for klucz, lista in pulapytan.items():
    if list.__getitem__(licznik).__len__()==1 :
        for element in lista :
            if element.__contains__(list.__getitem__(licznik)) :
                listaWynikowa.append(element)
    else :
        listaWynikowa.append("D. " + list.__getitem__(licznik))
    licznik=licznik+1

licznik=0

print("Dziekujemy " + imie + " za wypelnienie ankiety, oto twoje odpowiedzi " + "\n")
for klucz in pulapytan.keys() :
    print("Pytanie " + klucz)
    print("Odpowiedz " + listaWynikowa.__getitem__(licznik) + "\n")
    licznik=licznik+1