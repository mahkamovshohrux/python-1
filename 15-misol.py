n = list(map(int, input().split()))
x = []
for i in range(len(n)-1):
    for j in range(len(n)):
        if i != j and i + 1 != j:
            if n[i]+n[i+1]+n[j] == 0:
                l = sorted([n[i], n[i+1], n[j]])
                if l not in x:
                    x.append(l)
print(x)