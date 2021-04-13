def recall_password(grille, password):
    # your code here
    leng = len(password) - 1 
    res = ''
    # get 1st location form gril => [(0, 0), (1, 2), (2, 0), (2, 3)]
    location = []

    for i,word in enumerate(grille):    
        for j, char in enumerate(word):
            # print(char)
            if char == 'X':
                location.append([i,j])
    

    # transfer location to string [(0, 0), (1, 2), (2, 0), (2, 3)] =>  'ican' and rotate 
    def transfer_and_rotate(list):
        nonlocal location
        nonlocal res
        substr = ''
        for index, pos in enumerate(location):
            i = pos[0]
            j = pos[1]
            substr += password[i][j]
    
            # rotate => return location []

            location[index][0] = j
            location[index][1] = leng - i
        
       
        res += substr

        
        location = sorted(sorted(location, key = lambda k: k[1]), key= lambda ele: ele[0])
        return location
    
    for i in range(4):
        transfer_and_rotate(location)
        

    # print(res)


    


    


    



    return res




grille = ['X...', '..X.', 'X..X', '....']
password = ['itdf', 'gdce', 'aton', 'qrdi']
print(recall_password(grille, password))