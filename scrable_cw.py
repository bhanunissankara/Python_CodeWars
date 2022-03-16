"""
Complete the function scramble(str1, str2) that returns true if a
portion of str1 characters can be rearranged to match str2, otherwise returns false.
"""

def count_items(items):
    result = {}
    for item in items:
        result[item] = result.get(item, 0) + 1
    return result

def scramble(s1, s2):
    can_create = True
    s1_map = count_items(s1)
    s2_map = count_items(s2)
    for key, value in s2_map.items():
        try:
            if value > s1_map[key]:
                can_create = False
        except KeyError:
                return False
    return can_create

"""
test.assert_equals(scramble('rkqodlw', 'world'),  True)
test.assert_equals(scramble('cedewaraaossoqqyt', 'codewars'), True)
test.assert_equals(scramble('katas', 'steak'), False)
test.assert_equals(scramble('scriptjava', 'javascript'), True)
test.assert_equals(scramble('scriptingjava', 'javascript'), True)

def scramble(s1,s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True
"""