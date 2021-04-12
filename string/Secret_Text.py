def find_message(message: str) -> str:

    res = ''


    # message = > How are you? Eh, ok. Low or Lower?

    for char in message:
        if char.isupper():
            res += char
    
    return res


print(find_message('How are you? Eh, ok. Low or Lower?'))



