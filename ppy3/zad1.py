import re

wpis = input("Podaj kilka liczb rozdzielonych przecinkami ... ")
lista = wpis.split(",")
min = 50000000
max = 0

for i in range(0, len(lista)):
    x = int(re.sub(r"\D+", "", lista[i]))
    if x <= min:
        min = x
    elif x >= max:
        max = x

print("Max : " + str(max))
print("Min : " + str(min))
