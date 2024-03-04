## 시간초과!!!!!!!!!!

import sys
sys.setrecursionlimit(10000)
N,M = map(int, input().split())
lst = [list(input()) for _ in range(N)]
K = int(input())
ans = 0

def switch(j,k):
    global ans,lst
    if k == K:
        cnt = 0
        for i in range(N):
            if '0' not in lst[i]:
                cnt += 1
        ans = max(cnt,ans)
        return
    
    original_lst = [row[:] for row in lst]

    for i in range(N):
        if lst[i][j] == '0':
            lst[i][j] = '1'
        else:
            lst[i][j] = '0'
            
    if len(lst[0]) != 1:
        for a in range(M):
            if a != j:
                switch(a,k+1)
    elif len(lst[0]) == 1:
        switch(j,k+1)
    lst = original_lst

for j in range(M):
    switch(j,0)

print(ans)