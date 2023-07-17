n = input()
m = ""
for i in range(len(n)):

    for j in range(i+1, len(n)):
        if n[i] == n[j]:
            m = n[i:j+1]

print(m)
print(m)