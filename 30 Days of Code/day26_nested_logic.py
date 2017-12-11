ad, am, ay = map(int, input().strip().split(" "))
ed, em, ey = map(int, input().strip().split(" "))

hackos = 0

if ay == ey:
    if am <= em:
        if ad > ed:
            hackos = 15 * (ad - ed)
    else:
        hackos = 500 * (am - em)
elif ay > ey:
    hackos = 10000

print(hackos)
