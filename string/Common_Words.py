# assert checkio('hello,world', 'hello,earth') == 'hello'
# assert checkio('one,two,three', 'four,five,six') == ''
# assert checkio('one,two,three',#  'four,five,one,two,six,three') == 'one,three,two'


def checkio(line1,line2):


    res = []
    dic = {}

    line1 = line1.split(',')
    # 'hello,world' => ['hello','world']

    line2 = line2.split(',')

    for word in line1:
        dic[word] = True
    
    # dic = {'hello':True}
    for word in line2:
        if word in dic:
            res.append(word)

    return (',').join(res)



# test 
print(checkio('hello,world', 'hello,earth'))
print(checkio('one,two,three','four,five,one,two,six,three'))