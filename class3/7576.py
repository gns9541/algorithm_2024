from collections import deque
M,N = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]
queue = deque([])
# print(*T, sep="\n")
di = [1,-1,0,0]
dj = [0,0,-1,1]

for i in range(N):
    for j in range(M):
        if T[i][j] == 1:
            queue.append([i,j])

def BFS():
    while queue:
        i,j = queue.popleft()
        for k in range(4):
            ni,nj = i+di[k], j+dj[k]
            if 0<=ni<N and 0<=nj<M and T[ni][nj]==0:
                T[ni][nj] = T[i][j]+1
                queue.append([ni,nj])
        # print(*T, sep="\n")
        # print('')
BFS()
ans = 0
for i in T:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    ans = max(ans, max(i))
print(ans-1)
    

