N,M = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(N)]

print(*road, sep="\n")


