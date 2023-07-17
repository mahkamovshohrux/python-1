n = list(map(str, input().split()))
m = n[0]
s = ""
if len(n) == 0:
    print("")
for i in range(1, len(n)):
    while n[i].find(m) != 0:
        m = m[:-1]
        print(m)
        if not m:
            print(m)
print(m)
