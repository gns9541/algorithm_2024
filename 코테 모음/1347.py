N = int(input())
way = input()

di = [1,0,-1,0] # 아래 왼 위 오
dj = [0,-1,0,1]

arr = [['#']*200 for _ in range(200)]

i,j = 100,100
k = 0
a = 0
while True:
    if a == N:
        break
    if way[a] == 'R':
        k+=1
    if way[a] == 'L':
        k-=1
    if k == 4:
        k = 0
    if k == -1:
        k = 3
    if way[a] == 'F':
        ni,nj = i+di[k],j+dj[k]
        arr[i][j] = '.'
        arr[ni][nj] = '.'
        i,j = ni,nj  
    a+=1

# print(*arr, sep="\n")

min_x = 200
min_y = 200
max_x = 0
max_y = 0
for i in range(200):
    for j in range(200):
        if arr[i][j] == '.':
            min_x = min(min_x,i)
            min_y = min(min_y,j)
            max_x = max(max_x,i)
            max_y = max(max_y,j)
# print(min_x,min_y,max_x,max_y)

for i in range(min_x,max_x+1):
    ans = ''
    for j in range(min_y,max_y+1):
        ans+=arr[i][j]
    print(ans)




