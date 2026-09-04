n = int(input())
array = {}
for _ in range(n):
    string = input()
    array.setdefault(string,0)
    array[string] += 1
max = 0
words = []
for word in array:
    if array[word] >= max:
        max = array[word]
        words.append(word)
print(*words,sep='\n')


