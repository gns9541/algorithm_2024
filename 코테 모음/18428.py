N = int(input())
arr = [list(map(str, input().split())) for _ in range(N)]
ans = False

teacher = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == "T":
            teacher+=1

di=[1,-1,0,0]
dj=[0,0,-1,1]

def checking(i,j):
    for k in range(4):
        ni = i+di[k]
        nj = j+dj[k]
        while 0<= ni < N and 0<= nj < N and arr[ni][nj] !='O':
            if arr[ni][nj] == 'S':
                return True            
            else:        
                ni += di[k]
                nj += dj[k]
    return False

def obj(cnt):
    global ans
    if cnt == 3:
        passing = 0
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 'T':
                    if not checking(i,j):
                        passing+=1
        if passing == teacher:
            ans = True
        return

    for i in range(N):
        for j in range(N):
            if arr[i][j] == "X":
                arr[i][j] = "O"
                cnt+=1
                obj(cnt)
                arr[i][j] = "X"
                cnt-=1
obj(0)
if ans:
    print('YES')
else:
    print('NO')

