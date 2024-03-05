import sys
sys.setrecursionlimit(10**6)
T = int(input())
for _ in range(T):
    M,N,K = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(K)]
    arr = [[0]*M for _ in range(N)]
    for k in range(K):
        i = lst[k][1]
        j = lst[k][0]
        arr[i][j] = 1
    # print(*arr, sep="\n")
    di = [1,-1,0,0]
    dj = [0,0,-1,1]
    cnt = 0

    def dfs(i,j):
        for k in range(4):
            ni,nj = i+di[k],j+dj[k]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 1:
                arr[ni][nj] = 0
                dfs(ni,nj)

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                dfs(i,j)
                cnt+=1
    print(cnt)
        
            