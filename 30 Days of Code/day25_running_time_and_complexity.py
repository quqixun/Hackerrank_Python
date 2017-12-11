import math


def is_prime(n):
    if n < 2:
        return False
    elif n < 4:
        return True
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


T = int(input().strip())
for t in range(T):
    n = int(input().strip())
    print("Prime" if is_prime(n) else "Not prime")
