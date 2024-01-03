word = input().lower()
w = list(set(word))

fin_list = []
fin = 0
final_word = 0
for i in range(len(w)):
    ans = 0
    for j in range(len(word)):
        if w[i] == word[j]:
            ans += 1
    fin_list.append(ans)
    if fin < ans:
        fin = ans
        final_word = w[i].upper()
# print(fin_list)
# print(len(set(fin_list)))
max_word = max(fin_list)
cnt = 0
for i in range(len(fin_list)):
    if fin_list[i] == max_word:
        cnt += 1
if cnt > 1:
    print('?')
else:
    print(final_word)