def from_camel_case(name):
    #replace this for solution


    name = name.replace(name[0],name[0].lower(),1)

    for i in range(len(name)):
        if name[i].isupper() == True:
            
            name = name.replace(name[i],'_'+name[i].lower(),1)
            

    return name


def to_camel_case(name):
    # first letter =>upper case
    name = name.replace(name[0],name[0].upper(),1)
    i = 1

    while i < len(name):
        if name[i] == '_':
            name = name.replace(name[i],'',1)
            name = name[:i] + name[i].upper() + name[i+1:]
            
        #  if last char is _
        i +=1 

        
    
    return name




# test
print(from_camel_case('MyFunctionName'))

print(to_camel_case('my_function_name'))