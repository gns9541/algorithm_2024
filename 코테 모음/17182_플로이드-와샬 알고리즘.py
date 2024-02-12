#플로이드-와샬 알고리즘 공부하기


# N, K = map(int, input().split()) # 시작 위치
# arr = [list(map(int, input().split())) for _ in range(N)]
# visited = [0]*N
# ans = float('inf')

# def dfs(i,v,t):
#     global min

#     if v == N:
#         ans = min(ans, t)
#         return
    
#     for k in range(N):
#         if not visited[i]:
#             dfs(k,v+1,t+arr[i][k])
#             visited[i] = 1
# dfs(K,1,0)
# print(ans)
