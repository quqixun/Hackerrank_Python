T = int(input())

for _ in range(T):
    S = input()
    S_len = len(S)
    evenS = [S[i] for i in range(S_len) if i % 2 == 0]
    oddS = [S[i] for i in range(S_len) if i % 2 == 1]
    print(" ".join(["".join(evenS), "".join(oddS)]))