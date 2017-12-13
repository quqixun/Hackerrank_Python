import numpy as np
from scipy import stats

N = int(input().strip())
xs = list(map(int, input().strip().split()))
print(np.mean(xs))
print(np.median(xs))
print(int(stats.mode(xs)[0]))
