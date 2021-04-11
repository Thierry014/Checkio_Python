    # assert follow("fflff") == (-1, 4)
    # assert follow("ffrff") == (1, 4)
    # assert follow("fblr") == (0, 0)

def follow(instructions):
    x = 0
    y = 0 


        # f => y+=1  b:y-=1
        # l => x-=1, r:x+=1

    for char in instructions:
        if char == 'f':
            y += 1
        elif char == 'b':
            y -= 1
        elif char == 'l':
            x -= 1
        else:
            x += 1 

    return (x,y)


    # test 
print(follow("fflff"))