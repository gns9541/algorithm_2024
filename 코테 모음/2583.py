import sys
sys.setrecursionlimit(10000)

M,N,K = map(int, input().split())
square = [list(map(int, input().split())) for _ in range(K)]
arr = [[0]*N for _ in range(M)]
# print(*arr, sep='\n')
# i == y, j == x
for k in range(K):
    for i in range(square[k][1],square[k][3]):
        for j in range(square[k][0],square[k][2]):
            arr[i][j] = 1
# print('')
# print(*arr, sep='\n')
# print('')

di = [1,-1,0,0]
dj = [0,0,-1,1]

ans = []
visited = [[0]*N for _ in range(M)]

def dfs(i,j,cnt):
    arr[i][j] = 2
    for k in range(4):
        ni,nj = i+di[k], j+dj[k]
        if 0<=ni<M and 0<=nj<N and arr[ni][nj] == 0 :
            # visited[ni][nj] = 1
            cnt = dfs(ni,nj,cnt+1)
    # print(*arr, sep='\n')
    # print('')
    return cnt
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            ans.append(dfs(i,j,1))
print(len(ans))
ans = sorted(ans)
print(*ans)

