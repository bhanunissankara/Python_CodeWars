def decode_morse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    spaces = morse_code.count('   ')
    i = 0
    final_word = ''
    while i <= spaces:
        words.append(morse_code.split('   ')[i])
        i = i + 1
    for element in words:
        letter = decode_word(element)
        if final_word == '':
            final_word = final_word + letter
        else:
            final_word = final_word + ' ' + letter

    print(final_word)
    return final_word

def decode_word(input_morse):
    spaces = input_morse.count(' ')
    j = 0
    letter = ''
    while j <= spaces:
        letter = letter + input_morse.split(' ')[j]
        j = j + 1
    return letter

    # morse = morse_code.split()
    # str = ''
    # for i in range(len(morse)):
    #     morse[i] = MORSE_CODE[morse[i]]
    # print(morse)
    #return morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')

decode_morse("H o w w   a r e   y o u")

#def decodeMorse(morseCode):
#    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))
