W = input()
B = input()
stack = []

for char in W:
    stack.append(char)
    if len(stack) >= len(B) and ''.join(stack[-len(B):]) == B:
        # 폭발 문자열이 들어있으면 제거
        del stack[-len(B):]

result = ''.join(stack)

if not result:
    print('FRULA')
else:
    print(result)