n_prepyat = int(input())
n_pos = list(map(int,list(input().split())))
n_type = list(map(int,list(input().split())))
range_prepyat = [1,2,4]
type_prepyat = [1,3,5]
count_jump = int(input())
m_start_pos_jump = list(map(int,list(input().split())))
m_jump_range = list(map(int,list(input().split())))

way = []

money = 0
def generate_way():
    i = 0
    while(n_pos):
        if i == (n_pos[0]-1):
            if i > 0:
                if way[i-1] != 0:
                    money = 0
                    print("error way",way[i-1],i)
                    return
            type = n_type[0]
            range_p = range_prepyat[type-1]
            way.extend([type] * range_p)
            i += range_p
            del n_pos[0]
            del n_type[0]
        else:
            way.append(0)
            i+=1
        

generate_way()
i = 0
while i < len(way):
    if not m_start_pos_jump:
        print("Конец прыжков")
        break
    jump_pos = m_start_pos_jump[0] - 1
    jump_range = m_jump_range[0]
    end_pos_jump = jump_pos+jump_range
    if end_pos_jump > len(way):
        way.extend([0] * (end_pos_jump - len(way) + 1))
    if (way[i] != 0 and i != jump_pos):
        if i > 0 and way[i-1] == 0:
            print("споткнулся об камень",i+1)
            money -= 1
        i += 1
        print("Иду дальше")
    elif (i == jump_pos and way[end_pos_jump] != 0):
        money -= 1
        del m_start_pos_jump[0]
        del m_jump_range[0]
        i += jump_range
        print("Прыгнул и не долетел", i+1)
    elif i == jump_pos:
        set_jump = set(way[jump_pos:end_pos_jump])
        print("set",set_jump)
        for n in set_jump:
            if n == 0:
                continue
            money += type_prepyat[n-1]
            print("Перелетел",i+1)
        i += jump_range
        del m_start_pos_jump[0]
        del m_jump_range[0]
    else:
        print("иду к",i+1)
        i += 1

print("Сравнение",len(way),i)
print(way)
print(money)
        



