N = int(input())
land = [list(map(int, input().split())) for _ in range(N)]
# print(*land, sep="\n")
visited = [[0]*N for _ in range(N)]

di = [0,1,-1,0,0]
dj = [0,0,0,-1,1]

ans = 200*10
cost = 0
def check(i,j):
    for k in range(5):
        ni,nj = i+di[k], j+dj[k]
        if visited[ni][nj] == 1:
            return False
    return True

def dfs(s,v):
    global ans,cost
    if s == 3:
        # print(cost)
        # print(*visited, sep="\n")
        ans = min(ans, cost)
        return
    else:
        for i in range(1,N-1):
            for j in range(1,N-1):
                if check(i,j):
                    for k in range(5):
                        ni,nj = i+di[k], j+dj[k]
                        visited[ni][nj] = 1
                        cost+=land[ni][nj]
                    dfs(s+1,v)
                    for k in range(5):
                        ni,nj = i+di[k], j+dj[k]
                        visited[ni][nj] = 0
                        cost-=land[ni][nj]
                    
dfs(0,visited)
print(ans)