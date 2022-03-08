def points(games):
    points = 0
    for i in games:
        if int(i[0]) > int(i[2]):
            points += 3
        elif int(i[0]) == int(i[2]):
            points -= 1

    return points


print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))