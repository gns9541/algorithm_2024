from itertools import combinations
import sys

def solution(n, edges, users, d, limit):
    answer = 0
    
    # 그래프 초기화
    graph = {i: [] for i in range(1, n + 1)}
    for edge in edges:
        graph[edge[0]].append((edge[1], edge[2]))
        graph[edge[1]].append((edge[0], edge[2]))
    print(graph)
    
    # 모든 가능한 파킹존 조합을 확인
    for parking_zones in combinations(range(1, n + 1), 2):
        total_users = 0
        
        # 해당 조합에서의 최단 거리 계산
        distances = [sys.maxsize] * (n + 1)
        distances[parking_zones[0]] = 0
        distances[parking_zones[1]] = 0
        queue = [parking_zones[0], parking_zones[1]]
        
        while queue:
            current_node = queue.pop(0)
            for neighbor, edge_distance in graph[current_node]:
                if distances[neighbor] > distances[current_node] + edge_distance:
                    distances[neighbor] = distances[current_node] + edge_distance
                    queue.append(neighbor)
        
        # 유저가 이동 가능한 거리 내에 있는 파킹존에 대한 계산
        for i in range(n):
            if distances[i + 1] <= d:
                total_users += users[i]
        
        # 최대 바이크 수를 넘지 않는 경우에만 정답 갱신
        if total_users <= limit:
            answer = max(answer, total_users)
        
    
    return answer

# 예시 테스트
n = 7
edges = [[1,2,2],[5,2,2],[1,3,1],[1,6,2],[1,7,3],[6,7,4],[7,4,1]]
users = [0,2,0,0,0,4,1]
d = 2
limit = 3
result = solution(n, edges, users, d, limit)
print(result)  # 출력 결과: 6
