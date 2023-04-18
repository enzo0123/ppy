import sys
import smtplib
from email.mime.text import MIMEText

mapa = {}

with open("data/students.txt") as file:
    for x in file:
        line = x.rstrip()
        if line.__len__() == 0:
            print("Plik jest pusty")
        else:
            arr = line.split(",")
            if arr.__len__()==4:
                mapa[arr[0]] = [arr[1], arr[2], arr[3]]
            else:
                mapa[arr[0]] = [arr[1], arr[2], arr[3],arr[4],arr[5]]
            print("Dodano studentow z pliku")


def score(points):
    if points < 51:
        return 2
    elif points < 61:
        return 3
    elif points < 71:
        return 3.5
    elif points < 81:
        return 4
    elif points < 91:
        return 4.5
    else:
        return 5


def addStudent():
    licznik = 0
    key = input("Podaj adres email studenta\n")
    for keys in mapa.keys():
        if keys.__eq__(key):
            licznik = licznik + 1
            print("Student z takim emailem juz istnieje")
    if licznik == 0:
        x = input("Podaj imie, nazwisko i punkty studenta oddzielone przecinkami" + "\n")
        values = x.split(",")
        mapa[key] = values
        print("Dodano studenta")


def removeStudent():
    key = input("Podaj email studenta ktorego chcesz usunac\n")
    x = mapa.pop(key)
    print("Usunieto studenta o danych " + str(x))


def insertRating():
    for key, list in mapa.items():
        if list.__len__() == 3:
            points = int(list.__getitem__(2))
            rating = score(points)
            list.append(rating)
            list.append("GRADED")


def sendEmail(userEmail, userPassword):
    userEmail = userEmail
    userPassword = userPassword
    subject = "Grade"

    lista = []
    for key, list in mapa.items():
        if list.__len__() > 3:
            if list[4].__eq__("GRADED"):
                lista.append(key)

    for email in lista:
        points = 0
        score = 0
        name = ""
        lastName = ""
        for key, values in mapa.items():
            if key.__eq__(email):
                name = values[0]
                lastName = values[1]
                points = values[2]
                score = values[3]

        message = "Witaj " + name + " " + lastName + " z cwiczen otrzymales liczbe " + str(points) + " punktow co przeklada sie na ocene " + str(score)

        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = userEmail
        msg['To'] = email
        msg.attach(msg)

        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.login(userEmail, userPassword)
        smtp_server.sendmail(userEmail, email, msg.as_string())
        smtp_server.quit()


running = True

while running:
    print("1. Dodaj studenta\n" +
          "2. Usun studenta\n" +
          "3. Wystaw oceny\n" +
          "4. Wyswietl liste studentow\n" +
          "5. Wyslij email\n" +
          "6. Zakoncz program")
    x = input("Jaka czynnosc chcesz wykonac\n")
    if x.__eq__("1"):
        addStudent()
    elif x.__eq__("2"):
        removeStudent()
    elif x.__eq__("3"):
        insertRating()
    elif x.__eq__("4"):
        print(mapa)
    elif x.__eq__("5"):
        sendEmail("x", "y")
    elif x.__eq__("6"):
        running = False

    with open("data/students.txt", "w") as file:
        fileMessage = ""
        for key,list in mapa.items():
            message = key
            for value in list:
                message = message + "," + str(value)
            message = message + "\n"
            fileMessage = fileMessage + message
        file.write(fileMessage)


