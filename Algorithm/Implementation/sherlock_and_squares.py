import math

T = int(input().strip())

for i in range(T):
    A, B = map(int, input().strip().split(" "))
    sA = math.ceil(math.sqrt(A))
    sB = math.floor(math.sqrt(B))
    diff = sB - sA
    if diff < 0:
        print(0)
    else:
        print(diff + 1)
