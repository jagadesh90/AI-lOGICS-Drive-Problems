problem 1

n = int(input())

ranges = []
for _ in range(n):
    start, end = map(int, input().split())
    ranges.append([start, end])
ranges.sort()

result = []

for start, end in ranges:

    if not result or start > result[-1][1]:
        result.append([start, end])
    else:
        result[-1][1] = max(result[-1][1], end)

for start, end in result:
    print(start, end)