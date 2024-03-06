import sys
sys.setrecursionlimit(10**6)

V = int(input())
tree = [0]+[list(map(int, input().split())) for _ in range(V)]
# print(tree)
visited = [0]*(V+1)

ans = 0
def dfs(i,c,v):
    global ans
    for k in range(1,len(tree[i])-1):
        if k%2!=0:
            if v[tree[i][k]] == 0:
                v[i] = i
                dfs(tree[i][k],c+tree[i][k+1],v)
                v[i] = 0
            else:
                ans = max(ans,c)
                return
            # print(i,v,c)
            # print('')
for i in range(1,V+1):
    dfs(i,0,visited)
print(ans)