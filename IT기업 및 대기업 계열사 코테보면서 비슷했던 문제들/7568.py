N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]

ans = []
for i in range(N):
    cnt = 1
    for j in range(N):
        if D[i][0] < D[j][0] and D[i][1] < D[j][1]:
            cnt += 1
        # else:
        #     cnt += 1
    ans.append(cnt)
print(*ans)