N = int(input())
Point = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
Hole = [list(map(int, input().split())) for _ in range(K)]
w = Point[-1][0]
h = 0
for i in range(N):
    h = max(h,Point[i][1])



arr = [[0]*(w+1) for _ in range(h+1)]
print(*arr,sep="\n")

# for i in range(N):
#     if Point[i][0] == Point[i+1][0]:
#         for a in range()




        




