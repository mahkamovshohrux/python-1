a = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9,
                'V': 5, 'IV': 4, 'I': 1}

n = input()
j = 0
i = 0
while i < len(n):
    if i + 1 < len(n) and n[i:i + 2] in a:
        j += a[n[i:i + 2]]
        i += 2
    else:
        j += a[n[i]]
        i += 1
print(j)
print(j)