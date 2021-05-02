def sort_by_ext(files):
    # your code here
    return files


a = ['1.cad', '1.bat', '.aba','2.aa']
# => [['1', 'cad'], ['1', 'bat'], ['1', 'aa']]
a = [x.split('.') for x in a]

print(sorted(a,key=lambda k: (k[0],k[1])))




# ! checkio version 

def sort_by_ext(files):
    # 
    no_name = []
    res =  sorted([x.split('.') for x in files],key=lambda k: (k[1],k[0]))
    print(res)
    
    for i,ele in enumerate(res): 
        if ele[0] == '':
            print('remove')
            no_name.append(ele)
            res.pop(i)
    
    res = no_name + res
    res = sorted(res,key=lambda k: len(k))
    return [('.').join(x) for x in res]