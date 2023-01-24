"""

"""

a = [5, 1, 3, 4, 2]
N = len(a)


def swap(a, x, y):
    a[i], a[i + 1] = a[i + 1], a[i]


for j in range(N - 1):
    print(j, j + 1)
    for i in range(N-1):
        if a[i+1] < a[i]:
            print(i, i+1)
            swap(a, a[i], a[i+1])

