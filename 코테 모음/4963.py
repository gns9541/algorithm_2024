import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000)
def dfs(i,j):
    di = [1,-1,0,0,1,1,-1,-1]
    dj = [0,0,-1,1,1,-1,1,-1]
    arr[i][j] = 0
    for k in range(8):
        ni,nj = i+di[k], j+dj[k]
        if 0<=ni<h and 0<=nj<w and arr[ni][nj] == 1:
            dfs(ni,nj)

while True:
    w,h = map(int, input().split()) #j,i
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    # print(*arr, sep="\n")
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                dfs(i,j)
                cnt += 1
    print(cnt)







