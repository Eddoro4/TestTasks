def shortest_distance(elements):
    indexes_x = []
    indexes_y = []
    for idx,element in enumerate(elements):
        if element == 'X': indexes_x.append(idx)
        elif element == 'Y': indexes_y.append(idx)
    
    if not indexes_x or not indexes_y: return None
    shortest = float('inf')
    for el_x in indexes_x:
        for el_y in indexes_y:
            shortest = min(shortest, abs(el_x - el_y))
    return shortest
    pass

elements = ['Y', 'Z', 'Z', 'X', 'Z', 'Y']

print(shortest_distance(elements))