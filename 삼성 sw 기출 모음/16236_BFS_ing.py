N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(*arr, sep="\n")

di=[1,-1,0,0]
dj=[0,0,1,-1]

start = []
x,y = 0,0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            arr[i][j] = 2
            x,y = i,j
            break
            # start.append(i)
            # start.append(j)

def dfs(i,j,t,body,c):
    flag = 0
    for a in range(N):
        for b in range(N):
            if arr[a][b]!=0 and arr[i][j]>arr[a][b]:
                flag+=1
                break
    if flag > 0:
        for k in range(4):
            ni,nj = i+di[k], j+dj[k]
            if 0<=ni<N and 0<=nj<N:
                if arr[ni][nj] < arr[i][j]:
                    if body == c:
                        arr[ni][nj] = 0
                        dfs(ni,nj,t+1,body+1,0)
                    else:
                        arr[ni][nj] = 0
                        dfs(ni,nj,t+1,body,c+1)
                elif arr[ni][nj] == arr[i][j]:
                    dfs(ni,nj,t+1,body,0)
    else:
        print(t)
        return 
dfs(x,y,0,2,0)