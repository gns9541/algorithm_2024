from collections import deque

N = int(input())
rain_map = [list(map(int, input().split())) for _ in range(N)]
max_num = 0
res = []
for i in range(N):
    for j in range(N):
        if rain_map[i][j]>max_num:
            max_num = rain_map[i][j]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y, num):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < N and 0 <= ny < N:
                if rain_map[nx][ny] > num and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

for k in range(max_num):
    visited = [[0]*N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if rain_map[i][j] > k and visited[i][j] == 0:
                cnt += 1
                bfs(i,j,k)
    res.append(cnt)
print(max(res))

