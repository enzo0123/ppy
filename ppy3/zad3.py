import getpass
import math
import random

list=["p","k","n"]
myList=[]
botList=[]
myScore=0
draw=0
botScore=0
a=""

print("Papier Kamien Nozyce")
x=int(input("Ile rund chcesz rozegrac : "))
y=input("W jakim trybie chcesz zagrac " + "\n" +
        "Wybierz 1, jesli chcesz zagrac z komputerem " + "\n" +
        "Wybierz 2, jesli chcesz zagrac z 2 osoba" + "\n")

if y.__contains__("1"):
    a=input("Wybierz swoja nazwe : ")
    print("W kazdym ruchu wybierz jedna z trzech dostepnym opcji " + "\n" +
          "p-papier    k-kamien    n-nozyce")
    d="Bot"
    for i in range(0,x):
        b=input("wybor : ")
        c=list[random.randint(0,len(list))-1]
        myList.append(b)
        botList.append(c)
        print("wybor bota : " + c)
else:
    a=input("Wybierz swoja nazwe : ")
    d=input("Wybierz swoja nazwe : ")
    print("W kazdym ruchu wybierz jedna z trzech dostepnym opcji " + "\n" +
            "p-papier    k-kamien    n-nozyce")
    for i in range(0,x):
        b=getpass.getpass(a + " wybiera : ")
        c=getpass.getpass(d + " wybiera : ")
        myList.append(b)
        botList.append(c)



print()

for i in range(0,len(myList)):
    print(myList[i] + "\t" + botList[i])
    if (myList[i]=="p" and botList[i]=="k") or (myList[i]=="k" and botList[i]=="n") or (myList[i]=="n" and botList[i]=="p"):
        myScore=myScore+1
    elif myList[i]==botList[i]:
        draw=draw+1

botScore=x-myScore-draw
if botScore>myScore:
    print(d + " wygral z " + a + " wynikiem " + botScore.__str__() + ":" + myScore.__str__())
elif botScore==myScore:
    print("Mecz zakonczyl sie remisem " + botScore.__str__() + ":" +myScore.__str__())
else:
    print(a + " wygral z " + d + " wynikiem " + myScore.__str__() + ":" + botScore.__str__())




















