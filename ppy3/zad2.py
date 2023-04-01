import random

lista_miast = ["Warszawa", "Kraków", "Wrocław", "Łódź", "Poznań",
              "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok"]

print("Przkladowy pla wycieczki : ")
print()
lista=[]

for i in range(0,random.randint(2,10)):
    x=random.randint(0,len(lista_miast)-1)
    lista.append(lista_miast[x])
    lista_miast.pop(x)

for i in range(0, len(lista)):
    if i == 0 :
        print("Pojedz z " + lista[i])
    elif 0 < i < len(lista)-1:
        print(" przez " + lista[i])
    else:
        print(" az przyjedziesz do " + lista[i])