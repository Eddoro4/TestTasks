def longest_consecutive(nums:list) -> int:
    sorted_list = sorted(list(set(nums)))
    n = 0
    number = 0
    if sorted_list:
        n = 1
        number = sorted_list.pop(0)
    for i in sorted_list:
        if i == number+1:
            n += 1
            number = i
        else:
            break
    return n
    

print(longest_consecutive([100, 4, 200, 1, 3, 2]))