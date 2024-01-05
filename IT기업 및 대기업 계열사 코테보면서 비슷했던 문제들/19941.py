N, K = map(int,input().split())
lst = input().rstrip()
fin_lst = list(lst)

cnt = 0
for i in range(N):
    if fin_lst[i] == 'P':
        for j in range(i-K,i+K+1):
            if 0<=j<N and fin_lst[j] == 'H':
                    cnt += 1
                    fin_lst[j] = 0
                    break
print(cnt)     

