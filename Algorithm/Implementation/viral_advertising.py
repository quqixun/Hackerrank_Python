n = int(input())
all_people = 5
like_people = all_people // 2
all_like = like_people
for _ in range(1, n):
    all_people = like_people * 3
    like_people = all_people // 2
    all_like += like_people

print(all_like)
