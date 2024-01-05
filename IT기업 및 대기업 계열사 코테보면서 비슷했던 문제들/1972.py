import heapq as hq # 힙큐를 hq로 쓰기
import sys
N = int(input())
# lst = [int(input()) for _ in range(N)]
# print(lst)

heap = []
for _ in range(N):
    i = int(sys.stdin.readline())
    if i !=0:
        hq.heappush(heap,i)
    else:
        if len(heap)>0:
            print(hq.heappop(heap))
            # print(heap)
        else:
            print(0)