def solution(grid, d, k):
    MOD = 1000000007  # 나머지 연산에 사용할 값
    n = len(grid)  # 격자의 행 수
    m = len(grid[0])  # 격자의 열 수

    dp = [[0] * m for _ in range(n)]  # 각 칸에서 시작하는 경로의 수를 저장할 배열

    # dp[i][j]를 계산하는 함수
    def calculate_path_count(i, j):
        if dp[i][j] != 0:
            return dp[i][j]
        
        # 현재 칸에서 시작하는 경로의 수 초기화
        path_count = 0
        
        # 주어진 경사 수열 d를 k번 반복하여 경로의 수를 계산
        for idx in range(len(d) * k):
            x = i + idx // m
            y = j + idx % m
            
            if x >= n or y >= m:
                break
            
            # 경사 수열에 맞는 조건인 경우 경로의 수를 누적
            if grid[x][y] - grid[i][j] == d[idx % len(d)]:
                path_count = (path_count + calculate_path_count(x, y)) % MOD
        
        dp[i][j] = path_count
        return path_count
    
    # 각 칸에서 시작하는 경로의 수 계산
    total_path_count = 0
    for i in range(n):
        for j in range(m):
            total_path_count = (total_path_count + calculate_path_count(i, j)) % MOD

    return total_path_count


grid = [list(map(int, input().split())) for _ in range(n)]  # 격자의 각 칸의 높이 입력
d = list(map(int, input().split()))  # 경사 수열 입력
k = int(input())  # 경사 수열을 반복하는 횟수 입력

# 결과 출력
print(solution(grid, d, k))
