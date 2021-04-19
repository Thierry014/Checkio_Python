def find_quotes(a):
    quote = [] 
    new_quote = []
    res = []

    for i,char in enumerate(a):
        # get position of "
        if char == '"':
            quote.append(i)
    
    if len(quote)%2 == 1:
        quote.pop()
    
    for i in range(0,len(quote),2):
        new_quote.append([quote[i],quote[i+1]])
    
    for x in new_quote:
        res.append(a[x[0]+1:x[1]])



    return res



str  = '"good" morning mister "superman"'

print(find_quotes(str))