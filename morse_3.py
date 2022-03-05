def decode_morse(morse_code):
    decoded_word = ''
    for word in morse_code.split('   '):
        letter = ''.join(word.split(' '))
        if decoded_word == '':
            decoded_word = decoded_word + letter
        else:
            decoded_word = decoded_word + ' ' + letter
        print(letter)
    return decoded_word

print(decode_morse("H o w   a r e   y o u"))

