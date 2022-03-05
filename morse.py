def decode_morse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    spaces = morse_code.count('   ')
    i = 0
    words = []
    final_word = ''
    while i <= spaces:
        words.append(morse_code.split('   ')[i])
        i = i + 1
    for element in words:
        spaces = element.count(' ')
        letter = ''
        letters = []
        j = 0
        while j <= spaces:
            letter = letter + element.split(' ')[j]
            # letter = letter + MORSE_CODE[element.split(' ')[j]]
            j = j + 1
        if(final_word == ''):
            final_word = final_word + letter
        else:
            final_word = final_word + ' ' + letter

    print(final_word)
    return final_word

    # morse = morse_code.split()
    # str = ''
    # for i in range(len(morse)):
    #     morse[i] = MORSE_CODE[morse[i]]
    # print(morse)
    #return morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')

decode_morse("H o w w   a r e   y o u")
