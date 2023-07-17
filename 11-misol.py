# n = list(map(int, input().split(",")))
# n1 = n[::-1]
# s1 = []
# for i in n:
#     for j in n1:
#         if i > j:
#             s1.append(abs((n1.index(j) - n.index(i)+1) * j))
#         else:
#             s1.append(abs((n1.index(j) - n.index(i)+1) * i))
#
# print(max(s1))
def f(n):
    n = int(n)
    return n//2 + n % 2
print(sum(map(f, input().split())))
print()