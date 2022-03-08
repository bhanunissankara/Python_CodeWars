def remove_char(s):
    return ''.join(s[i] for i in range(1,len(s)-1,1))

    # str1 = ''
    # for i in range(1, len(s)-1,1):
    #     str1 += s[i]
    # return str1

print(remove_char('eloquent'))
print(remove_char('country'))