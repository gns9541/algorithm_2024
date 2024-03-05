N = int(input())
# stairs = [int(input()) for _ in range(N)]
# print(stairs)

arr = [0]*(301)
for i in range(1,N+1):
    arr[i] = int(input())

dp = [0]*(301)
dp[1] = arr[1]
dp[2] = arr[1] + arr[2]
dp[3] = max(arr[1]+arr[3], arr[2]+arr[3])
# print(dp[3])
for i in range(4,N+1):
    dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])
    # print(dp[i],i)
    # print('')
print(dp[N])