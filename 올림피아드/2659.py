from itertools import product
N = list(map(int, input().split()))

min_num = 9999

def make_num(lst,i):
    if i == 0:
        return (lst[0]*1000) + (lst[1]*100) + (lst[2]*10) + lst[3]
    if i == 1:
        return (lst[1]*1000) + (lst[2]*100) + (lst[3]*10) + lst[0]
    if i == 2:
        return (lst[2]*1000) + (lst[3]*100) + (lst[0]*10) + lst[1]
    if i == 3:
        return (lst[3]*1000) + (lst[0]*100) + (lst[1]*10) + lst[2]

def find(N,min_num):
    for i in range(4):
        if make_num(N,i) < min_num:
            min_num = make_num(N,i)
    return min_num
result = find(N,9999)
# print(min_num)

cnt = 1
for i in range(1111, result):
    if '0' not in list(str(i)) and i == find(list(map(int, str(i))),9999):
        cnt += 1
print(cnt)


