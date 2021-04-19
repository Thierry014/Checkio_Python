def checkio(*args):
    if len(args) == 0:
        return 0
        
    big, small = args[0],args[0]
    for num in args:
        if num > big:
            big = num
        
        if num < small:
            small = num 
    return big - small 



print(checkio(1,2,3))


# ! optimized 

def checkio(*args):
    if args:
        return max(args) - min(args)
    return 0