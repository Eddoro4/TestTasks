nk = list(map(int,input().split()))
n = nk[0]
k = nk[1]
numbers = list(range(1,n+1))
for i in range(1,k+1):
    j = i+1
    if numbers[i] < numbers[j]:
        temp = numbers[i]
        numbers[i] = numbers[j]
        numbers[j] = temp

print(*numbers)