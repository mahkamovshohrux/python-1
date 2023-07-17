n = list(map(int, input().split()))
m = int(input("m="))
x = []
for i in range(len(n)-1):
    for j in range(2, len(n)):
        if i != j and i + 1 != j:
            s = n[i] + n[i+1] + n[j]
            if s not in x:
                x.append(abs(s))

print(x)

