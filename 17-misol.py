n = [[], [], ["a", 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
m = input("m=")
s = []
if len(m) == 2:
    if int(m[0]) > 1 and int(m[1]) > 1:
        for i in n[int(m[0])]:
            for j in n[int(m[1])]:
                if i+j not in s:
                    s.append(i+j)
    elif int(m[0]) > 1:
        print(n[int(m[0])])

    elif int(m[1]) > 1:
        print(n[int(m[1])])
    else:
        print(False)
elif len(m) == 1 and int(m) > 1:
    print(n[int(m)])
elif len(s) > 0:
    print(s)
else:
    print(False)
