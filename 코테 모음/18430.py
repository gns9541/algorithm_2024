N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ai=[1,0]
aj=[0,1]
bi=[1,0]
bj=[0,-1]
ci=[-1,0]
cj=[0,1]
di=[-1,0]
dj=[0,-1]


def make(arr,i,j,cnt):
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                for k in range(2):
                    ni,nj = i+ai[k], j+aj[k]
                    if 0<=ni<N and 0<=nj<M and arr[ni][nj] != 0:
                        cnt + arr[ni][nj]
                

                for k in range(2):
                    ni,nj = i+bi[k], j+bj[k]
                for k in range(2):
                    ni,nj = i+ci[k], j+cj[k]
                for k in range(2):
                    ni,nj = i+di[k], j+dj[k]
            

