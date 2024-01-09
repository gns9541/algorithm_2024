N, M, L, K = map(int, input().split())
stars = [list(map(int,input().split())) for _ in range(K)]

earth = [[0]*(N+1) for _ in range(M+1)]

for i in range(K):
    earth[stars[i][1]][stars[i][0]] = 1
print(*earth, sep="\n")

ans = []
for i in range(1,N-L):
    for j in range(1,M-L):
        cnt = 0
        for l in range(L):
            if earth[i+l][j] == 1:
                cnt +=1
            if earth[i][j+l] == 1:
                cnt += 1
    ans.append(cnt)
print(ans)
print(max(ans))