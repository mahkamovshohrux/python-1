n = input("n;")
s = ""
for i in n:
    if i not in s:
        s += i
print(len(s))