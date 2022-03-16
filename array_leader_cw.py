def array_leaders(numbers):
    leader_list = []
    leader_index = [i for i in range(len(numbers)) if numbers[i] > sum(numbers[i+1:len(numbers)])]
    for i in leader_index:
        leader_list.append(numbers[i])
    return leader_list
#     leaders = []
#     for i in range(len(numbers)):
#         add = numbers[i+1:len(numbers)]
#         if numbers[i] > sum(add):
#             leaders.append(numbers[i])

#     return leaders

#     return [n for (i,n) in enumerate(numbers) if n>sum(numbers[(i+1):])]

print(array_leaders([16,17,4,3,5,2]))