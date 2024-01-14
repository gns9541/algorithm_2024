N,M = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(N)]

di, dj = [1,1,1],[1,0,-1]

ans = []
def dfs(x,y,f,n):
    if x == N-1:
        ans.append(f)
    for k in range(3):
        dx = x+di[k]
        dy = y+dj[k]
        if 0<=dx<N and 0<=dy<M:
            if k != n:
                dfs(dx,dy,f+road[dx][dy],k)

for i in range(M):
    dfs(0,i,road[0][i],4)

print(min(ans))
