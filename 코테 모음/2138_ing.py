num = int(input())
cur = list(map(int,input()))
bck = cur[:] #백업용으로 초기 cur값 저장
gl = list(map(int,input()))
rst = 0
for j in range(2): #전구 키고,껏을 때
    cur[0] = (cur[0]+j)%2
    cur[1] = (cur[1]+j)%2
    for i in range(1,num): #전구를 일직선상으로 탐색할 때
        if cur[i-1]!=gl[i-1]:
            rst+=1
            cur[i-1]=(cur[i-1]+1)%2
            cur[i]=(cur[i]+1)%2
            if i!=num-1:
                cur[i+1]=(cur[i+1]+1)%2
    for i in range(num): #gl값과 일치하는지 확인
        if cur[i]!=gl[i]:
            cur = bck[:]
            rst = 1
            break
    else:
        print(rst)
        exit(0)
print(-1) #2번다 일치 하지 않을 때