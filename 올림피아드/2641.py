from collections import deque
N = int(input())
real = list(map(int, input().split()))
real = deque(real)
M = int(input())
sample = [list(map(int, input().split())) for _ in range(M)]
reverse_real = list(reversed(real))
reverse_real = deque(reverse_real)

reverse_sample = []
for i in range(M):
    lst = []
    for j in range(N):
        if sample[i][j] == 1:
            lst.append(3)
        elif sample[i][j] == 2:
            lst.append(4)
        elif sample[i][j] == 3:
            lst.append(1)
        elif sample[i][j] == 4:
            lst.append(2)
    reverse_sample.append(lst)
# print(reverse_sample)
ans = []

for i in range(M): # 그냥 로테이트
    k = 0
    while True:
        if k == N:
            break
        real.rotate(1)
        if list(real) == sample[i] or list(real) == reverse_sample[i]:
            ans.append(i)
            break
        k+=1
    # print(ans,i)
    if i not in ans:
        k = 0
        while True:
            if k == N:
                break
            reverse_real.rotate(1)
            # print(list(reverse_real),i)
            # print(reverse_sample[i])
            if list(reverse_real) == sample[i] or list(reverse_real) == reverse_sample[i]:
                ans.append(i)
                break
            k+=1
        # print(ans,i)
# print(ans)
print(len(ans))
for i in range(M):
    if i in ans:
        print(*sample[i])



    



