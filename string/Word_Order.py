def words_order(text, words):
    # your code here
    dic = {}

    text = text.split(' ')
    for i,word in enumerate(text):
        dic[word] = i
    
    for word in words:
        if word not in dic:
            return False
        
    for i in range(1,len(words)):
        if dic[words[i]] <= dic[words[i-1]]:
            return False
    return True


print(words_order('hi world im here', ['world', 'here']))