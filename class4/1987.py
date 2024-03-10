# import sys
# sys.setrecursionlimit(10**6)

R,C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
# print(arr)
visited = [arr[0][0]]
di = [1,-1,0,0]
dj = [0,0,-1,1]

ans = 0

def dfs(i,j,c,v):
    global ans
    for k in range(4):
        ni,nj = i+di[k], j+dj[k]
        if 0<=ni<R and 0<=nj<C and arr[ni][nj] not in v:
            v.append(arr[ni][nj])
            dfs(ni,nj,c+1,v)
            v.pop()
    ans = max(ans,c)
dfs(0,0,1,visited)
print(ans)