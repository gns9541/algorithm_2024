from collections import deque

def bfs(n, m, maze):
    if n == 1 and m == 1:
        return 1  # 시작점과 도착점이 같은 경우

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 방향
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]  # 벽을 부순 경우와 아닌 경우 각각의 visited 배열

    queue = deque([(0, 0, 0)])  # 시작점 (행, 열, 벽을 부순 횟수)
    visited[0][0][0] = True

    while queue:
        x, y, wall_break = queue.popleft()
        
        # 도착점에 도달한 경우
        if x == n-1 and y == m-1:
            return visited[x][y][wall_break]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 맵 범위를 벗어나지 않고 방문하지 않은 곳인 경우
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][wall_break]:
                # 이동 가능한 경우
                if maze[nx][ny] == 0:
                    queue.append((nx, ny, wall_break))
                    visited[nx][ny][wall_break] = visited[x][y][wall_break] + 1
                # 벽을 부수고 이동하는 경우
                elif maze[nx][ny] == 1 and wall_break == 0:
                    queue.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][wall_break] + 1

    return -1  # 도달할 수 없는 경우

# 입력
n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

# 출력
result = bfs(n, m, maze)
print(result)
