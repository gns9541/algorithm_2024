N = int(input())
body = [list(map(str, input().split())) for _ in range(N)]

heart = []
real = []
for i in range(N):
    flag = 0
    for j in range(N):
        if body[i][0][j] == '*':
            heart=[i+2,j+1]
            real=[i+1,j]
            flag = 1
            break
    if flag == 1:
        break
print(*heart)

#허리
cnt_a = 0
for k in range(real[0]+1,N):
    if body[k][0][real[1]] == '*':
        cnt_a +=1
    else:
        break

#왼팔
cnt_b = 0
for k in range(0,real[1]):
    if body[real[0]][0][k] == '*':
        cnt_b +=1

#오른팔
cnt_c = 0
for k in range(real[1]+1,N):
    if body[real[0]][0][k] == '*':
        cnt_c +=1

#왼다리
cnt_d = 0
for k in range(real[0]+1+cnt_a,N):
    if body[k][0][real[1]-1] == '*':
        cnt_d +=1

#오른다리
cnt_e = 0
for k in range(real[0]+1+cnt_a,N):
    if body[k][0][real[1]+1] == '*':
        cnt_e +=1


print(cnt_b,cnt_c,cnt_a,cnt_d,cnt_e)