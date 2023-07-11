n = list(map(int, input("n").split()))
m = list(map(int, input("m").split()))
s1 = ""
s2 = ""
for i in range(len(n)):
    s1 += str(n[i])
    s2 += str(m[i])
s = int(s1) + int(s2)
s = str(s)
s3 = s[::-1]
s4 = []
for i in s3:
    s4.append(int(i))
print(s4)