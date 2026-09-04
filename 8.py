import math
nt = list(map(int,input().split()))
n = nt[0]
t = nt[1]
numbers_cell = list(map(int,input().split()))
x_n = [0 for _ in range(n)]
y_n = [0 for _ in range(n)]
for iteration,number in enumerate(numbers_cell):
    y = math.floor(number / (n+1))
    x = ((number-1) % n)
    x_n[x] += 1
    y_n[y] += 1
    if max(*x_n,y_n) >= 3:
        print(iteration)
        break
else:
    print(-1)

    

