x=int(input("Podaj pierwsza liczbe : "))
y=int(input("Podaj druga liczbe : "))
z=input("Podaj operator : ")

if z.__eq__("+"):
    print(x+y)
elif z.__eq__("-"):
    print(x-y)
elif z.__eq__("/"):
    print(x/y)
elif z.__eq__("*"):
    print(x*y)