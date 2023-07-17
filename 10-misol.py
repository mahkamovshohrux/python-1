n = input()
m = input()
if n == m:
    print(True)
elif len(n) != len(m):
    print(False)
else:
    s = ""
    for i in range(len(n)):
        if n[i] == m[i] or m[i] == "*" or m[i] == ".":
            s += n[i]
        else:
            print(False)
            break
    print(len(s) == len(m))
print()