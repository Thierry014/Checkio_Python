def checkio(number):
    # list 
    l1 = [1,2]
    res = 2

    while res < 100:
        l1.append(sum(l1))
        res = l1[-1]

    
    for i, value in enumerate(l1):
        if number < value:
            return i - 1
    
    return 0


print(checkio(10))





