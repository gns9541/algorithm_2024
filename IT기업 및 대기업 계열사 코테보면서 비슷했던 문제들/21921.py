# N,X = map(int, input().split())
# V = list(map(int, input().split()))
# date = N-X

# now_sum = sum(V[:X])
# max_sum = now_sum

# visitors = []
# for i in range(N-X+1):
#     cnt = 0
#     for j in range(X):
#         cnt += V[j+i]
#     visitors.append(cnt)
# # print(visitors)
# for i in range(X,N):
#     now_sum = now_sum - V[i-X]+V[i]
#     max_sum = max(max_sum, now_sum)


# if max_sum == 0:
#     print('SAD')
# else:
#     print(max_sum)
#     cnt = 0
#     for i in range(len(visitors)):
#         if visitors[i] == max_sum:
#             cnt +=1
#     print(cnt)

N, X = map(int, input().split())
V = list(map(int, input().split()))

# 처음 X개의 합을 구함
current_sum = sum(V[:X])
max_sum = current_sum
count = 1 if max_sum > 0 else 0

# 현재 구간의 합을 이용해 다음 구간의 합을 갱신
for i in range(X, N):
    current_sum = current_sum - V[i - X] + V[i]
    if current_sum == max_sum:
        count += 1
    elif current_sum > max_sum:
        max_sum = current_sum
        count = 1

# 최대 합 출력
if max_sum == 0:
    print('SAD')
else:
    print(max_sum)
    print(count)


