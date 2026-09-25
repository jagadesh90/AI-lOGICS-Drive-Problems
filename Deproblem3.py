problem 3:-

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

res = []
c = 0
i = 0

while i < n or i < m or c:
    x = a[i] if i < n else 0
    y = b[i] if i < m else 0

    total = x + y + c

    res.append(total % 10)
    c= total // 10

    i += 1

print(*result)