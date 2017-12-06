# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input().strip())
p = list(map(int, input().strip().split(" ")))

for x in range(1, n + 1):
    print(p.index(p.index(x) + 1) + 1)
