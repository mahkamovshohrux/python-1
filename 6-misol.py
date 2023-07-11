
n = [['P', '', 'A', '', 'H', '', 'N'], ['A', 'P', 'L', 'S', 'I', 'I', 'G'], ['Y', '', 'I', '', 'R', '', '']]
m = ''
for i in n:
    for j in range(len(n[0])):
        if i[j] != "":
            m += i[j]
print(m)