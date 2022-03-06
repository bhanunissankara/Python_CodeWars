def create_phone_number(n):
    # Original solution
    #return '(' + n[0].__str__() + n[1].__str__() + n[2].__str__() + ')' + ' ' + n[3].__str__() + n[4].__str__() + n[5].__str__() \
    #        + '-' + n[6].__str__() + n[7].__str__() + n[8].__str__() + n[9].__str__()

    phone = ''.join(str(x) for x in n)
    return '(' + str(phone[0:3]) + ')' + ' ' + phone[3:6] + '-' + phone[6:10]

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))