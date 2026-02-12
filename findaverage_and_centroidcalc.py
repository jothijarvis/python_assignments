# Find Average of int arguments. And calculate the centroid of varying dimensional points as arguments. author: Jothiswarooban
'''Assignment 3: Find average'''
def average_calc(*args):
    # add exception for none case
    if len(args) > 0:
        int_avg = sum(args)/len(args)
        return int_avg
    else :
        return 0

result = average_calc(1,2,3,4,5,8,6)
print("Average of input number:",result)



'''Assignment 4: Find centroid of varying dimensional points'''
def centroid(*args):
    max_len = 0
    for point in args:
        if len(point) > max_len:
            max_len = len(point)

    new_points = []
    for point in args:
        new_points.append(point + [0] * (max_len - len(point)))

    # print(new_points)
    # can user zip_longest from itertools
    centroid_val = []
    for i in range(max_len):
        col_sum = 0
        for point in new_points:
            col_sum += point[i]
        centroid_val.append(col_sum / len(new_points))

    return centroid_val
# provide as *args
# input_points = ([1, 2, 3], [5, 6], [9, 7, 6, 5, 4], [21, 34], [75], [89], [-25, 90], [2, 3, 4] , [67], [1, 2, 3], [5, 6],[21, 34], [75], [89], [-25, 90], [2, 3, 4])
centroid_val = centroid([1, 2, 3], [5, 6], [9, 7, 6, 5, 4], [21, 34], [75], [89], [-25, 90], [2, 3, 4] , [67], [1, 2, 3], [5, 6],[21, 34], [75], [89], [-25, 90], [2, 3, 4])
print("Centroid:", centroid_val)