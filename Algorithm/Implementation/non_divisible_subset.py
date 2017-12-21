n, k = map(int, input().strip().split(" "))
arr = map(int, input().strip().split(" "))

counter = [0] * k
for a in arr:
    counter[a % k] += 1

num = min(counter[0], 1)
for i in range(1, (k // 2) + 1):
    if i != k - i:
        num += max(counter[i], counter[k - i])
    else:
        num += min(counter[i], 1)
print(num)
