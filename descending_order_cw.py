def descending_order(num):
    return int(''.join(sorted(i for i in str(num)))[::-1])

#     desc_list = []
#     for i in str(num):
#         desc_list.append(i)
#     return int(''.join(sorted(desc_list))[::-1])

print(descending_order(1201))
print(descending_order(123456789))