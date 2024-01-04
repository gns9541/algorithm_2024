# num = int(input())
# nums = str(num)

nums = input().rstrip()
print(nums)

i = 0
idx = 0
while True:
    i += 1
    for n in str(i):
        if nums[idx] in n:
            idx+=1
            if idx >= len(nums):
                print(i)
                exit()

