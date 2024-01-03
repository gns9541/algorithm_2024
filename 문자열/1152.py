word = input()
ans = 0
for i in range(len(word)):
    if word[i] == ' ':
        ans +=1
if word[0] == ' ':
    ans-=1
if word[-1] == ' ':
    ans-=1

print(ans+1)