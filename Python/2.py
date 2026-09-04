def find_related(field, value):
    records = [
        {"key": 1, "id": "12345", "phone": "89997776655", "mail": "test@mail.ru"},
        {"key": 2, "id": "54321", "phone": "87778885566", "mail": "two@mail.ru"},
        {"key": 3, "id": "98765", "phone": "87776664577", "mail": "three@mail"},
        {"key": 4, "id": "66678", "phone": "87778885566", "mail": "four@mail.ru"},
        {"key": 5, "id": "34567", "phone": "84547895566", "mail": "four@mail.ru"},
        {"key": 6, "id": "34567", "phone": "89087545678", "mail": "five@mail.ru"},
        {"key": 7, "id": "11111", "phone": "80000000000", "mail": "seven@mail.ru"},
        {"key": 8, "id": "22222", "phone": "83333333333", "mail": "eight@mail.ru"},
    ]
    index_dict = {'id':{},'phone':{},'mail':{} }
    for idx,record in enumerate(records):
        for f in index_dict:
            index_dict[f].setdefault(record[f],[]).append(idx)
    queue:list = index_dict[field].get(value,[])
    visited = set()
    while queue:
        index = queue.pop()
        visited.add(index)
        for field in index_dict:
            for line in index_dict[field]:
                list_index = index_dict[field][line]
                if index in list_index:
                    for j in list_index:
                        if j not in visited:
                            queue.append(j)
    result = []
    for index in visited:
        result.append(records[index][field])
    result.sort()
    return result
                    
                    
print(find_related('mail','two@mail.ru'))