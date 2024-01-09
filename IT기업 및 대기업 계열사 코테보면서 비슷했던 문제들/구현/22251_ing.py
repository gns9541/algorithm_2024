from itertools import combinations

N,K,P,X = map(int, input().split()) 
# 9 1 2 5
# 총N층, K자리수, P개 반전, 현재 X층
# num = [list([0]*3) for _ in range(5)]
# print(*num, sep="\n")


nums = ['1111110','0011000','0110111','0111101','1011001',
       '1101101','1101111','0111000','1111111','1111101']
ans = []

print(list(nums))
idx = [0,1,2,3,4,5,6]
changes = []
for i in combinations(idx,P):
    changes.append(list(i))
print('바꿀',changes)

for i in range(9):
    a = list(nums[i])
    print(a)
    if i != X-1:
        for j in changes:
            for k in range(len(j)):
                # print(j[k])
                if a[j[k]] == '1':
                    a[j[k]] = '0'
                else:
                    a[j[k]] = '1'
            if "".join(a) in nums:
                if "".join(a) != nums[X-1]:
                    ans.append("".join(a))
print(set(ans))


            
