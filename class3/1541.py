from collections import deque
# -를 기준으로 나누면 최소 가능
arr = input().split('-')
# print(arr)
ans = []
for i in arr:
    new = i.split('+')
    # print(new)
    plus = 0
    for j in range(len(new)):
        plus+=int(new[j])
    ans.append(plus)
# print(ans)
res = ans[0]
for i in range(1,len(ans)):
    res-=ans[i]
print(res)
