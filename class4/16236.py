N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
di = [-1,0,1,0]
dj = [0,1,0,-1]
def BFS(i,j,c):
    for k in range(4):
        ni,nj = i+di[k], j+dj[k]
        if 0<=ni<N and 0<=nj<N and arr[i][j]>=arr[ni][nj]:
            visited[ni][nj] = 1
    pass