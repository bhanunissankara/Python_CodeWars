def vowel_2_index(string):
    str1 = ''
    for i, j in enumerate(string):
        if j in "aeiouAEIOU":
            str1 += str(i+1)
        else:
            str1 += j
    return str1

    # vowels = 'aeiouAEIOU'
    # return ''.join(j if j not in vowels else str(i+1) for i, j in enumerate(string))

print((vowel_2_index('thias is my string')))