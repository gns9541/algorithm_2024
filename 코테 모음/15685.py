king, stone, N = map(str, input().split())
N = int(N)
move = [input() for _ in range(N)]
arr = [[0]*10 for _ in range(10)]
# w = [0,'A','B','C','D','E','F','G','H']
w = [0,'H','G','F','E','D','C','B','A']
way = ['R','L','B','T','RT','LT','RB','LB']
di = [0,0,1,-1,-1,-1,1,1]
dj = [1,-1,0,0,1,-1,1,-1]

# print(king, stone, N)
# print(move)
ki,kj = int(king[1]),0
si,sj = int(stone[1]),0
for i in range(9):
    if w[i] == king[0]:
        kj = i
    if w[i] == stone[0]:
        sj = i
# print([ki,kj],[si,sj])


for i in range(1,9):
    for j in range(1,9):
        if i == ki and j == kj:
            arr[i][j] = 1
        if i == si and j == sj:
            arr[i][j] = 2
# print(*arr, sep="\n")
# print('')
def rotate(lst):
    ret = [[0] * 10 for _ in range(10)]

    for r in range(10):
        for c in range(10):
            ret[10-1-r][10-1-c] = lst[r][c]
    return ret
arr = rotate(arr)
# print(*arr, sep="\n")

for m in range(len(move)):
    for a in range(8):
        if way[a] == move[m]:
            cnt = 0
            for i in range(10):
                for j in range(10):
                    if arr[i][j] == 1 and cnt == 0:
                        ni,nj = i+di[a],j+dj[a]
                        if 1<=ni<9 and 1<=nj<9:
                            if arr[ni][nj] == 0:
                                arr[ni][nj] = 1
                                arr[i][j] = 0
                                cnt += 1
                            elif arr[ni][nj] == 2:
                                ai,aj = i+2*di[a], j+2*dj[a]
                                if 1<=ai<9 and 1<=aj<9:
                                    arr[ai][aj] = 2
                                    arr[ni][nj] = 1
                                    arr[i][j] = 0
                                cnt += 1

        # print('')
        # print(way[a],*arr, sep="\n")

k = 0
s = 0
for i in range(10):
    for j in range(10):
        if arr[i][j] == 1:
            k = [i,j]
        if arr[i][j] == 2:
            s = [i,j]

print(w[9-k[1]]+str(9-k[0]))
print(w[9-s[1]]+str(9-s[0]))


