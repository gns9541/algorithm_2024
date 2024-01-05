import heapq as hq # 힙큐를 hq로 쓰기
import sys
input = sys.stdin.readline

n = int(input())
heap = []

init_numbers = list(map(int,input().split())) 
for num in init_numbers:
    hq.heappush(heap,num) #list 객체를 풀어서 원소를 heap에 넣어준다.

for i in range(n-1):  
    numbers = list(map(int,input().split())) 
        # heap의 0번째 원소는 해당 입력까지, 모든 수 들 중 n번째 큰 수
        # 입력 한줄 마다 힙 원소를 뒤바꾼다.
    for num in numbers:
        if heap[0] < num :
            hq.heappush(heap,num)
            hq.heappop(heap)

print(heap[0])