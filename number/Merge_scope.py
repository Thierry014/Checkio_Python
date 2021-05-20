def mergeNum(l1):
    pass


l1 = [[1,5],[6,10],[4,7]]

ranges = [l1[0]]

for i in range(1,len(l1)):
    for x in ranges:
        # x = (2,6)
        if l1[i][0]>x[1] or l1[i][1]<x[0]:
            # add new range 
            ranges.append([l1[i][0],l1[i][1]])
            break
        elif l1[i][0] < x[0] and l1[i][1]>x[1]:
            # update whole current range
            if l1[i][1] >= x[1]:
                x[0] = l1[i][0]
                x[1] = l1[i][1]
        
        else:
            # update upper or lower 
            if l1[i][0] < x[0]:
                x[0] = l1[i][0]
            elif l1[i][1]>x[1]:
                x[1] = l1[i][1]


print(ranges)

