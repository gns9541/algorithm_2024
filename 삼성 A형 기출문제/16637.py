N = int(input())
eq = input()
result = -1*2**31

def dfs(i, number):
    global result
    if i == N-1:
        result = max(result, number)
        return 
    if i+2<N:
        next = cal(number, int(eq[i+2]),eq[i+1])
        dfs(i+2, next)
    if i+4<N:
        next_next = cal(int(eq[i+2]), int(eq[i+4]), eq[i+3])
        next = cal(number, next_next, eq[i+1])
        dfs(i+4, next)

def cal(a,b,w):
    if w == '+':
        num = a+b
    elif w == '-':
        num = a-b
    elif w == '*':
        num = a*b
    return num

dfs(0,int(eq[0]))
print(result)