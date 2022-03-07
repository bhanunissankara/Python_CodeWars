def pipe_fix(nums):
    num = nums[0]
    arr1 = [num]
    while num < max(nums):
        arr1.append(num+1)
        num += 1
    return arr1

# return list(range(nums[0], nums[-1] + 1))

print(pipe_fix([1, 2, 3]))