def count_words(text, words):
    count = 0 

    for word in words:
        text = text.lower()
        if word in text:
            count += 1

            print(word)

    return count

print(count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}))