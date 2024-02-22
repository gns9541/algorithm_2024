dice = [list(map(int,input().split())) for _ in range(6)]
# print(*dice, sep="\n")

# 인접한 면이 직선으로 두번 이동해서 만날 수 있으면 전개도?

di=[1,-1,0,0]
dj=[0,0,1,-1]

ans = 0
num = 0
lst = []
new = []
for i in range(6):
    for j in range(6):
        if dice[i][j] != 0:
            cnt = 0
            zero_count = 0
            for k in range(4):
                ai,aj = i+di[k], j+dj[k]
                ni,nj = i+2*di[k], j+2*dj[k]
                if (0<=ni<6 and 0<=nj<6 and dice[ni][nj] == 0) or (0>ni or 6<=ni or 0>nj or 6<=nj):
                    zero_count+=1
            
            if zero_count == 4:
                print(zero_count)
                for k in range(4):
                    ai,aj = i+di[k], j+dj[k]
                    if 0<=ai<6 and 0<=aj<6 and dice[ai][aj]!=0:
                        si,sj = i+2*di[k], j+2*dj[k]
                        if 0<=si<6 and 0<=sj<6:
                            for l in range(4):
                                li,lj = i+2*di[l], j+2*dj[l]
                                if 0<=li<6 and 0<=lj<6 and dice[li][lj]!=0 and dice[li][lj]!=dice[ai][aj]:
                                    cnt+=1
                                    lst.append(dice[si][sj])
                                    if dice[i][j] == 1:
                                        num = dice[si][sj]
            else:
                for k in range(4):
                    ni,nj = i+2*di[k], j+2*dj[k]
                    if 0<=ni<6 and 0<=nj<6:
                        if dice[ni][nj] != 0:
                            cnt += 1
                            lst.append(dice[ni][nj])
                            if dice[i][j] == 1:
                                num = dice[ni][nj]
                                break

            if cnt==1:
                ans+=1
            print(dice[i][j],cnt,lst)

for i in lst:
    if i == 1:
        new.append(i)
    elif i == 2:
        new.append(i)
    elif i == 3:
        new.append(i)
    elif i == 4:
        new.append(i)
    elif i == 5:
        new.append(i)
    elif i == 6:
        new.append(i)

if len(new) == 6:
    print(num)
else:
    print(0)




                        
            
