ROMANS =(('M',  1000),
          ('CM', 900),
          ('D',  500),
          ('CD', 400),
          ('C',  100),
          ('XC', 90),
          ('L',  50),
          ('XL', 40),
          ('X',  10),
          ('IX', 9),
          ('V',  5),
          ('IV', 4),
          ('I',  1))

def checkio(data):
    res = ''

    for roman in ROMANS:
        num = data // roman[1]
        if num > 0 :
            for i in range(num):
                res += roman[0]
        data %= roman[1]

    
   

    #replace this for solution
    return res


    # 6=> VI
print(checkio(499))

