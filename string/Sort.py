def sort_by_ext(files):
    # your code here
    return files


a = ['1.cad', '1.bat', '.aba','2.aa']
# => [['1', 'cad'], ['1', 'bat'], ['1', 'aa']]
a = [x.split('.') for x in a]

print(sorted(a,key=lambda k: (k[0],k[1])))