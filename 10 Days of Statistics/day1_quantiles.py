def median(l):
    idx = (len(l) + 1) / 2
    idxi = int(idx)
    if idxi == idx:
        return l[idxi - 1], idxi - 1, idxi
    else:
        return (l[idxi - 1] + l[idxi]) // 2, idxi, idxi


n = int(input().strip())
xs = list(map(int, input().strip().split()))
xs.sort()

Q2, Q1_end, Q3_beg = median(xs)
Q1, _, _ = median(xs[:Q1_end])
Q3, _, _ = median(xs[Q3_beg:])

print(Q1)
print(Q2)
print(Q3)
