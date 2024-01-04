from collections import Counter
N, M = map(int, input().split())
words = []
for _ in range(N):
    w = input()
    if len(w)>=M:
        words.append(w)

print(words)

# words_set = set(words)
# print(words_set)

sorted_list = sorted(words, key=lambda x: words.count(x), reverse=True)

print(sorted_list)
words_set = set(sorted_list)
print(words_set)
# for i in range(M):
