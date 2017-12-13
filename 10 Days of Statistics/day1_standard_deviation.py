import math

n = int(input().strip())
xs = list(map(int, input().strip().split()))

mean = sum(xs) / n
sqds = sum([(x - mean) ** 2 for x in xs])
sd = math.sqrt(sqds / n)

print("{0:.1f}".format(sd))
