N = int(input())
Point = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
Hole = [list(map(int, input().split())) for _ in range(K)]
w = Point[-1][0]
print(Point)
print(w)
h = 0
for i in range(N):
    h = max(h,Point[i][1])
print(h)
print(Hole)
arr = [[0]*(w+1) for _ in range(h+1)]
print(*arr,sep="\n")

for i in range(h+1):
    for j in range(w+1):
        pass




