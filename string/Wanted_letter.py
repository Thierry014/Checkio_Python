def checkio(text):

    dic = {}

    text = sorted(text.lower())
    for char in text:
        if char.isalpha():
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 0

    #"how do you do?"


    print(dic)
    sort_list = sorted(dic, key = lambda k: dic[k], reverse=True)
    print(sort_list)

    return sort_list[0] if sort_list[0] else ''



# test
print(checkio("how do you do?"))
print(checkio("Hello World!"))
print(checkio("bca!!!!"))