N,M,L,K = map(int, input().split())
star = [list(map(int, input().split())) for _ in range(K)]
arr = [[0]*(N+1) for _ in range(M+1)]
for k in range(K):
    i = star[k][1]
    j = star[k][0]
    arr[i][j] = 1


print(*arr,sep="\n")