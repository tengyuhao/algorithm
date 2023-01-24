"""

Bubble Sort

0   1   2   3   4
ROUND 1
5   1   3   4   2
------------------
1   5   3   4   2       i = 0, 1
1   3   5   4   2       i = 1, 2
1   3   4   5   2       i = 2, 3
1   3   4   2   5       i = 3, 4    max = n-1
------------------

ROUND 2
1   3   4   2   5
------------------
1   3   4   2   5       i = 0, 1
1   3   4   2   5       i = 1, 2
1   3   2   4   5       i = 2, 3
1   3   2   4   5       i = 3, 4   max = n-2
------------------

1   3   2   4   5
------------------
1   3   2   4   5
1   2   3   4   5
1   2   3   4   5
1   2   3   4   5
------------------
"""

a = [5, 1, 3, 4, 2]

# maxn = max(a)
# print(maxn)
#
# for i in range(len(a)):
#     if maxn == a[i]:
#         a[i] = a[i+1]
#         a[i+1] = maxn
#         break
# print(a)


def swap(a, x, y):
    a[i], a[i+1] = a[i+1], a[i]
print(a)

for i in range(len(a)-1):
    if a[i+1] < a[i]:
        swap(a, a[i], a[i+1])


print(a)

for i in range(len(a)-1):
    if a[i+1] < a[i]:

        swap(a, a[i], a[i+1])


print(a)

for i in range(len(a)-1):
    if a[i+1] < a[i]:

        swap(a, a[i], a[i+1])


print(a)

for i in range(len(a)-1):
    if a[i+1] < a[i]:

        swap(a, a[i], a[i+1])


print(a)