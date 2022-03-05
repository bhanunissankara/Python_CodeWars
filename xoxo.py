def xoxo(input_str):
    x = 0
    o = 0
    for element in input_str:
        if element.lower() == 'x':
            x = x+1
        elif element.lower() == 'o':
            o = o+1
    if x == 0 and o == 0:
        return True
    elif x == o:
        return True
    else:
        return False

print(xoxo("oX"))



# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false


#def xo(s):
#    s = s.lower()
#    return s.count('x') == s.count('o')

# def xo(s):
#    return s.lower().count('x') == s.lower().count('o')
