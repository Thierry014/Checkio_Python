def checkio(numbers):
    # checkio([5, 6, -10, -7, 4]) == 8
    x = numbers
    x.append(0)
    y = [0,x[0]]

    # x = [5,6,-10,-7,4]
    # y = [0,5]

    for num in numbers[1:]:
        y.append(num+max(y[-1],y[-2]))

        # y= [0,5,6+5=11]
    
    return y[-1]

print(checkio([5,6,-10,-7,4]))
    
