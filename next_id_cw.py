def next_id(arr):
    if not arr:
        return 0
    j = None
    highest_num = sorted(arr)[::-1][0]
    for i in range(0, highest_num):
        if i not in arr:
            j = i
            break
    if j is not None:
        return j
    else:
        return highest_num + 1
    # t = 0
    # while t in arr:
    #     t +=1
    # return t

print(next_id([9,8,0,1,7,6]))