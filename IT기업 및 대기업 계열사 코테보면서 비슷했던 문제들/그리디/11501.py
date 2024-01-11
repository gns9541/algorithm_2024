
# 3 5 9
# 3             비용 : 3   0
# 5 5 - 이득 2   비용 : 8   1
# 9 9 9 -       비용 : 17  2

# 1         1
# 1 1       2
# 3 3 3     5
# 1 1 1 1   6
# 2 2 2 2   8

# 주가 오르면 사고 내리면 판다..!
T = int(input())
for _ in range(T):
    N = int(input())
    stock = list(map(int, input().split()))
    stock.reverse()
    max = stock[0]
    sum = 0

    for i in range(1, N):
        if max < stock[i]:
            max = stock[i]
            continue
        sum += max - stock[i]

    print(sum)    