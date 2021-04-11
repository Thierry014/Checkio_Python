def caps_lock(text: str) -> str:

    isCap = False
    res = ''
    
    for char in text:
        if char == 'a':
            isCap = not isCap
        else:
            if isCap:
                char = char.upper()
            res += char


    return res

# test
print(caps_lock('abc'))
print(caps_lock("Why are you asking me that?"))
print(caps_lock("Always wanted to visit Zambia."))