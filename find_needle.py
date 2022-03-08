def find_needle(haystack):
    return ''.join('found the needle at position '+str(i) for i, j in enumerate(haystack) if j == 'needle')

print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))
print(find_needle(['283497238987234', 'a dog', 'a cat', 'some random junk', 'a piece of hay', 'needle', 'something somebody lost a while ago']))
