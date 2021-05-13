def checkio(words):
    longest = 0
    longest_word = []

    for word in words:
        if len(word) > longest:
            longest = len(word)
            longest_word = [word]
        elif len(word) == longest: 
            longest_word.append(word)

    words = [x for x in words if len(x)<longest]

# check words[i] == longest_word[0][len(words)[i]*-1:]
    for long_word in longest_word:
        for short_word in words:
            if short_word == long_word[len(short_word)*-1:]:
                return True
    
    return False

# words = {'hello','hi','hower','l'}
# print(checkio(words))


def end_with(words):
    for word in words:
        for target in words:
            if word != target and target == word[len(target)*-1:]:
                return True
    
    return False


words = {'hello','hi','hower','l'}
print(checkio(words))