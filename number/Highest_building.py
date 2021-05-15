def highest_building(building):
    result = [0,0]


    x = len(building)
    y = len(building[0])
    new_build = [[None for _ in range(x)] for i in range(y)]

    print(x,y)
    
    # rotate

    for i in range(y):
        for j in range(x):
            new_build[i][j] = building[x-j-1][i]
    
    height = 0
    for i, line in enumerate(new_build):
        print(line)
        if sum(line) > result[1]:
            result = [i+1,sum(line)]

    return result