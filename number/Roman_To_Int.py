ROMANS ={
    'M':1000,
    'CM':900,
    'D':500,
    'CD':400,
    'C':100,
    'XC':90,
    'L':50,
    'XL':40,
    'X':10,
    'IX':9,
    'V':5,
    'IV':4,
    'I':1,
}

def reverse_roman(roman_string):

    # 6 = VI => IV  
    # 4 = IV => VI
    # 499 = CDXCIX
    res = 0 

    # reverse ROMAN
    roman = roman_string[::-1]
    if roman_string:
        res += ROMANS[roman[0]]
    
    for i in range(1,len(roman)):
        if ROMANS[roman[i]]>=ROMANS[roman[i-1]]:
            res += ROMANS[roman[i]]
        else:
            res -= ROMANS[roman[i]]


    return res

print(reverse_roman('MMMDCCCLXXXVIII'))