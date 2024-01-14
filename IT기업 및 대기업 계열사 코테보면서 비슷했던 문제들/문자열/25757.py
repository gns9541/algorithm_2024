N, Game = map(str, input().split()) # y:2, f:3, o:4
N = int(N)
people = [input() for _ in range(N)]
people = list(set(people))

ans = 0
# for i in range(people):
if Game == 'Y':
        ans = len(people)
elif Game == 'F':
        ans = len(people) // 2
else:
        ans = len(people) // 3
print(ans)