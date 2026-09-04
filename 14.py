def is_subsequence(s:str, t:str):
    i_s = 0
    i_t = 0
    lenght = len(s)
    lenght_t = len(t)
    while i_s < lenght:
        while i_t < lenght_t:
            if s[i_s] == t[i_t]:
                i_s += 1
            i_t += 1
        else:
            break
    return i_s == lenght
    pass

s = 'axc'
t = 'ahbgdc'

print(is_subsequence(s, t))