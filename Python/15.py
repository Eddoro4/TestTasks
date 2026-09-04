def longest_unique_substring(s):
    indexes = {}
    left_window = 0
    right_window = 0
    best = 0
    for i,char in enumerate(s):
        old_index = indexes.get(char,-1)
        if old_index >= left_window:
            left_window = old_index+1
        
        right_window += 1
        indexes.setdefault(char,i)
        indexes[char] = i
        best = max(best, right_window - left_window)
        
    return best
    pass
s = 'pwwkew'

print(longest_unique_substring(s))