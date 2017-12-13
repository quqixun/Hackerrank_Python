N = int(input().strip())
xs = list(map(int, input().strip().split()))
ws = list(map(int, input().strip().split()))

wxs = [x * w for x, w in zip(xs, ws)]
print("{0:.1f}".format(sum(wxs) / sum(ws)))
