def yaml(a):
    # your code here

    dic = {}
    # split based on \n
    # find pos of ':'  [0:index] => key [index+1:]=>value 
    #  if value isdigit => int(value)

    a = a.split('\n')

    for word in a:
        # remove line without content
        if len(word):
            word = word.replace('"', '').replace('\\','')
            index = word.find(':')
            key = word[:index]
            value= word[index+2:]

            value = int(value) if value.isdigit() else value

            dic[key] = value

    # print(dic)



    return dic

# ! test yamel 
# print(yaml("""name: Alex Fox
# age: 12

# class: 12b"""))



print(yaml("name: \"Alex \\\"Fox\\\"\"\nage: 12\n\nclass: 12b"))


