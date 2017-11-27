n = int(input())
hike = input()

height = 0
vally_num = 0

for h in hike:
    if h == "U":
        if height < 0 and height + 1 >= 0:
            vally_num += 1
        height += 1
    else:
        height -= 1

print(vally_num)
