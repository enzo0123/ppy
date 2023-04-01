def metoda(key, number):
    array = list(key)
    result = ""
    for znak in array:
        if znak.isalpha():
            x = ord(znak)
            x = x + number
            znak = chr(x)
        result = result + znak
    return result


print(metoda("", 5))
