N = int(input())
height_count = list(map(int, input().split()))
queue = [0]*N
for i in range(N):
    cnt = 0
    for j in range(N):
        if cnt == height_count[i] and queue[j] == 0:
            queue[j] = i+1
            break
        else:
            if queue[j] == 0:
                cnt += 1
print(*queue)
 
