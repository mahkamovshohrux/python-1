n = int(input())
if n > 0:
    n = str(n)
    print(n[::-1])
else:
    n = str(n)
    n = n[1::]
    print(-int(n[::-1]))
    print()