n = input()
s = ""
for i in range(len(n)):
    if n[i].isdigit():
        s += n[i]
print(s)