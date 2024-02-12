H,W,X,Y = map(int, input().split()) # 2 4 1 1
B = [list(map(int, input().split())) for _ in range(H+X)]
A = [[-1]*W for _ in range(H)]
arr = [[0]*(W+Y) for _ in range(H+X)]
# print(*A, sep='\n')
# print(*arr, sep='\n')
for i in range(H):
    for j in range(W):
        arr[i][j] = -1
# print(*arr, sep="\n")

for i in range(H):
    for j in range(W):
        if arr[i+X][j+Y] == -1:
            arr[i+X][j+Y] = -2
        else:
            arr[i+X][j+Y] = -1
# print(*arr, sep="\n")

for i in range(H+X):
    for j in range(W+Y):
        if arr[i][j] == -1:
            if 0<=i<H and 0<=j<W:
                A[i][j] = B[i][j]
# print(*A,sep="\n")

for i in range(H+X):
    for j in range(W+Y):
        if arr[i][j] == -2:
            if 0<=i<H and 0<=j<W:
                A[i][j] = B[i][j]-A[i-X][j-Y]
print(*A,sep="\n")
for i in range(len(A)):
    print(*A[i])

# 1 1 1 1
# 1 1 1 1

# 0 0 0 0 0
# 0 1 1 1 1
# 0 1 1 1 1 


