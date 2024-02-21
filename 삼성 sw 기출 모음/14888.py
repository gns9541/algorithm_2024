N = int(input())
A = list(map(int, input().split()))
# plus, minus, times, devide = map(int, input().split())
lst = list(map(int, input().split()))

def cal(i,x,y):
    if i == 0:
        return x+y
    elif i == 1:
        return x-y
    elif i == 2:
        return x*y
    elif i == 3:
        if x<0:
            return -(-x//y)
        else:
            return x//y

ans = []
def dfs(x,y,lst):
    if lst == [0,0,0,0]:
        ans.append(x)
        return
    # if y == N:
    #     print(x)
    #     ans.append(x)
    #     return
    for i in range(4):
        if lst[i] > 0:
            temp_x = x
            x = cal(i,x,A[y])
            lst[i]-=1
            dfs(x,y+1,lst)
            lst[i]+=1
            x = temp_x
        else:
            pass

dfs(A[0],1,lst)
print(max(ans))
print(min(ans))

