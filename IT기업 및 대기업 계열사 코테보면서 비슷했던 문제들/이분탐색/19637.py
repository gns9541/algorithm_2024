def BS(target, n):
    start = 0
    end = N-1

    while start <= end:
        mid = (start + end) // 2
        if n[mid][1] < target:
            start = mid + 1
        else:
            start = mid - 1
    return n[start][0]

N, M = map(int, input().split())
name = [list(map(str, input().split())) for _ in range(N)]
p = [int(input()) for _ in range(M)]
n = []
for i in range(N):
    n.append([name[i][0], int(name[i][1])])
n.sort(key = lambda x:x[1])
print(p)
print(n)

for i in range(M):
    print(BS(p[i], n))
