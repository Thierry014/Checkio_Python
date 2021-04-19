def f_recusive(k):
    
    if k == 0:
        return 0
    elif k == 1 or k == 2:
        return 1
    else:
        return f_recusive(k-1) + f_recusive(k-2)


# print(f_recusive(9))

def f_for(k):
    a = 0
    b = 1

    if k == 1:
        return 1
    else:
        for i in range(1,k):
            c = a+b
            a = b
            b = c
        return a 

print(f_for(9))

