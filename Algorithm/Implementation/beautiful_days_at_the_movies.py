inputs = input().split(" ")
i, j, k = [int(e) for e in inputs]

num = 0
for n in range(i, j + 1):
    nr = int(str(n)[::-1])
    if abs(nr - n) % k == 0:
        num += 1
print(num)
