def elevator_distance(array):
    return sum([abs(array[i+1]-array[i]) for i in range(0,len(array)-1)])


    # flights = 0
    # for i, j in enumerate(array):
    #     if i+1<len(array):
    #         flights += abs(array[i+1]-array[i])
    # return flights

print(elevator_distance([5, 2, 8]))
print(elevator_distance([7,1,7,1]))