n = input()
if n == n[::-1]:
    print(True)
else:
    print(False)




# n = list(map(int, input().split()))
# k = int(input())
# m = []
# for i in range(len(n)-k+1):
#     m.append([])
#     for j in range(i, i+k):
#         m[i].append(n[j])
# x = []
# for i in m:
#     x.append(max(i))
# print(x)

# n = list(map(int, input().split()))
# k = int(input())
# y = []
# for i in n:
#     x = n.count(i)
#     if x not in y:
#        y.append(x)
# y.sort()
#
# y = y[::-1]
# y = y[k-1:]
# print(y)
# for i in n:
#     if n.count(i) == max(y):
#         print(i)
#         break
