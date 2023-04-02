def metoda(key, number):
    if number > 31 :
        return "Wprowadzono błędne dane"
    array = list(key)
    result = ""
    for znak in array:
        if znak.isalpha():
            x = ord(znak)
            if x < 97 :
                x=x+32
            if x+number>122 :
                x=x+number-26
            else:
                x=x+number
            znak = chr(x)
        result = result + znak
    return result


print(metoda("zAbyW", 3))