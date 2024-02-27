from itertools import permutations

N = int(input())
cards = [list(map(int, input().split())) for _ in range(N)]

ans = []
for i in cards:
    a = list(permutations(i,3))
    num = 0
    for k in a:
        num = max(num,int(str(sum(k))[-1]))
    ans.append(num)

result = 0
num = 0
for i in range(N):
    if num<=ans[i]:
        num = ans[i]
        result = i+1
print(result)

