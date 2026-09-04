nk = list(map(int,input().split()))
n = nk[0]
k = nk[1]
numbers = list(map(int,input().split()))
S = []
lenght = len(numbers)
for i,number in enumerate(numbers):
    if((i+1) > lenght):
        break
    for j in range(i+1,lenght):
        S.append(number * numbers[j])
S.sort()
print(S[k-1])