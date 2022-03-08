def better_than_average(class_points, your_points):
    return True if sum(class_points)/len(class_points) < your_points else False

    # if sum(class_points)/len(class_points) < your_points:
    #     return True
    # return False

print(better_than_average([10,10], 10))