N,M = map(int,input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]

di = [1,-1,0,0]
dj = [0,0,1,-1]

def check(x,y,arr,K):
    # for i in range(N):
    #     for j in range(M):
    #         if arr[i][j] == 1:
    #             for k in range(4):
    #                 ni,nj = i+di[k], j+dj[k]
    #                 while 0<=ni<N and 0<=nj<M:
    #                     if arr[ni][nj] == 1:
    #                         return False
    #                     else:
    #                         ni+=di[k]
    #                         nj+=dj[k]
    #                 return True
    for k in range(4):
        if k == K:
            ni,nj = x+di[k], y+dj[k]
            while 0<=ni<N and 0<=nj<M:
                if arr[ni][nj] == 1:
                    return False
                else:
                    ni+=di[k]
                    nj+=dj[k]
                    return True
                

def melt(arr):
    t=0
    while True:
        cnt = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    cnt+=1
        if cnt == N*M:
            break

        for i in range(N):
            for j in range(M):
                if arr[i][j] == 1:
                    cnt = 0
                    for k in range(4):
                        ni,nj = i+di[k], j+dj[k]
                        if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0:
                            if check(i,j,cheese,k):
                                cnt+=1

                    if cnt >=2:
                        arr[i][j] = 2
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 2:
                    arr[i][j] = 0
        t+=1
        # print('')
        # print(*arr,sep='\n')
    print(t)
melt(cheese)

                 
                    


    

    


