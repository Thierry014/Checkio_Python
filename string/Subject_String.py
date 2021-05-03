def isometric_strings(str1: str, str2: str) -> bool:
    # your code here
    if len(str1) != len(str2):
        return False
    
    dic = {}
    
    for i in range(len(str1)):
        dic[str1[i]] = str2[i]
    
    for char in str1:
        str1 = str1.replace(char,dic[char])
        
    return str1 == str2