n = list(map(int, input().split()))
m = int(input("m;"))

for i in range(len(n)-1):
    if n[i] + n[i+1] == m:
        print([i, i+1])