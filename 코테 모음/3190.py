from collections import deque
N = int(input())
K = int(input())
apple = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
way = [list(map(str, input().split())) for _ in range(L)]

arr = [[0]*(N+1) for _ in range(N+1)]

di = [0,1,0,-1] # 오 아래 왼 위
dj = [1,0,-1,0]

for k in range(K):
    i = apple[k][0]
    j = apple[k][1]
    arr[i][j] = 1
# print(*arr,sep="\n")
# print('')
k = 0
t = 0
i,j = 1,1 # 머리
x,y = 1,1 # 꼬리
snake = deque([[1,1]])
while True:
    # 몸길이 늘려 다음칸
    t+=1
    arr[i][j] = 2
    ni,nj = i+di[k],j+dj[k]
    if 1<=ni<N+1 and 1<=nj<N+1: 
        if arr[ni][nj] == 0:
            arr[ni][nj] = 2
            i,j = ni,nj
            snake.append([ni,nj])
            delete = snake.popleft()
            arr[delete[0]][delete[1]] = 0
        elif arr[ni][nj] == 1:
            arr[ni][nj] = 2
            i,j = ni,nj
            snake.append([ni,nj])
        else:
            break
    else:
        break
    # print(*arr,sep="\n")
    # print('')
    for a in range(L):
        if int(way[a][0]) == t:
            if way[a][1] == 'D':
                k+=1
                if k == 4:
                    k = 0
            else:
                k-=1
                if k == -1:
                    k = 3
# print(snake)
# print(*arr,sep="\n")
print(t)
    # 게임 끝
    # 사과 있으면 사과 없어지고 꼬리그대로
    # 사과 없으면 꼬리 줄이기


