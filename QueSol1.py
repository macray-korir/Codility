def Solution(R):
    maximum_indicator = 0
    current_size = 0
    maximum_depth = 0
    current_depth = 0

    for i in range(len(R)):
        if R[1] != 0:
            current_size += 1
            current_depth = R[1]
            max_depth = max(maximum_depth,current_depth)
        else:
            current_indicator = current_size * max_depth
            maximum_indicator = max(maximum_indicator,current_indicator)
            current_size = 0
            max_depth = 0

    return maximum_indicator

lst = [1, 4, 1, 0, 5, 2, 3, 0, 8]
print(Solution(lst))

