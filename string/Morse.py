MORSE = {'a': '.-',    'b': '-...',  'c': '-.-.',
         'd': '-..',   'e': '.',     'f': '..-.',
         'g': '--.',   'h': '....',  'i': '..',
         'j': '.---',  'k': '-.-',   'l': '.-..',
         'm': '--',    'n': '-.',    'o': '---',
         'p': '.--.',  'q': '--.-',  'r': '.-.',
         's': '...',   't': '-',     'u': '..-',
         'v': '...-',  'w': '.--',   'x': '-..-',
         'y': '-.--',  'z': '--..',  '0': '-----',
         '1': '.----', '2': '..---', '3': '...--',
         '4': '....-', '5': '.....', '6': '-....',
         '7': '--...', '8': '---..', '9': '----.'
        }

def morse_decoder(text):
    #replace this for solution
    # split word
    text = text.split('   ')
    # split char
    res = []
    temp = ''
    for word in text:
        word = word.split(' ')
    # word = [1,2]
        for char in word:
            for key, value in MORSE.items():
                if char == MORSE[key]:
                # get key 
                    temp += key
        res.append(temp)
        temp = ''

    return (' ').join(res)


print(morse_decoder('... --- -- .   - . -..- -'))


def morse_encoder(text):
    text = text.lower()
    # some text => some text
    res = [] 
    for char in text:
        if char in MORSE:
            res.append(MORSE[char])
        else:
            res.append(' ')
    
    return (' ').join(res)

print(morse_encoder('some text'))