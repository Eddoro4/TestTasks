def find_unique_elements(list1, list2):
    i_list1 = 0
    i_list2 = 0
    lenght_1 = len(list1)
    lenght_2 = len(list2)
    result = []
    while i_list1 < lenght_1 and i_list2 < lenght_2:
        num = list1[i_list1]
        num2 = list2[i_list2]
        if num < num2:
            result.append(num)
            i_list1 += 1
        elif num > num2:
            i_list2 += 1
        elif num == num2:
            i_list1 += 1
            i_list2 += 1
    if i_list1 < lenght_1:
        result.extend(list1[i_list1:])
    return result
    pass

list1 = [1, 3, 5, 7, 9]
list2 = [2, 3, 5, 6, 8]

print(find_unique_elements(list1, list2))
#[1, 7, 9]