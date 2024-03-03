import heapq
import sys

n = int(sys.stdin.readline())

leftHeap = []
rightHeap = []
for i in range(n):
    num = int(sys.stdin.readline())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -num)
    else:
        heapq.heappush(rightHeap, num)

    if rightHeap and rightHeap[0] < -leftHeap[0]:
        leftValue = heapq.heappop(leftHeap)
        rightValue = heapq.heappop(rightHeap)

        heapq.heappush(leftHeap, -rightValue)
        heapq.heappush(rightHeap, -leftValue)

    # print(leftHeap,rightHeap)
    print(-leftHeap[0])
    # print('')
# import heapq

# # 빈 힙 생성
# heap = []

# # 원소 추가
# heapq.heappush(heap, 4)
# heapq.heappush(heap, 1)
# heapq.heappush(heap, 7)
# heapq.heappush(heap, 3)

# print("현재 힙:", heap)

# # 최소 원소 삭제 및 반환
# min_element = heapq.heappop(heap)
# print("가장 작은 원소:", min_element)
# print("최소 원소 삭제 후 힙:", heap)
