def checkio(num):
    res = 1

#  123 => [1,2,3]
    num = list(str(num))

# remove 0 
    num = [ int(x) for x in num if x!='0']
    
    for x in num:
        res *= x

    return res




print(checkio(1024))