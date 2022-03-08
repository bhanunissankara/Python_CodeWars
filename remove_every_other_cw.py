def remove_every_other(my_list):
    ret_list = []
    for i, element in enumerate(my_list):
        if i%2 == 0:
            ret_list.append(element)
    return ret_list

# return [v for c,v in enumerate(my_list) if not c%2]

print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))
print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))