def fact(n):
    return 1 if n == 0 else n * fact(n - 1)


def nCr(n, r):
    return fact(n) / (fact(r) * fact(n - r))


bprob = 1.09 / (1 + 1.09)
gprob = 1 - bprob
probs = [(bprob ** i) * (gprob ** (6 - i)) * nCr(6, i) for i in range(3, 7)]
print("{0:.3f}".format(sum(probs)))
