def to26digit(value : int):
    return chr(ord("a") + (value % 26))

def to10digit(value : str):
    return ord(value) - ord("a")

def base10to26(value : int):
    output = ""
    while value > 0:
        digit = value % 26
        value //= 26
        output = to26digit(digit) + output
    if output == "":
        return "a"
    return output

def base26to10(value : str):
    output = 0
    for digit in value[::-1]:
        output *= 26
        output += to10digit(digit)
    return output