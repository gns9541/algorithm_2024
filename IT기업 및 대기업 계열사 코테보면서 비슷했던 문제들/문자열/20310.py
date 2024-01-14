S = input()

cnt_z = 0
cnt_o = 0
for i in (S):
    if i == '0':
        cnt_z += 1
    else:
        cnt_o += 1

cnt_z = cnt_z//2
cnt_o = cnt_o//2

ans = ''
for i in range(cnt_z):
    ans+='0'
for i in range(cnt_o):
    ans+='1'


print(ans)