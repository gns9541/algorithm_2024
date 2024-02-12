from copy import deepcopy
from itertools import permutations
N,M,K = map(int, input().split())
arr = [[0]*(M+1)]+[[0]+list(map(int, input().split())) for _ in range(N)]
eq = [list(map(int, input().split())) for _ in range(K)]
new = deepcopy(arr)

print(ways)
print(eq)
print(*arr, sep="\n")
square = []
for i in range(K):
    square.append([[eq[i][0]-eq[i][2], eq[i][1]-eq[i][2]], [eq[i][0]+eq[i][2], eq[i][1]+eq[i][2]]])
print(square)

# for i in range()



