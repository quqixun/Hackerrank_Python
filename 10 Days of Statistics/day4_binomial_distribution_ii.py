def fact(n):
    return 1 if n == 0 else n * fact(n - 1)


def nCr(n, r):
    return fact(n) / (fact(r) * fact(n - r))


def prob(pct, aln, bsz):
    p = [(pct ** i) * ((1 - pct) ** (bsz - i)) * nCr(bsz, i) for i in range(aln, bsz + 1)]
    return sum(p)


print("{0:.3f}".format(prob(0.88, 8, 10)))
print("{0:.3f}".format(prob(0.12, 2, 10)))
