def max_dist_to_closest(seats):
    last_busy = -1
    max_dist = 0
    for i in range(len(seats)):
        if seats[i] == 1:
            if last_busy == -1:
                max_dist = max(max_dist, i)
            else:
                max_dist = max(max_dist,(i - last_busy) // 2)
            last_busy = i
    return max(max_dist, len(seats) - last_busy - 1)
    pass

seats = [1, 0, 0, 0, 1, 0, 1]

print(max_dist_to_closest(seats))